import os
import json
import csv
import shutil
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import aiofiles
from PIL import Image
import hashlib

from app.core.config import settings
from app.models.agent import FilePermission


class SecurityError(Exception):
    """Raised when a security violation is detected"""
    pass


class FileSystemTools:
    """Secure file system tools with granular permissions"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.base_dir = Path(settings.file_access_base_dir).resolve()
        self.max_file_size = settings.file_access_max_size_mb * 1024 * 1024
        self.allowed_extensions = set(settings.file_access_allowed_extensions)
        
        # Create base directory if it doesn't exist
        self.base_dir.mkdir(parents=True, exist_ok=True)
    
    async def check_permission(
        self,
        path: Path,
        permission_type: str,
        file_pattern: Optional[str] = None
    ) -> bool:
        """Check if agent has permission for the requested operation"""
        # TODO: Check from database
        # For now, implement basic security checks
        
        # Ensure path is within base directory
        try:
            resolved_path = path.resolve()
            resolved_path.relative_to(self.base_dir)
        except ValueError:
            raise SecurityError(f"Access denied: Path outside allowed directory")
        
        # Check file extension
        if path.is_file() and path.suffix not in self.allowed_extensions:
            raise SecurityError(f"Access denied: File type not allowed")
        
        return True
    
    async def read_file(
        self,
        file_path: str,
        encoding: str = "utf-8"
    ) -> Dict[str, Any]:
        """Read file content with security checks"""
        path = Path(file_path).resolve()
        
        # Security checks
        await self.check_permission(path, "read")
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if path.stat().st_size > self.max_file_size:
            raise SecurityError(f"File too large: {path.stat().st_size} bytes")
        
        # Read file based on extension
        if path.suffix == ".json":
            async with aiofiles.open(path, "r", encoding=encoding) as f:
                content = await f.read()
                return {
                    "type": "json",
                    "content": json.loads(content),
                    "path": str(path),
                    "size": path.stat().st_size,
                }
        
        elif path.suffix == ".csv":
            rows = []
            async with aiofiles.open(path, "r", encoding=encoding) as f:
                content = await f.read()
                reader = csv.DictReader(content.splitlines())
                rows = list(reader)
            
            return {
                "type": "csv",
                "content": rows,
                "path": str(path),
                "size": path.stat().st_size,
            }
        
        elif path.suffix in [".txt", ".html", ".xml"]:
            async with aiofiles.open(path, "r", encoding=encoding) as f:
                content = await f.read()
            
            return {
                "type": "text",
                "content": content,
                "path": str(path),
                "size": path.stat().st_size,
            }
        
        elif path.suffix in [".png", ".jpg", ".jpeg"]:
            # Return image metadata
            img = Image.open(path)
            return {
                "type": "image",
                "content": {
                    "width": img.width,
                    "height": img.height,
                    "format": img.format,
                    "mode": img.mode,
                },
                "path": str(path),
                "size": path.stat().st_size,
            }
        
        else:
            # Binary file - return metadata only
            return {
                "type": "binary",
                "content": None,
                "path": str(path),
                "size": path.stat().st_size,
                "hash": await self._calculate_file_hash(path),
            }
    
    async def write_file(
        self,
        file_path: str,
        content: Union[str, Dict, List],
        encoding: str = "utf-8",
        create_dirs: bool = True
    ) -> Dict[str, Any]:
        """Write content to file with security checks"""
        path = Path(file_path).resolve()
        
        # Security checks
        await self.check_permission(path, "write")
        
        # Create parent directories if needed
        if create_dirs:
            path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write based on file type
        if path.suffix == ".json":
            content_str = json.dumps(content, indent=2)
        elif path.suffix == ".csv" and isinstance(content, list):
            if content and isinstance(content[0], dict):
                output = []
                keys = content[0].keys()
                output.append(",".join(keys))
                for row in content:
                    output.append(",".join(str(row.get(k, "")) for k in keys))
                content_str = "\n".join(output)
            else:
                raise ValueError("CSV content must be a list of dictionaries")
        else:
            content_str = str(content)
        
        # Check size before writing
        if len(content_str.encode(encoding)) > self.max_file_size:
            raise SecurityError("Content too large")
        
        async with aiofiles.open(path, "w", encoding=encoding) as f:
            await f.write(content_str)
        
        return {
            "path": str(path),
            "size": path.stat().st_size,
            "created": datetime.fromtimestamp(path.stat().st_ctime),
        }
    
    async def list_directory(
        self,
        dir_path: str,
        pattern: str = "*",
        max_depth: int = 3,
        include_hidden: bool = False
    ) -> List[Dict[str, Any]]:
        """List directory contents with security checks"""
        path = Path(dir_path).resolve()
        
        # Security checks
        await self.check_permission(path, "list")
        
        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {dir_path}")
        
        if not path.is_dir():
            raise ValueError(f"Not a directory: {dir_path}")
        
        files = []
        
        def _scan_dir(current_path: Path, depth: int = 0):
            if depth > max_depth:
                return
            
            try:
                for item in current_path.glob(pattern):
                    if not include_hidden and item.name.startswith("."):
                        continue
                    
                    file_info = {
                        "name": item.name,
                        "path": str(item),
                        "type": "directory" if item.is_dir() else "file",
                        "size": item.stat().st_size if item.is_file() else None,
                        "modified": datetime.fromtimestamp(item.stat().st_mtime),
                    }
                    
                    if item.is_file():
                        file_info["extension"] = item.suffix
                    
                    files.append(file_info)
                    
                    if item.is_dir():
                        _scan_dir(item, depth + 1)
            except PermissionError:
                pass
        
        _scan_dir(path)
        return files
    
    async def transform_data(
        self,
        input_path: str,
        output_path: str,
        transformation: str,
        options: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Transform data between formats"""
        options = options or {}
        
        # Read input file
        input_data = await self.read_file(input_path)
        
        # Apply transformation
        if transformation == "json_to_csv":
            if input_data["type"] != "json":
                raise ValueError("Input must be JSON")
            
            # Convert JSON to CSV
            data = input_data["content"]
            if isinstance(data, list) and data and isinstance(data[0], dict):
                await self.write_file(output_path, data)
            else:
                raise ValueError("JSON must be an array of objects")
        
        elif transformation == "csv_to_json":
            if input_data["type"] != "csv":
                raise ValueError("Input must be CSV")
            
            await self.write_file(output_path, input_data["content"])
        
        elif transformation == "resize_image":
            if input_data["type"] != "image":
                raise ValueError("Input must be an image")
            
            img = Image.open(input_path)
            width = options.get("width", img.width)
            height = options.get("height", img.height)
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            img.save(output_path)
        
        else:
            raise ValueError(f"Unknown transformation: {transformation}")
        
        return {
            "input": input_path,
            "output": output_path,
            "transformation": transformation,
        }
    
    async def create_archive(
        self,
        source_paths: List[str],
        archive_path: str,
        compression: str = "zip"
    ) -> Dict[str, Any]:
        """Create archive from files/directories"""
        archive = Path(archive_path).resolve()
        
        # Security check for output
        await self.check_permission(archive, "write")
        
        if compression == "zip":
            with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
                for source in source_paths:
                    source_path = Path(source).resolve()
                    
                    # Security check for each source
                    await self.check_permission(source_path, "read")
                    
                    if source_path.is_file():
                        zf.write(source_path, source_path.name)
                    elif source_path.is_dir():
                        for file in source_path.rglob("*"):
                            if file.is_file():
                                arc_name = str(file.relative_to(source_path.parent))
                                zf.write(file, arc_name)
        else:
            raise ValueError(f"Unsupported compression: {compression}")
        
        return {
            "archive": str(archive),
            "size": archive.stat().st_size,
            "files_count": len(source_paths),
        }
    
    async def extract_archive(
        self,
        archive_path: str,
        extract_to: str
    ) -> Dict[str, Any]:
        """Extract archive to directory"""
        archive = Path(archive_path).resolve()
        dest = Path(extract_to).resolve()
        
        # Security checks
        await self.check_permission(archive, "read")
        await self.check_permission(dest, "write")
        
        dest.mkdir(parents=True, exist_ok=True)
        
        if archive.suffix == ".zip":
            with zipfile.ZipFile(archive, "r") as zf:
                # Check total uncompressed size
                total_size = sum(info.file_size for info in zf.filelist)
                if total_size > self.max_file_size * 10:  # 10x limit for archives
                    raise SecurityError("Archive too large when extracted")
                
                zf.extractall(dest)
        else:
            raise ValueError(f"Unsupported archive format: {archive.suffix}")
        
        return {
            "archive": str(archive),
            "extracted_to": str(dest),
            "files_count": len(list(dest.rglob("*"))),
        }
    
    async def _calculate_file_hash(self, path: Path) -> str:
        """Calculate SHA256 hash of file"""
        sha256_hash = hashlib.sha256()
        async with aiofiles.open(path, "rb") as f:
            while chunk := await f.read(8192):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()


class FileToolsAPI:
    """API endpoints for file tools"""
    
    @staticmethod
    async def grant_permission(
        agent_id: str,
        directory_path: str,
        permission_type: str,
        file_patterns: List[str] = None,
        max_depth: int = 3,
        expires_in_hours: Optional[int] = None
    ) -> Dict[str, Any]:
        """Grant file system permission to an agent"""
        # TODO: Save to database
        return {
            "agent_id": agent_id,
            "directory_path": directory_path,
            "permission_type": permission_type,
            "file_patterns": file_patterns or ["*"],
            "max_depth": max_depth,
            "expires_at": None,  # TODO: Calculate expiration
            "granted_at": datetime.utcnow(),
        }
    
    @staticmethod
    async def revoke_permission(
        agent_id: str,
        permission_id: str
    ) -> Dict[str, Any]:
        """Revoke file system permission"""
        # TODO: Delete from database
        return {
            "message": "Permission revoked successfully",
            "permission_id": permission_id,
        }
    
    @staticmethod
    async def list_permissions(
        agent_id: str
    ) -> List[Dict[str, Any]]:
        """List all permissions for an agent"""
        # TODO: Fetch from database
        return []
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_name: str = Field(default="SimpleAgent", description="Application name")
    app_env: str = Field(default="development", description="Application environment")
    debug: bool = Field(default=True, description="Debug mode")
    secret_key: SecretStr = Field(
        default="your-secret-key-here", description="Application secret key"
    )
    api_prefix: str = Field(default="/api/v1", description="API prefix")

    # Server
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    workers: int = Field(default=4, description="Number of workers")

    # Database
    database_url: str = Field(
        default="sqlite:///./simple_agent.db", description="Database URL"
    )

    # Redis
    redis_url: str = Field(default="redis://localhost:6379/0", description="Redis URL")

    # JWT
    jwt_secret_key: SecretStr = Field(
        default="your-jwt-secret-key", description="JWT secret key"
    )
    jwt_algorithm: str = Field(default="HS256", description="JWT algorithm")
    access_token_expire_minutes: int = Field(
        default=30, description="Access token expiration in minutes"
    )
    refresh_token_expire_days: int = Field(
        default=7, description="Refresh token expiration in days"
    )

    # Browser
    browser_headless: bool = Field(
        default=False, description="Run browser in headless mode"
    )
    browser_timeout: int = Field(
        default=30000, description="Browser operation timeout in milliseconds"
    )
    browser_download_dir: str = Field(
        default="./downloads", description="Browser download directory"
    )

    # File System Access
    file_access_base_dir: str = Field(
        default="./workspace", description="Base directory for file access"
    )
    file_access_max_size_mb: int = Field(
        default=100, description="Maximum file size in MB"
    )
    file_access_allowed_extensions: List[str] = Field(
        default_factory=lambda: [".txt", ".json", ".csv", ".xml", ".html", ".pdf", ".png", ".jpg", ".jpeg"],
        description="Allowed file extensions",
    )

    # Logging
    log_level: str = Field(default="INFO", description="Log level")
    log_format: str = Field(default="json", description="Log format")
    log_file: str = Field(default="./logs/simple_agent.log", description="Log file path")

    # Celery
    celery_broker_url: str = Field(
        default="redis://localhost:6379/1", description="Celery broker URL"
    )
    celery_result_backend: str = Field(
        default="redis://localhost:6379/2", description="Celery result backend"
    )

    # CORS
    cors_origins: List[str] = Field(
        default_factory=lambda: ["http://localhost:3000", "http://localhost:5173"],
        description="CORS allowed origins",
    )
    cors_allow_credentials: bool = Field(
        default=True, description="Allow CORS credentials"
    )

    # Rate Limiting
    rate_limit_enabled: bool = Field(default=True, description="Enable rate limiting")
    rate_limit_per_minute: int = Field(
        default=60, description="Rate limit per minute"
    )


settings = Settings()
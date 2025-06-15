import asyncio
import json
import os
from typing import Dict, List, Optional, Any, Union, Literal
from datetime import datetime
from pathlib import Path

from browser_use import Browser, BrowserConfig
from browser_use.agent.service import Agent
from playwright.async_api import Page, ElementHandle, Browser as PlaywrightBrowser
from pydantic import BaseModel, Field
import aiofiles

from app.core.config import settings


class ActionResult(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    screenshot: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class BrowserAction(BaseModel):
    type: Literal[
        "navigate",
        "click",
        "type",
        "wait",
        "extract",
        "screenshot",
        "execute_js",
        "wait_for_selector",
        "hover",
        "select",
        "upload_file",
        "download",
    ]
    selector: Optional[str] = None
    value: Optional[Union[str, int, bool, Dict[str, Any]]] = None
    options: Optional[Dict[str, Any]] = None


class ElementSelector(BaseModel):
    strategy: Literal["css", "xpath", "text", "role", "test_id"]
    value: str
    fallback: Optional["ElementSelector"] = None
    wait_visible: bool = True
    timeout: int = 10000


class BrowserAutomationEngine:
    def __init__(self):
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
        self.screenshots_dir = Path("./screenshots")
        self.downloads_dir = Path(settings.browser_download_dir)
        self.recordings_dir = Path("./recordings")
        
        # Create directories
        self.screenshots_dir.mkdir(exist_ok=True)
        self.downloads_dir.mkdir(exist_ok=True)
        self.recordings_dir.mkdir(exist_ok=True)

    async def initialize(self, config: Optional[BrowserConfig] = None) -> None:
        """Initialize the browser with configuration"""
        if config is None:
            config = BrowserConfig(
                headless=settings.browser_headless,
                chrome_instance_path="/tmp/chrome",
                disable_security=False,
                extra_chromium_args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                ],
            )
        
        self.browser = Browser(config=config)

    async def start_session(
        self,
        url: Optional[str] = None,
        viewport: Optional[Dict[str, int]] = None,
        user_agent: Optional[str] = None,
        record_video: bool = False,
    ) -> Page:
        """Start a new browser session"""
        if not self.browser:
            await self.initialize()

        context_options = {
            "viewport": viewport or {"width": 1280, "height": 720},
            "user_agent": user_agent,
        }

        if record_video:
            context_options["record_video_dir"] = str(self.recordings_dir)
            context_options["record_video_size"] = viewport or {"width": 1280, "height": 720}

        # Get browser context through browser-use
        async with self.browser as browser_context:
            self.page = await browser_context.new_page()
            
            if url:
                await self.navigate(url)
            
            return self.page

    async def navigate(self, url: str, wait_until: str = "domcontentloaded") -> ActionResult:
        """Navigate to a URL"""
        try:
            if not self.page:
                return ActionResult(success=False, error="No active page session")
            
            response = await self.page.goto(url, wait_until=wait_until)
            
            return ActionResult(
                success=True,
                data={
                    "url": self.page.url,
                    "status": response.status if response else None,
                    "title": await self.page.title(),
                }
            )
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def click(
        self,
        selector: ElementSelector,
        force: bool = False,
        button: str = "left",
        click_count: int = 1,
    ) -> ActionResult:
        """Click on an element"""
        try:
            element = await self._find_element(selector)
            if not element:
                return ActionResult(success=False, error="Element not found")
            
            await element.click(
                force=force,
                button=button,
                click_count=click_count,
            )
            
            return ActionResult(success=True, data={"clicked": selector.value})
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def type_text(
        self,
        selector: ElementSelector,
        text: str,
        clear_first: bool = True,
        delay: int = 50,
    ) -> ActionResult:
        """Type text into an element"""
        try:
            element = await self._find_element(selector)
            if not element:
                return ActionResult(success=False, error="Element not found")
            
            if clear_first:
                await element.clear()
            
            await element.type(text, delay=delay)
            
            return ActionResult(success=True, data={"typed": text})
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def extract_data(
        self,
        selectors: Dict[str, ElementSelector],
        extract_type: str = "text",
    ) -> ActionResult:
        """Extract data from multiple elements"""
        try:
            results = {}
            
            for name, selector in selectors.items():
                element = await self._find_element(selector)
                if element:
                    if extract_type == "text":
                        results[name] = await element.text_content()
                    elif extract_type == "value":
                        results[name] = await element.get_attribute("value")
                    elif extract_type == "href":
                        results[name] = await element.get_attribute("href")
                    elif extract_type == "src":
                        results[name] = await element.get_attribute("src")
                    elif extract_type == "all_attributes":
                        results[name] = await self._get_all_attributes(element)
                else:
                    results[name] = None
            
            return ActionResult(success=True, data=results)
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def take_screenshot(
        self,
        full_page: bool = False,
        clip: Optional[Dict[str, int]] = None,
    ) -> ActionResult:
        """Take a screenshot of the page"""
        try:
            if not self.page:
                return ActionResult(success=False, error="No active page session")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            filepath = self.screenshots_dir / filename
            
            screenshot_options = {
                "path": str(filepath),
                "full_page": full_page,
            }
            
            if clip:
                screenshot_options["clip"] = clip
            
            await self.page.screenshot(**screenshot_options)
            
            return ActionResult(
                success=True,
                data={"path": str(filepath)},
                screenshot=str(filepath),
            )
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def execute_javascript(self, script: str, args: Optional[List[Any]] = None) -> ActionResult:
        """Execute JavaScript in the page context"""
        try:
            if not self.page:
                return ActionResult(success=False, error="No active page session")
            
            result = await self.page.evaluate(script, args)
            
            return ActionResult(success=True, data=result)
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def wait_for_condition(
        self,
        condition: str,
        timeout: int = 30000,
        polling_interval: int = 100,
    ) -> ActionResult:
        """Wait for a JavaScript condition to be true"""
        try:
            if not self.page:
                return ActionResult(success=False, error="No active page session")
            
            script = f"""
                () => {{
                    return new Promise((resolve, reject) => {{
                        const startTime = Date.now();
                        const check = () => {{
                            if ({condition}) {{
                                resolve(true);
                            }} else if (Date.now() - startTime > {timeout}) {{
                                reject(new Error('Timeout waiting for condition'));
                            }} else {{
                                setTimeout(check, {polling_interval});
                            }}
                        }};
                        check();
                    }});
                }}
            """
            
            await self.page.evaluate(script)
            
            return ActionResult(success=True, data={"condition_met": True})
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def handle_file_upload(
        self,
        selector: ElementSelector,
        file_paths: List[str],
    ) -> ActionResult:
        """Handle file upload"""
        try:
            element = await self._find_element(selector)
            if not element:
                return ActionResult(success=False, error="Element not found")
            
            await element.set_input_files(file_paths)
            
            return ActionResult(success=True, data={"uploaded_files": file_paths})
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def get_page_info(self) -> ActionResult:
        """Get current page information"""
        try:
            if not self.page:
                return ActionResult(success=False, error="No active page session")
            
            info = {
                "url": self.page.url,
                "title": await self.page.title(),
                "viewport": self.page.viewport_size,
                "cookies": await self.page.context.cookies(),
            }
            
            return ActionResult(success=True, data=info)
        except Exception as e:
            return ActionResult(success=False, error=str(e))

    async def _find_element(self, selector: ElementSelector) -> Optional[ElementHandle]:
        """Find element using selector strategy"""
        if not self.page:
            return None
        
        try:
            locator = None
            
            if selector.strategy == "css":
                locator = self.page.locator(selector.value)
            elif selector.strategy == "xpath":
                locator = self.page.locator(f"xpath={selector.value}")
            elif selector.strategy == "text":
                locator = self.page.locator(f"text={selector.value}")
            elif selector.strategy == "role":
                role, name = selector.value.split(":", 1) if ":" in selector.value else (selector.value, None)
                locator = self.page.get_by_role(role, name=name)
            elif selector.strategy == "test_id":
                locator = self.page.locator(f"[data-testid='{selector.value}']")
            
            if locator and selector.wait_visible:
                await locator.wait_for(state="visible", timeout=selector.timeout)
            
            element = await locator.element_handle()
            
            # Try fallback if element not found
            if not element and selector.fallback:
                element = await self._find_element(selector.fallback)
            
            return element
        except:
            if selector.fallback:
                return await self._find_element(selector.fallback)
            return None

    async def _get_all_attributes(self, element: ElementHandle) -> Dict[str, str]:
        """Get all attributes of an element"""
        return await element.evaluate("""
            (element) => {
                const attrs = {};
                for (const attr of element.attributes) {
                    attrs[attr.name] = attr.value;
                }
                return attrs;
            }
        """)

    async def execute_action(self, action: BrowserAction) -> ActionResult:
        """Execute a single browser action"""
        if action.type == "navigate":
            return await self.navigate(action.value)
        
        elif action.type == "click":
            selector = ElementSelector(
                strategy=action.options.get("strategy", "css"),
                value=action.selector,
            )
            return await self.click(selector)
        
        elif action.type == "type":
            selector = ElementSelector(
                strategy=action.options.get("strategy", "css"),
                value=action.selector,
            )
            return await self.type_text(selector, action.value)
        
        elif action.type == "wait":
            await asyncio.sleep(action.value / 1000)  # Convert ms to seconds
            return ActionResult(success=True, data={"waited": action.value})
        
        elif action.type == "screenshot":
            return await self.take_screenshot(
                full_page=action.options.get("full_page", False)
            )
        
        elif action.type == "execute_js":
            return await self.execute_javascript(action.value)
        
        else:
            return ActionResult(success=False, error=f"Unknown action type: {action.type}")

    async def execute_workflow(
        self,
        actions: List[BrowserAction],
        stop_on_error: bool = True,
    ) -> List[ActionResult]:
        """Execute a sequence of browser actions"""
        results = []
        
        for action in actions:
            result = await self.execute_action(action)
            results.append(result)
            
            if not result.success and stop_on_error:
                break
        
        return results

    async def close(self) -> None:
        """Close the browser session"""
        if self.page:
            await self.page.close()
            self.page = None
        
        if self.browser:
            # Browser-use handles cleanup automatically
            self.browser = None


class SmartSelectorBuilder:
    """Build resilient selectors with multiple strategies"""
    
    @staticmethod
    def build_selector(
        element_info: Dict[str, Any],
        prefer_strategy: str = "css",
    ) -> ElementSelector:
        """Build a selector with fallback strategies"""
        selectors = []
        
        # CSS selector
        if element_info.get("id"):
            selectors.append(ElementSelector(
                strategy="css",
                value=f"#{element_info['id']}",
            ))
        
        if element_info.get("class"):
            classes = element_info["class"].split()
            selectors.append(ElementSelector(
                strategy="css",
                value=f".{'.'.join(classes)}",
            ))
        
        # Text selector
        if element_info.get("text"):
            selectors.append(ElementSelector(
                strategy="text",
                value=element_info["text"],
            ))
        
        # XPath selector
        if element_info.get("xpath"):
            selectors.append(ElementSelector(
                strategy="xpath",
                value=element_info["xpath"],
            ))
        
        # Test ID selector
        if element_info.get("data-testid"):
            selectors.append(ElementSelector(
                strategy="test_id",
                value=element_info["data-testid"],
            ))
        
        # Chain selectors as fallbacks
        if len(selectors) > 1:
            for i in range(len(selectors) - 1):
                selectors[i].fallback = selectors[i + 1]
        
        return selectors[0] if selectors else None
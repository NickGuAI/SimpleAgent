#!/usr/bin/env python3
"""Test script to verify browser-use integration"""

import asyncio
from app.core.browser_engine import BrowserAutomationEngine, BrowserAction


async def test_browser():
    print("Testing browser automation engine...")
    
    engine = BrowserAutomationEngine()
    
    try:
        # Initialize browser
        await engine.initialize()
        print("✓ Browser initialized")
        
        # Start session
        await engine.start_session()
        print("✓ Browser session started")
        
        # Navigate to a website
        result = await engine.navigate("https://example.com")
        if result.success:
            print(f"✓ Navigated to {result.data['url']}")
            print(f"  Title: {result.data['title']}")
        else:
            print(f"✗ Navigation failed: {result.error}")
        
        # Take screenshot
        screenshot_result = await engine.take_screenshot()
        if screenshot_result.success:
            print(f"✓ Screenshot saved to {screenshot_result.data['path']}")
        else:
            print(f"✗ Screenshot failed: {screenshot_result.error}")
        
        # Test action execution
        action = BrowserAction(
            type="execute_js",
            value="return document.querySelector('h1').textContent"
        )
        js_result = await engine.execute_action(action)
        if js_result.success:
            print(f"✓ JavaScript executed: {js_result.data}")
        else:
            print(f"✗ JavaScript execution failed: {js_result.error}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    finally:
        await engine.close()
        print("✓ Browser closed")


if __name__ == "__main__":
    asyncio.run(test_browser())
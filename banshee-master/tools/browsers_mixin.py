from splinter import Browser
import os
import asyncio
from pyppeteer import launch



class BrowserMixin:
    def browser(self):
        executable_path = {'executable_path': 'venders/chromedriver'}
        self.browser = Browser(os.getenv('BROWSER'),
                               headless=True, **executable_path)
        if hasattr(self, 'cookies'):
            self.browser.add_cookies(self.cookies)
        return self.browser

    async def browser_async(self):
        self.browser = await launch(
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False,
            headless=True
        )
        return self.browser


    async def page_async(self):
        await self.browser_async()
        self.page = await self.browser.newPage()
        # return self.page
        await self.page.goto('http://www.baidu.com')
        await self.browser.close()






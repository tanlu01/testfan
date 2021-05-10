import os
import requests
from bs4 import BeautifulSoup
from tools.browsers_mixin import BrowserMixin

class Page(BrowserMixin):
    def visit(self, url=None):
        if url is None:
            self.resp = requests.get(self.host + self.api, headers=self.headers)
        else:
            self.resp = requests.get(url)
        return BeautifulSoup(self.resp.content, 'html.parser')
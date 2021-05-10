from getgauge.python import step, data_store
from pages.page import Page
from pages.mt.mt_app import MtApp
from api.mt.mt import Mt
import asyncio


@step("页面检查")
def try_ui():
    mt_app = MtApp()
    mt_app.api = '//x/prime.html?is_home=1&__disable_token_cache=1&__replace=1&ref_page_name=bottom_tabbar&uid_h=478a29cedd5c0f45703b028547745945&x-feature=fund_returns%2Cprime&exp_ids=&tk=ACJapb4faIlE6Y9lVUcH9-K7djNEp2cTyHptZW5ndHVp&x_device=QUNKYXBiNGZhSWxFNlk5bFZVY0g5LUs3ZGpORXAyY1R5SHB0Wlc1bmRIVnB8OGY5MDgwMjdiZWYxNDBjZTM4Njc1NTBlMTdiMGY3YWQxYWU2ZmJmYw%3D%3D&openid=ACJapb4faIlE6Y9lVUcH9-K7djNEp2cTyHptZW5ndHVp#event.back'
    # soup = mt_app.visit('http://sx.app.mengtuiapp.com//x/prime.html?is_home=1&__disable_token_cache=1&__replace=1&ref_page_name=bottom_tabbar&uid_h=478a29cedd5c0f45703b028547745945&x-feature=fund_returns%2Cprime&exp_ids=&tk=ACJapb4faIlE6Y9lVUcH9-K7djNEp2cTyHptZW5ndHVp&x_device=QUNKYXBiNGZhSWxFNlk5bFZVY0g5LUs3ZGpORXAyY1R5SHB0Wlc1bmRIVnB8OGY5MDgwMjdiZWYxNDBjZTM4Njc1NTBlMTdiMGY3YWQxYWU2ZmJmYw%3D%3D&openid=ACJapb4faIlE6Y9lVUcH9-K7djNEp2cTyHptZW5ndHVp#event.back')
    soup = mt_app.visit()
    print(mt_app.resp)
    print(soup)


@step("初始化浏览器")
def init_browser():
    data_store.spec['browser'] = Page().browser()
    data_store.spec['browser'].visit('http://www.baidu.com')



@step("初始化萌推APP浏览器")
def init_mt_app_browser():
    mt_app = MtApp()
    data_store.spec['browser'] = mt_app.browser()



@step("关闭浏览器")
def quit_browser():
    data_store.spec['browser'].quit()


@step("try_pyppeteer")
def try_pyppeteer():
    data_store.spec['page_async'] = Page()
    asyncio.run(data_store.spec['page_async'].page_async())
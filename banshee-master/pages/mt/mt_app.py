import os
from pages.page import Page

class MtApp(Page):
    host = os.getenv('APP_PAGE_HOST')
    api = '/'
    method = 'get'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Token': '7975emeQA2KSVylZPGqF17NDIn0TJ4d6rscQKPNX3fak319k0xtuYp1j2Z9DkBb9oR_2t1NWt_rkv00Vc6Y9xhbd9iG5oO2YM_6ZtOgvxzmgjIh-e2c',
    }
import os
from dotenv import load_dotenv
load_dotenv()
load_dotenv(verbose=True)
from pathlib import Path
env_path = Path('env/default') / 'qtt.properties'
load_dotenv(dotenv_path=env_path)

from locust import HttpUser, task, tag, between, constant, events
from load_testing.mt.p0.user_loading import UserLoading
from load_testing.mt.p0.goods_loading import BaseScenario

class MtLoading(HttpUser):
    wait_time = between(1, 2)
    host = os.getenv('API_GATEWAY_HOST')
    # host = ''
    
    # tasks = {UserLoading: 1, GoodsLoading: 1}
    tasks = {BaseScenario: 1}


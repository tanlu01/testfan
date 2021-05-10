from api.account.account import Passport
import os

class Logout(Passport):
    method = 'post'
    headers = {'qtt_app_name': 'toutiao.oauth'}
    host = os.getenv('ACCOUNT_HOST')
    api = '/account/logout'
    data = {
        "token": '3b14KrmQihtt2q-ZqiM9Q5baR1gEEWwvxeIUYBdUVcGD1AiemH7KhByXtL-Jwvw6tBnY1JzbrdZlQXR7aP7g70_znochg68I2mff11ZAev_yb0T7gLw',
        "public_params": Passport.public_params
    }

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }
from datetime import datetime

class StepResult():
    def __init__(self):
        self.result = {
            "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "env": "qa",
            "url": "",
            "case_full_path": "",
            "case_name": "",
            "app": "qlive",
            "host": "http://qlive.qutoutiao.net",
            "owner": "Sam",
            "test_link_id": "",
            "from": "qute",
            "result": "Pass",
            "err_message": "",
            "duration": "0.00"
        }

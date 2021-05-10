from locust import TaskSet, task, between, constant


class DummyLoading(TaskSet):
    host = 'http://127.0.0.1:4567'
    data = {"username": "foo", "password": "bar"}

    @task
    def case_1(self):
        self.client.post(f"{self.host}/login", self.data)

    @task
    def case_2(self):
        self.client.get(f"{self.host}/hello")
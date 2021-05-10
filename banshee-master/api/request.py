import operator
import responses
import requests
from functools import wraps
from jsonschema import validate


def _validate(**expected_kwargs):
    def decorator_validate(func):
        @wraps(func)
        def wrapper_validate(self, *args, **kwargs):
            r = func(self, *args, **kwargs)
            status = r.status_code
            assert status == expected_kwargs['status'], f"status_code error: actually = {status} , expected = {expected_kwargs['status']} ."
            body = r.json()
            for key in expected_kwargs['keys']:
                if key not in body:
                    assert False, f'response_body error: {body} should include "{key}".'
            return body
        return wrapper_validate
    return decorator_validate


def _validata_schema(func):
    @wraps(func)
    def wrapper_validate(self):
        r = func(self)
        if hasattr(self, 'expected_schema'):
            validate(instance=r, schema=self.expected_schema)
        return r
    return wrapper_validate


class Request:
    @_validata_schema
    @_validate(status=200, keys=[])
    def request(self):
        self.resp = operator.methodcaller(f'_{self.method}')(self)
        return self.resp

    def _get(self):
        responses.add(responses.GET, self.host+self.api, json=self.mock_data, status=self.mock_status)
        return requests.get(self.host+self.api, headers=self.headers, params=self.data, cookies=self.cookies)

    def _post(self):
        responses.add(responses.POST, self.host+self.api, json=self.mock_data, status=self.mock_status)
        if {'Content-Type': 'application/x-www-form-urlencoded'}.items() <= self.headers.items():
            return requests.post(self.host+self.api, headers=self.headers, data=self.data, cookies=self.cookies)
        else:
            return requests.post(self.host+self.api, headers=self.headers, json=self.data, cookies=self.cookies)

    def _delete(self):
        responses.add(responses.DELETE, self.host+self.api, json=self.mock_data, status=self.mock_status)
        return requests.delete(self.host+self.api, headers=self.headers, json=self.data, cookies=self.cookies)

    def _put(self):
        responses.add(responses.PUT, self.host+self.api, json=self.mock_data, status=self.mock_status)
        return requests.put(self.host+self.api, json=self.data, headers=self.headers, cookies=self.cookies)

    @classmethod
    def loading_params(cls):
        return {'headers': cls.headers, 'api': cls.api, 'data': cls.data, 'method': cls.method}

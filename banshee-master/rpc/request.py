import os
import logging
from functools import wraps
import grpc


class Request():
    def __init__(self):
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
        self.stub = self.pb2_grpc.ServiceStub(self.channel)

    def call(self):
        try:
            self.resp = self.method(self.req)
        except grpc.RpcError as e:
            self.resp = e.details

    @classmethod
    def call_grpc(cls, func):
        @wraps(func)
        def wrapper_call(self, *args, **kwargs):
            func(self, *args, **kwargs)
            try:
                self.resp = self.meth(self.req)
            except grpc.RpcError as e:
                self.resp = e.details
            finally:
                return self.resp
        return wrapper_call

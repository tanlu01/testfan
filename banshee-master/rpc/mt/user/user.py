import os
import logging
import grpc
from rpc.mt.mt import Mt
import rpc.mt.user.user_pb2
import rpc.mt.user.user_pb2_grpc

class User(Mt):
    def __init__(self):
        # self.host = os.getenv('API_GRPC_HOST')
        self.server_port = 31101
        self.pb2 = rpc.mt.user.user_pb2
        self.pb2_grpc = rpc.mt.user.user_pb2_grpc
        super().__init__()

    # def user_by_id(self, uid):
    #     self.req = self.pb2.UserByIdArgs(uid = int(uid))
    #     self.method = lambda r: self.stub.UserById(r)
    #     self.call()
    #     return self.resp
    
    @Mt.call_grpc
    def user_by_id(self, uid):
        self.req = self.pb2.UserByIdArgs(uid = int(uid))
        self.meth = lambda r: self.stub.UserById(r)
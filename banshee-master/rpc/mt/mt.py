from rpc.request import Request
import os


class Mt(Request):
    grpc_host = os.getenv('API_GRPC_HOST')

    def __init__(self):
        self.host = Mt.grpc_host
        super().__init__()
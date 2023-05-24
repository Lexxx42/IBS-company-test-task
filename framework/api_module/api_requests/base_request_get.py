import requests
from .base_request import BaseRequest


class BaseRequestGet(BaseRequest):
    def send(self):
        self.response = requests.get(self.url + self.method_api)
        return self.response

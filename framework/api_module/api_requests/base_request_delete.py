import requests
from .base_request import BaseRequest


class BaseRequestDelete(BaseRequest):
    def send(self):
        self.response = requests.delete(self.url + self.method_api)
        return self.response

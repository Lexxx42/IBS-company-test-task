import requests
from .base_request import BaseRequest


class BaseRequestPut(BaseRequest):
    def send(self):
        self.response = requests.put(self.url + self.method_api,
                                     data=self.params)
        return self.response

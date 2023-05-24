import requests
from .base_request import BaseRequest


class BaseRequestPost(BaseRequest):
    def send(self):
        self.response = requests.post(self.url + self.method_api,
                                      data=self.params)
        return self.response

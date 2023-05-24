import requests
from .base_request import BaseRequest


class BaseRequestPatch(BaseRequest):
    def send(self):
        self.response = requests.patch(self.url + self.method_api,
                                       data=self.params)
        return self.response

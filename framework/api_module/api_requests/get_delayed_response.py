import json
import allure
from .base_request_get import BaseRequestGet


class GetDelayedResponse(BaseRequestGet):

    @allure.step('Send request with selected delay.')
    def send_request_with_selected_delay(self, request, delay: int) -> None:
        request.method_api = self.method_api + str(delay)
        request.send()

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

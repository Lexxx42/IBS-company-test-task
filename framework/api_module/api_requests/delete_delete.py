import allure
from .base_request_delete import BaseRequestDelete


class DeleteDelete(BaseRequestDelete):

    @allure.step('Send request with selected user id.')
    def send_request_with_selected_user_id(self, request, user_id: int) -> None:
        request.method_api = self.method_api + str(user_id)
        request.send()

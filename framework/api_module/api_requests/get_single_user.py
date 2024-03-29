import allure
from .base_request_get import BaseRequestGet


class GetSingleUser(BaseRequestGet):

    @allure.step('Send request with selected user id.')
    def send_request_with_selected_user_id(self, request, user_id: int) -> None:
        request.method_api = self.method_api + str(user_id)
        request.send()

    @allure.step('Check id user id in response.')
    def should_be_correct_user_id(self, user_id_request: int) -> None:
        user_id_response = self.get_response()['data']['id']
        assert user_id_request == user_id_response, \
            f'User id in request: {user_id_request},\n' \
            f' should be equal to user id in response: {user_id_response}'

    @allure.step('Check data with incorrect user id.')
    def should_not_be_data_with_id(self) -> None:
        data = self.get_response()
        number_of_data_items = len(data.items())
        assert number_of_data_items == 0, \
            f'Should be no data. But got: {data}'

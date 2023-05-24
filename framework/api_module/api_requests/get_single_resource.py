import allure
from .base_request_get import BaseRequestGet


class GetSingleResource(BaseRequestGet):

    @allure.step('Send request with selected resource id.')
    def send_request_with_selected_resource_id(self, request, resource_id: int) -> None:
        request.method_api = self.method_api + str(resource_id)
        request.send()

    @allure.step('Check resource id in response.')
    def should_be_correct_resource_id(self, resource_id_request: int) -> None:
        resource_id_response = self.response.json()['data']['id']
        assert resource_id_request == resource_id_response, \
            f'Id in request: {resource_id_request=},\n' \
            f' should be equal to: {resource_id_response=}'

    @allure.step('Check data with incorrect user id.')
    def should_not_be_data_with_id(self) -> None:
        data = self.response.json()
        number_of_data_items = len(data.items())
        assert number_of_data_items == 0, \
            f'Should be no data. But got: {data}'

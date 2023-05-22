"""This module represents main page object."""
import json
import allure
from .base_page import BasePage
from ..web_locators import MainPageLocators
from .. import TestGetListUsersMethod


class MainPage(BasePage):
    """Main page object."""
    locators = MainPageLocators()



    @allure.step('Check api list_users equal to ui call.')
    def check_correct_list_users_request(self) -> None:
        with allure.step('Click on list_users button'):
            list_users_button = self.element_is_clickable(self.locators.GET_LIST_USERS_BUTTON)
            list_users_button.click()
        with allure.step('Get api response'):
            body_from_api = TestGetListUsersMethod.get_received_response_body_for_ui()
        with allure.step('Get ui response'):
            body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
            body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

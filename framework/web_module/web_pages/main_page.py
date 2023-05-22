"""This module represents main page object."""
from .base_page import BasePage
from ..web_locators import MainPageLocators


class MainPage(BasePage):
    """Main page object."""
    locators = MainPageLocators()

    def check_correct_list_users_request(self):
        list_users_button = self.element_is_clickable(self.locators.GET_LIST_USERS_BUTTON)
        list_users_button.click()
        


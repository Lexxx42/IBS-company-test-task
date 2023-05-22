"""
Module contains tests for Main page of the site.
"""
import allure
import pytest
from ..web_pages import MainPage


@allure.suite('Main page')
class TestMainPage:
    """Class represents Main page.
    Features:
    !!!!!!!!
    """

    @allure.feature('List Users request')
    class TestListUsers:
        """Class represents List Users request tests."""
        main_page_link = 'https://reqres.in/'

        @allure.title('List Users request shows correct result in main page.')
        def test_list_users_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_correct_list_users_request()

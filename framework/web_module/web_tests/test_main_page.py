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
    TestGeneralUI,
    TestListUsers
    """

    @allure.feature('List Users request')
    class TestGeneralUI:
        """Class represents GeneralUI tests."""
        main_page_link = 'https://reqres.in/'

        @allure.title('Current URL must be correct.')
        def test_url_of_main_page(self, driver):
            """Test URL must be correct."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_url_of_main_page()

        @allure.title('Main page must have correct title.')
        def test_title_of_main_page(self, driver):
            """Test Title must be correct."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_title_of_main_page()

        @allure.title('Main page must have correct logo.')
        def test_logo_of_main_page(self, driver):
            """Test logo must be correct."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_logo_of_main_page()

        @allure.title('Main page must have correct h2 texts.')
        def test_h2_texts_of_main_page(self, driver):
            """Test h2_texts must be correct."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_h2_texts_of_main_page()

        @allure.title('Main page must have correct h3 titles.')
        def test_h3_titles_of_main_page(self, driver):
            """Test h3 titles must be correct."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_h3_titles_of_main_page()

        @allure.title('Support button is clickable.')
        def test_support_button_is_clickable(self, driver):
            """Test support button on main page."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_support_button_main_page()

        @allure.title('Main page must have correct h3 texts.')
        def test_h3_texts_of_main_page(self, driver):
            """Test h3 texts must be correct."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_h3_texts_of_main_page()

    @allure.feature('List Users request')
    class TestListUsers:
        """Class represents List Users request tests."""
        main_page_link = 'https://reqres.in/'

        @allure.title('List Users request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_ui_status_code_output_list_users()

        @allure.title('List Users request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_request_url_output_list_users()

        @allure.title('List Users request shows correct result in main page.')
        def test_list_users_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_request_ui_output_list_users()

    @allure.feature('Single User request')
    class TestSingleUser:
        """Class represents Single User request tests."""
        main_page_link = 'https://reqres.in/'

        @allure.title('Single User request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_ui_status_code_output_single_user()

        @allure.title('Single User request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_request_url_output_single_user()

        @allure.title('Single User request shows correct result in main page.')
        def test_list_users_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_request_ui_output_single_user()

    @allure.feature('Single User request')
    class TestSingleUserNotFound:
        """Class represents SingleUserNotFound request tests."""
        main_page_link = 'https://reqres.in/'

        @allure.title('SingleUserNotFound request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_ui_status_code_output_single_user_not_found()

        @allure.title('SingleUserNotFound request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_request_url_output_single_user_not_found()

        @allure.title('SingleUserNotFound request shows correct result in main page.')
        def test_list_users_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, self.main_page_link)
            main_page.open()
            main_page.check_request_ui_output_single_user_not_found()

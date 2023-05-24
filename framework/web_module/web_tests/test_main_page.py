"""
Module contains tests for Main page of the site.
"""
import allure
import pytest
from ..web_pages import MainPage

MAIN_PAGE_LINK = 'https://reqres.in/'


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

        @allure.title('Current URL must be correct.')
        def test_url_of_main_page(self, driver):
            """Test URL must be correct."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_url_of_main_page()

        @allure.title('Main page must have correct title.')
        def test_title_of_main_page(self, driver):
            """Test Title must be correct."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_title_of_main_page()

        @allure.title('Main page must have correct logo.')
        def test_logo_of_main_page(self, driver):
            """Test logo must be correct."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_logo_of_main_page()

        @allure.title('Main page must have correct h2 texts.')
        def test_h2_texts_of_main_page(self, driver):
            """Test h2_texts must be correct."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_h2_texts_of_main_page()

        @allure.title('Main page must have correct h3 titles.')
        def test_h3_titles_of_main_page(self, driver):
            """Test h3 titles must be correct."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_h3_titles_of_main_page()

        @allure.title('Support button is clickable.')
        def test_support_button_is_clickable(self, driver):
            """Test support button on main page."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_support_button_main_page()

        @allure.title('Main page must have correct h3 texts.')
        def test_h3_texts_of_main_page(self, driver):
            """Test h3 texts must be correct."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_h3_texts_of_main_page()

    @allure.feature('List Users request')
    class TestListUsers:
        """Class represents List Users request tests."""

        @allure.title('List Users request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_list_users()

        @allure.title('List Users request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_list_users()

        @allure.title('List Users request shows correct result in main page.')
        def test_list_users_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_list_users()

    @allure.feature('Single User request')
    class TestSingleUser:
        """Class represents Single User request tests."""

        @allure.title('Single User request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_single_user()

        @allure.title('Single User request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_single_user()

        @allure.title('Single User request shows correct result in main page.')
        def test_list_users_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_single_user()

    @allure.feature('Single User request')
    class TestSingleUserNotFound:
        """Class represents SingleUserNotFound request tests."""

        @allure.title('SingleUserNotFound request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_single_user_not_found()

        @allure.title('SingleUserNotFound request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_single_user_not_found()

        @allure.title('SingleUserNotFound request shows correct result in main page.')
        def test_list_users_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_single_user_not_found()

    @allure.feature('List Resource request')
    class TestListResource:
        """Class represents ListResource request tests."""

        @allure.title('ListResource request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_list_resource()

        @allure.title('ListResource request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_list_resource()

        @allure.title('ListResource request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_list_resource()

    @allure.feature('Single Resource request')
    class TestSingleResource:
        """Class represents SingleResource request tests."""

        @allure.title('SingleResource request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_single_resource()

        @allure.title('SingleResource request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_single_resource()

        @allure.title('SingleResource request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_single_resource()

    @allure.feature('Single Resource Not Found request')
    class TestSingleResource:
        """Class represents SingleResourceNotFound request tests."""

        @allure.title('SingleResourceNotFound request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_single_resource_not_found()

        @allure.title('SingleResourceNotFound request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_single_resource_not_found()

        @allure.title('SingleResourceNotFound request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_single_resource_not_found()

    @allure.feature('DelayedResponse request')
    class TestDelayedResponse:
        """Class represents SingleResourceNotFound request tests."""

        @allure.title('DelayedResponse response comes after delay.')
        @pytest.mark.parametrize('delay', range(1, 4))
        def test_delayed_response(self, driver, delay: int) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_delay(delay_from_api=delay)

        @allure.title('DelayedResponse request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_delayed_response()

        @allure.title('DelayedResponse request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_delayed_response()

        @allure.title('DelayedResponse request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_delayed_response()

    @allure.feature('PostCreate request')
    class TestSingleResource:
        """Class represents PostCreate request tests."""

        @allure.title('PostCreate request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_post_create()

        @allure.title('PostCreate request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_post_create()

        @allure.title('PostCreate request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_post_create()

    @allure.feature('RegisterSuccessful request')
    class TestRegisterSuccessful:
        """Class represents RegisterSuccessful request tests."""

        @allure.title('RegisterSuccessful request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_register_successful()

        @allure.title('RegisterSuccessful request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_register_successful()

        @allure.title('RegisterSuccessful request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_register_successful()

    @allure.feature('RegisterUnsuccessful request')
    class TestRegisterUnsuccessful:
        """Class represents RegisterUnsuccessful request tests."""

        @allure.title('RegisterUnsuccessful request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_register_unsuccessful()

        @allure.title('RegisterUnsuccessful request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_register_unsuccessful()

        @allure.title('RegisterUnsuccessful request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_register_unsuccessful()

    @allure.feature('LoginSuccessful request')
    class TestLoginSuccessful:
        """Class represents LoginSuccessful request tests."""

        @allure.title('LoginSuccessful request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_login_successful()

        @allure.title('LoginSuccessful request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_login_successful()

        @allure.title('LoginSuccessful request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_login_successful()

    @allure.feature('LoginUnsuccessful request')
    class TestLoginSuccessful:
        """Class represents LoginUnsuccessful request tests."""

        @allure.title('LoginUnsuccessful request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_login_unsuccessful()

        @allure.title('LoginUnsuccessful request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_login_unsuccessful()

        @allure.title('LoginUnsuccessful request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_login_unsuccessful()

    @allure.feature('PutUpdate request')
    class TestPutUpdate:
        """Class represents PutUpdate request tests."""

        @allure.title('PutUpdate request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_put_update()

        @allure.title('PutUpdate request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_put_update()

        @allure.title('PutUpdate request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_put_update()

    @allure.feature('PatchUpdate request')
    class TestPatchUpdate:
        """Class represents PatchUpdate request tests."""

        @allure.title('PatchUpdate request shows correct status code in main page.')
        def test_status_code_ui_output(self, driver) -> None:
            """Test user can view status code of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_ui_status_code_output_patch_update()

        @allure.title('PatchUpdate request shows correct request URL in main page.')
        def test_request_url_ui_output(self, driver) -> None:
            """Test user can view request url of API call."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_url_output_patch_update()

        @allure.title('PatchUpdate request shows correct result in main page.')
        def test_request_shows_correct_result(self, driver) -> None:
            """Test user can fill the form and sent it."""
            main_page = MainPage(driver, MAIN_PAGE_LINK)
            main_page.open()
            main_page.check_request_ui_output_patch_update()

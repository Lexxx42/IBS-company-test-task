"""This module represents main page object."""
import json
from time import perf_counter as timer
import allure
import requests
from .base_page import BasePage
from ..web_locators import MainPageLocators
from .. import get_received_response_body_for_ui_list_users, get_request_url_for_ui_list_users, \
    get_received_response_body_for_ui_single_user, get_request_url_for_ui_single_user, \
    get_request_url_for_ui_single_user_not_found, get_request_url_for_ui_list_resource, \
    get_received_response_body_for_ui_list_resource, get_request_url_for_ui_single_resource, \
    get_received_response_body_for_ui_single_resource, get_received_response_body_for_ui_delayed_response, \
    get_request_url_for_ui_delayed_response


class MainPage(BasePage):
    """Main page object."""
    locators = MainPageLocators()

    @allure.step('Check url of main page.')
    def check_url_of_main_page(self):
        expected_url = 'https://reqres.in/'
        actual_url = self.get_current_url()
        assert expected_url == actual_url, \
            f'Expected {actual_url=} to be {expected_url=}'

    @allure.step('Check title of main page.')
    def check_title_of_main_page(self):
        expected_title = 'Reqres - A hosted REST-API ready to respond to your AJAX requests'
        actual_title = self.get_page_title()
        assert expected_title == actual_title, \
            f'Expected {expected_title=} to be {actual_title=}'

    @allure.step('Check logo of main page.')
    def check_logo_of_main_page(self):
        logo_element = self.element_is_visible(self.locators.LOGO)
        with allure.step('Get image link from src attribute'):
            logo_source = logo_element.get_attribute('src')
        with allure.step(f'Get request with {logo_source=}'):
            request = requests.get(logo_source, timeout=5)
        with allure.step('Get image content type'):
            content_type = request.headers.get('content-type')
        assert request.status_code == 200, \
            f'Expected {request.status_code} with {logo_source=} to be 200'
        assert content_type == 'image/png', \
            f'Invalid content {content_type}, image/png expected'

    @allure.step('Check h2 texts of main page.')
    def check_h2_texts_of_main_page(self):
        first_h2 = self.element_is_visible(self.locators.FIRST_H2)
        first_h2_text = first_h2.text
        second_h2 = self.element_is_visible(self.locators.SECOND_H2)
        second_h2_text = second_h2.text
        first_h2_expected = 'Test your front-end against a real API'
        second_h2_expected = 'A hosted REST-API ready to respond to your AJAX requests.'
        assert first_h2_text == first_h2_expected, \
            f'Expected {first_h2_text=} to be equal {first_h2_expected=}'
        assert second_h2_text == second_h2_expected, \
            f'Expected {second_h2_text=} to be equal {second_h2_expected=}'

    @allure.step('Check h3 titles of main page.')
    def check_h3_titles_of_main_page(self):
        h3_titles = self.elements_are_visible(self.locators.H3_TITLES)
        actual_titles = []
        for title in h3_titles:
            self.go_to_element(title)
            actual_titles.append(title.text)
        expected_titles = ['Fake data', 'Real responses', 'Always-on']
        assert expected_titles == actual_titles, \
            f'Expected titles to be: {expected_titles}\n' \
            f'Got: {actual_titles}'

    @allure.step('Check h3 texts of main page.')
    def check_h3_texts_of_main_page(self):
        h3_paragraphs = self.elements_are_visible(self.locators.H3_PARAGRAPHS)
        actual_texts = []
        for paragraph in h3_paragraphs:
            self.go_to_element(paragraph)
            actual_texts.append(paragraph.text)
        expected_texts = [
            'No more tedious sample data creation, we\'ve got it covered.',
            'Develop with real response codes. GET, POST, PUT & DELETE supported.',
            '24/7 free access in your development phases. Go nuts.'
        ]
        assert expected_texts == actual_texts, \
            f'Expected titles to be: {expected_texts}\n' \
            f'Got: {actual_texts}'

    @allure.step('Check support button on main page.')
    def check_support_button_main_page(self):
        support_button = self.element_is_clickable(self.locators.SUPPORT_BUTTON)
        support_button.click()
        one_time_payment_field = self.element_is_visible(self.locators.ONE_TIME_PAYMENT)
        one_time_payment_field_placeholder = one_time_payment_field.get_attribute('placeholder')
        placeholder_expected = '$10'
        assert one_time_payment_field_placeholder == placeholder_expected, \
            f'Expected {one_time_payment_field_placeholder=} to be equal to \n' \
            f'{placeholder_expected=}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_list_users(self):
        response_status_code_output = 0
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        list_users_button = self.element_is_clickable(self.locators.GET_LIST_USERS_BUTTON)
        list_users_button.click()
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
            response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
            response_status_code_output = response_status_code.text
        status_code_expected = 200
        assert response_status_code_output == str(status_code_expected), \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_list_users(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_users_button = self.element_is_clickable(self.locators.GET_LIST_USERS_BUTTON)
            list_users_button.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = get_request_url_for_ui_list_users()
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api list_users equal to ui call.')
    def check_request_ui_output_list_users(self) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_users_button = self.element_is_clickable(self.locators.GET_LIST_USERS_BUTTON)
            list_users_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_list_users()
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_user(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        response_status_code_output = 0
        single_user_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_BUTTON)
        single_user_button.click()
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
            response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
            response_status_code_output = response_status_code.text
        status_code_expected = 200
        assert response_status_code_output == str(status_code_expected), \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_user(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            single_user_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_BUTTON)
            single_user_button.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = get_request_url_for_ui_single_user()
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_single_user(self) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            single_user_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_BUTTON)
            single_user_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_single_user()
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_user_not_found(self):
        response_status_code_output = 0
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        single_user_not_found_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_NOT_FOUND_BUTTON)
        single_user_not_found_button.click()
        response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
            response_status_code_output = response_status_code.text
        status_code_expected = 404
        assert response_status_code_output == str(status_code_expected), \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_user_not_found(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            single_user_not_found_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_NOT_FOUND_BUTTON)
            single_user_not_found_button.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = get_request_url_for_ui_single_user_not_found()
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_single_user_not_found(self) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            single_user_not_found_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_NOT_FOUND_BUTTON)
            single_user_not_found_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_single_user(search_type='not found')
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_list_resource(self):
        response_status_code_output = 0
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        list_resource_button = self.element_is_clickable(self.locators.GET_LIST_RESOURCE_BUTTON)
        list_resource_button.click()
        response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
            response_status_code_output = response_status_code.text
        status_code_expected = 200
        assert response_status_code_output == str(status_code_expected), \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_list_resource(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_resource_button = self.element_is_clickable(self.locators.GET_LIST_RESOURCE_BUTTON)
            list_resource_button.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = get_request_url_for_ui_list_resource()
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_list_resource(self) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_resource_button = self.element_is_clickable(self.locators.GET_LIST_RESOURCE_BUTTON)
            list_resource_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_list_resource(search_type='unknown')
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_resource(self):
        response_status_code_output = 0
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        list_resource_button = self.element_is_clickable(self.locators.GET_SINGLE_RESOURCE_BUTTON)
        list_resource_button.click()
        response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
            response_status_code_output = response_status_code.text
        status_code_expected = 200
        assert response_status_code_output == str(status_code_expected), \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_resource(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_resource_button = self.element_is_clickable(self.locators.GET_SINGLE_RESOURCE_BUTTON)
            list_resource_button.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = get_request_url_for_ui_single_resource()
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_single_resource(self) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_resource_button = self.element_is_clickable(self.locators.GET_SINGLE_RESOURCE_BUTTON)
            list_resource_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_single_resource(search_type='found')
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_resource_not_found(self):
        response_status_code_output = 0
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        list_resource_not_found_button = self.element_is_clickable(
            self.locators.GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON)
        list_resource_not_found_button.click()
        response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
            response_status_code_output = response_status_code.text
        status_code_expected = 404
        assert response_status_code_output == str(status_code_expected), \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_resource_not_found(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_resource_not_found_button = self.element_is_clickable(
                self.locators.GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON)
            list_resource_not_found_button.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = get_request_url_for_ui_single_resource(search_type='not found')
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_single_resource_not_found(self) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            list_resource_not_found_button = self.element_is_clickable(
                self.locators.GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON)
            list_resource_not_found_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_single_resource(search_type='not found')
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check if response got after delay.')
    def check_delay(self, delay_from_api: int) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            delayed_response_button = self.element_is_clickable(
                self.locators.GET_DELAYED_RESPONSE_BUTTON)
            timer_start = timer()
            delayed_response_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_delayed_response(delay_from_api)
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                timer_stop = timer()
                body_from_page = json.loads(body_from_page_text)
        time_when_got_response = timer_stop - timer_start
        assert time_when_got_response >= delay_from_api, \
            f'Time delay: {time_when_got_response=},\n' \
            f' should be greater than response delay: {delay_from_api=}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_delayed_response(self):
        response_status_code_output = 0
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        delayed_response_button = self.element_is_clickable(
            self.locators.GET_DELAYED_RESPONSE_BUTTON)
        delayed_response_button.click()
        response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
            response_status_code_output = response_status_code.text
        status_code_expected = 200
        assert response_status_code_output == str(status_code_expected), \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_delayed_response(self):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            delayed_response_button = self.element_is_clickable(
                self.locators.GET_DELAYED_RESPONSE_BUTTON)
            delayed_response_button.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = get_request_url_for_ui_delayed_response()
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_delayed_response(self) -> None:
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on list_users button'):
            delayed_response_button = self.element_is_clickable(
                self.locators.GET_DELAYED_RESPONSE_BUTTON)
            delayed_response_button.click()
        with allure.step('Get api response'):
            body_from_api = get_received_response_body_for_ui_delayed_response()
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text):
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

"""This module represents main page object."""
import json
from time import perf_counter as timer
import allure
import requests
from requests.exceptions import JSONDecodeError
from .base_page import BasePage
from ..web_locators import MainPageLocators
from .. import get_received_response_body_for_ui_list_users, get_request_url_for_ui_list_users, \
    get_received_response_body_for_ui_single_user, get_request_url_for_ui_single_user, \
    get_request_url_for_ui_single_user_not_found, get_request_url_for_ui_list_resource, \
    get_received_response_body_for_ui_list_resource, get_request_url_for_ui_single_resource, \
    get_received_response_body_for_ui_single_resource, get_received_response_body_for_ui_delayed_response, \
    get_request_url_for_ui_delayed_response, get_request_url_for_ui_post_create, \
    get_received_response_body_for_ui_post_create, \
    get_received_response_body_for_ui_register_successful, get_request_url_for_ui_register_successful, \
    get_request_url_for_ui_login_successful, get_received_response_body_for_ui_login_successful, \
    get_received_response_body_for_ui_put_update, get_request_url_for_ui_put_update, \
    get_received_response_body_for_ui_patch_update, get_request_url_for_ui_patch_update, \
    get_received_response_body_for_ui_delete_delete, get_request_url_for_ui_delete_delete, \
    get_received_response_body_for_ui_single_resource_not_found, get_request_url_for_ui_single_resource_not_found, \
    get_received_response_body_for_ui_login_unsuccessful, get_received_response_body_for_ui_register_unsuccessful


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

    @allure.step('Get selected data from page')
    def get_data_from_output_request(self, *args: str) -> dict[str]:
        try:
            output_request = self.element_is_visible(self.locators.OUTPUT_REQUEST)
            output_request_text = output_request.text
            data_from_output = json.loads(output_request_text)
        except JSONDecodeError:
            return {}
        data_from_page = {}
        for arg in args:
            data_from_page[arg] = data_from_output[arg]
        return data_from_page

    @allure.step('Get response body from api and page.')
    def get_api_and_ui_response_body(
            self, button_to_click, extraction_method, *args, full_body=False, is_list_users=False):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on button'):
            button_to_click.click()
        with allure.step('Get api response'):
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text) and not is_list_users:
                if full_body is True:
                    body_from_api = extraction_method()
                else:
                    data = self.get_data_from_output_request(*args)
                    body_from_api = extraction_method(*tuple(data.values()))
            else:
                body_from_api = extraction_method()
        with allure.step('Get ui response'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text) and not is_list_users:
                if full_body is True:
                    body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                    try:
                        body_from_page = json.loads(body_from_page_text)
                    except Exception:
                        body_from_page = None
                else:
                    body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                    body_from_page = json.loads(body_from_page_text)
            else:
                body_from_page_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
                body_from_page = json.loads(body_from_page_text)
        with allure.step('Return api and ui responses'):
            return body_from_api, body_from_page

    @allure.step('Get status code from page.')
    def get_status_code(self, element_of_button_to_press, is_list_users=False) -> str:
        response_status_code_output = ''
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        element_of_button_to_press.click()
        response_status_code = self.element_is_visible(self.locators.RESPONSE_STATUS_CODE)
        self.element_is_visible(self.locators.RESPONSE_OUTPUT)
        if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text) and not is_list_users:
            response_status_code_output = response_status_code.text
        else:
            response_status_code_output = response_status_code.text
        return response_status_code_output

    @allure.step('Get request methods from api and page.')
    def get_request_methods_from_api_and_ui(self, button_to_click, ui_extraction_method, is_list_users=False):
        initial_text = self.element_is_visible(self.locators.RESPONSE_OUTPUT).text
        with allure.step('Click on button'):
            button_to_click.click()
        with allure.step('Get request URL from ui'):
            self.element_is_visible(self.locators.RESPONSE_OUTPUT)
            if self.is_element_changed_output_text(self.locators.RESPONSE_OUTPUT, initial_text) and not is_list_users:
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = ui_extraction_method()
            else:
                ui_request_url = self.element_is_visible(self.locators.REQUEST_URL)
                ui_request_method = ui_request_url.text
                api_request_method = ui_extraction_method()
        return ui_request_method, api_request_method

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_list_users(self):
        list_users_button = self.element_is_clickable(self.locators.GET_LIST_USERS_BUTTON)
        response_status_code_output = self.get_status_code(list_users_button, is_list_users=True)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_list_users(self):
        list_users_button = self.element_is_clickable(
            self.locators.GET_LIST_USERS_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(list_users_button,
                                                     get_request_url_for_ui_list_users,
                                                     is_list_users=True)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api list_users equal to ui call.')
    def check_request_ui_output_list_users(self) -> None:
        list_users_button = self.element_is_clickable(
            self.locators.GET_LIST_USERS_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(
            list_users_button,
            get_received_response_body_for_ui_list_users,
            full_body=True,
            is_list_users=True)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_user(self):
        single_user_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_BUTTON)
        response_status_code_output = self.get_status_code(single_user_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_user(self):
        single_user_button = self.element_is_clickable(
            self.locators.GET_SINGLE_USER_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(single_user_button,
                                                     get_request_url_for_ui_single_user)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_single_user(self) -> None:
        single_user_button = self.element_is_clickable(
            self.locators.GET_SINGLE_USER_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(
            single_user_button,
            get_received_response_body_for_ui_single_user,
            full_body=True)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_user_not_found(self):
        single_user_not_found_button = self.element_is_clickable(self.locators.GET_SINGLE_USER_NOT_FOUND_BUTTON)
        response_status_code_output = self.get_status_code(single_user_not_found_button)
        status_code_expected = '404'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_user_not_found(self):
        single_user_not_found_button = self.element_is_clickable(
            self.locators.GET_SINGLE_USER_NOT_FOUND_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(single_user_not_found_button,
                                                     get_request_url_for_ui_single_user_not_found)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_single_user_not_found(self) -> None:
        single_user_not_found_button = self.element_is_clickable(
            self.locators.GET_SINGLE_USER_NOT_FOUND_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(
            single_user_not_found_button,
            get_request_url_for_ui_single_user_not_found,
            full_body=True)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_list_resource(self):
        list_resource_button = self.element_is_clickable(self.locators.GET_LIST_RESOURCE_BUTTON)
        response_status_code_output = self.get_status_code(list_resource_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_list_resource(self):
        list_resource_button = self.element_is_clickable(
            self.locators.GET_LIST_RESOURCE_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(list_resource_button,
                                                     get_request_url_for_ui_list_resource)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_list_resource(self) -> None:
        list_resource_button = self.element_is_clickable(
            self.locators.GET_LIST_RESOURCE_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(
            list_resource_button,
            get_received_response_body_for_ui_list_resource,
            full_body=True)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_resource(self):
        single_resource_button = self.element_is_clickable(self.locators.GET_SINGLE_RESOURCE_BUTTON)
        response_status_code_output = self.get_status_code(single_resource_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_resource(self):
        single_resource_button = self.element_is_clickable(
            self.locators.GET_SINGLE_RESOURCE_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(single_resource_button,
                                                     get_request_url_for_ui_single_resource)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api single_user equal to ui call.')
    def check_request_ui_output_single_resource(self) -> None:
        single_resource_button = self.element_is_clickable(
            self.locators.GET_SINGLE_RESOURCE_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(
            single_resource_button,
            get_received_response_body_for_ui_single_resource,
            full_body=True)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_single_resource_not_found(self):
        single_resource_not_found = self.element_is_clickable(
            self.locators.GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON)
        response_status_code_output = self.get_status_code(single_resource_not_found)
        status_code_expected = '404'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_single_resource_not_found(self):
        single_resource_not_found = self.element_is_clickable(
            self.locators.GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(single_resource_not_found,
                                                     get_request_url_for_ui_single_resource_not_found)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_single_resource_not_found(self) -> None:
        single_resource_not_found = self.element_is_clickable(
            self.locators.GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(
            single_resource_not_found,
            get_received_response_body_for_ui_single_resource_not_found,
            full_body=True)
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
        delayed_response_button = self.element_is_clickable(
            self.locators.GET_DELAYED_RESPONSE_BUTTON)
        response_status_code_output = self.get_status_code(delayed_response_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_delayed_response(self):
        delayed_response_button = self.element_is_clickable(
            self.locators.GET_DELAYED_RESPONSE_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(delayed_response_button, get_request_url_for_ui_delayed_response)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_delayed_response(self) -> None:
        delayed_response_button = self.element_is_clickable(
            self.locators.GET_DELAYED_RESPONSE_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(
            delayed_response_button,
            get_received_response_body_for_ui_delayed_response,
            full_body=True)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_post_create(self):
        post_create_button = self.element_is_clickable(
            self.locators.POST_CREATE_BUTTON)
        response_status_code_output = self.get_status_code(post_create_button)
        status_code_expected = '201'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_post_create(self):
        post_create_button = self.element_is_clickable(
            self.locators.POST_CREATE_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(post_create_button, get_request_url_for_ui_post_create)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_post_create(self) -> None:
        post_create_button = self.element_is_clickable(
            self.locators.POST_CREATE_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(post_create_button,
                                                                          get_received_response_body_for_ui_post_create,
                                                                          'name', 'job', full_body=False)
        api_response_name = body_from_api['name']
        api_response_job = body_from_api['job']
        api_response_id = body_from_api['id']
        page_response_name = body_from_page['name']
        page_response_job = body_from_page['job']
        page_response_id = body_from_page['id']
        assert api_response_name == page_response_name, \
            f'Expected {api_response_name=} to be equal {page_response_name=}'
        assert api_response_job == page_response_job, \
            f'Expected {api_response_job=} to be equal {page_response_job=}'
        assert api_response_id == page_response_id, \
            f'Expected {api_response_id=} to be equal {page_response_id=}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_register_successful(self):
        register_successful_button = self.element_is_clickable(
            self.locators.REGISTER_SUCCESSFUL_BUTTON)
        response_status_code_output = self.get_status_code(register_successful_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_register_successful(self):
        register_successful_button = self.element_is_clickable(
            self.locators.REGISTER_SUCCESSFUL_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(register_successful_button,
                                                     get_request_url_for_ui_register_successful)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_register_successful(self) -> None:
        register_successful_button = self.element_is_clickable(
            self.locators.REGISTER_SUCCESSFUL_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(register_successful_button,
                                                                          get_received_response_body_for_ui_register_successful,
                                                                          'email', 'password', full_body=False)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_register_unsuccessful(self):
        register_unsuccessful_button = self.element_is_clickable(
            self.locators.REGISTER_UNSUCCESSFUL_BUTTON)
        response_status_code_output = self.get_status_code(register_unsuccessful_button)
        status_code_expected = '400'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_register_unsuccessful(self):
        register_unsuccessful_button = self.element_is_clickable(
            self.locators.REGISTER_UNSUCCESSFUL_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(register_unsuccessful_button,
                                                     get_request_url_for_ui_register_successful)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_register_unsuccessful(self) -> None:
        register_unsuccessful_button = self.element_is_clickable(
            self.locators.REGISTER_UNSUCCESSFUL_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(register_unsuccessful_button,
                                                                          get_received_response_body_for_ui_register_unsuccessful,
                                                                          'email', full_body=False)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_login_successful(self):
        login_successful_button = self.element_is_clickable(
            self.locators.LOGIN_SUCCESSFUL_BUTTON)
        response_status_code_output = self.get_status_code(login_successful_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_login_successful(self):
        login_successful_button = self.element_is_clickable(
            self.locators.LOGIN_SUCCESSFUL_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(login_successful_button, get_request_url_for_ui_login_successful)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_login_successful(self) -> None:
        login_successful_button = self.element_is_clickable(
            self.locators.LOGIN_SUCCESSFUL_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(login_successful_button,
                                                                          get_received_response_body_for_ui_login_successful,
                                                                          'email', 'password', full_body=False)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_login_unsuccessful(self):
        login_unsuccessful_button = self.element_is_clickable(
            self.locators.LOGIN_UNSUCCESSFUL_BUTTON)
        response_status_code_output = self.get_status_code(login_unsuccessful_button)
        status_code_expected = '400'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_login_unsuccessful(self):
        login_unsuccessful_button = self.element_is_clickable(
            self.locators.LOGIN_UNSUCCESSFUL_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(login_unsuccessful_button, get_request_url_for_ui_login_successful)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_login_unsuccessful(self) -> None:
        login_unsuccessful_button = self.element_is_clickable(
            self.locators.LOGIN_UNSUCCESSFUL_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(login_unsuccessful_button,
                                                                          get_received_response_body_for_ui_login_unsuccessful,
                                                                          'email',
                                                                          full_body=False)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_put_update(self):
        put_update_button = self.element_is_clickable(
            self.locators.PUT_UPDATE_BUTTON)
        response_status_code_output = self.get_status_code(put_update_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_put_update(self):
        put_update_button = self.element_is_clickable(
            self.locators.PUT_UPDATE_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(put_update_button, get_request_url_for_ui_put_update)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_put_update(self) -> None:
        put_update_button = self.element_is_clickable(
            self.locators.PUT_UPDATE_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(put_update_button,
                                                                          get_received_response_body_for_ui_put_update,
                                                                          'name', 'job',
                                                                          full_body=False)
        api_response_name = body_from_api['name']
        api_response_job = body_from_api['job']
        page_response_name = body_from_page['name']
        page_response_job = body_from_page['job']
        assert api_response_name == page_response_name, \
            f'Expected {api_response_name=} to be equal {page_response_name=}'
        assert api_response_job == page_response_job, \
            f'Expected {api_response_job=} to be equal {page_response_job=}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_patch_update(self):
        patch_update_button = self.element_is_clickable(
            self.locators.PATCH_UPDATE_BUTTON)
        response_status_code_output = self.get_status_code(patch_update_button)
        status_code_expected = '200'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_patch_update(self):
        patch_update_button = self.element_is_clickable(
            self.locators.PATCH_UPDATE_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(patch_update_button, get_request_url_for_ui_patch_update)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_patch_update(self) -> None:
        patch_update_button = self.element_is_clickable(
            self.locators.PATCH_UPDATE_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(patch_update_button,
                                                                          get_received_response_body_for_ui_patch_update,
                                                                          'name', 'job',
                                                                          full_body=False)
        api_response_name = body_from_api['name']
        api_response_job = body_from_api['job']
        page_response_name = body_from_page['name']
        page_response_job = body_from_page['job']
        assert api_response_name == page_response_name, \
            f'Expected {api_response_name=} to be equal {page_response_name=}'
        assert api_response_job == page_response_job, \
            f'Expected {api_response_job=} to be equal {page_response_job=}'

    @allure.step('Check api output status code.')
    def check_ui_status_code_output_delete_delete(self):
        delete_button = self.element_is_clickable(
            self.locators.DELETE_BUTTON)
        response_status_code_output = self.get_status_code(delete_button)
        status_code_expected = '204'
        assert response_status_code_output == status_code_expected, \
            f'Expected {response_status_code_output} to be {status_code_expected}'

    @allure.step('Check request url in UI.')
    def check_request_url_output_delete_delete(self):
        delete_button = self.element_is_clickable(
            self.locators.DELETE_BUTTON)
        ui_request_method, api_request_method = \
            self.get_request_methods_from_api_and_ui(delete_button, get_request_url_for_ui_delete_delete)
        assert ui_request_method == api_request_method, \
            f'Expected request method: {api_request_method}' \
            f'\n to be equal to request method on the main page: {ui_request_method}'

    @allure.step('Check api method equal to ui call.')
    def check_request_ui_output_delete_delete(self) -> None:
        delete_button = self.element_is_clickable(
            self.locators.DELETE_BUTTON)
        body_from_api, body_from_page = self.get_api_and_ui_response_body(delete_button,
                                                                          get_received_response_body_for_ui_delete_delete,
                                                                          full_body=True)
        assert body_from_api == body_from_page, \
            f'Expected response body from api: {body_from_api}' \
            f'\n to be equal to response on the main page: {body_from_page}'

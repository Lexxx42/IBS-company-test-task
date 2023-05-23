"""
This module contains locators for Main page of the site.
"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Class for Main page locators."""
    # Main page
    LOGO = (By.XPATH, '//h1/a/img')
    FIRST_H2 = (By.CSS_SELECTOR, 'h2.tagline:nth-child(1)')
    SECOND_H2 = (By.XPATH, '//main[@class="the-sell"]//h2[2]')
    H3_TITLES = (By.CSS_SELECTOR, '.v-center h3')
    H3_PARAGRAPHS = (By.CSS_SELECTOR, '.v-center p')
    SUPPORT_BUTTON = (By.CSS_SELECTOR, 'button a')

    # Support page
    ONE_TIME_PAYMENT = (By.XPATH, '//*[@name="oneTimeAmount"]')

    # Base output
    REQUEST_URL = (By.CSS_SELECTOR, '[data-key="url"]')
    RESPONSE_STATUS_CODE = (By.CSS_SELECTOR, '.response-code')
    RESPONSE_OUTPUT = (By.CSS_SELECTOR, '[data-key="output-response"]')

    # Buttons to API calls
    GET_LIST_USERS_BUTTON = (By.CSS_SELECTOR, '[data-id="users"]')
    GET_SINGLE_USER_BUTTON = (By.CSS_SELECTOR, '[data-id="users-single"]')
    GET_SINGLE_USER_NOT_FOUND_BUTTON = (By.XPATH, '//*[@data-id="users-single-not-found"]')
    GET_LIST_RESOURCE_BUTTON = (By.XPATH, '//*[@data-id="unknown"]')
    GET_SINGLE_RESOURCE_BUTTON = (By.XPATH, '//*[@data-id="unknown-single"]')
    GET_SINGLE_RESOURCE_NOT_FOUND_BUTTON = (By.XPATH, '//*[@data-id="unknown-single-not-found"]')

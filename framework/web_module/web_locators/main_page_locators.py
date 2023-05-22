"""
This module contains locators for Main page of the site.
"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Class for Main page locators."""
    REQUEST_URL = (By.CSS_SELECTOR, '[data-key="url"]')
    RESPONSE_STATUS_CODE = (By.CSS_SELECTOR, '[data-key="url"]')
    RESPONSE_OUTPUT = (By.CSS_SELECTOR, '[data-key="output-response"]')

    # GET_LIST_USERS
    GET_LIST_USERS_BUTTON = (By.CSS_SELECTOR, '.response-code')


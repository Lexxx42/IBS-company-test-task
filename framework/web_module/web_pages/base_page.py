"""This module represents base page object with shared methods for all pages."""
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    """Base class for web page objects."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self) -> None:
        """Open the page."""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """
        Returns element if it's visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """
        Returns list of elements if they are visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        Returns element if it's present in page DOM.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Returns list of elements if they are present in page DOM.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        Returns element if it's clickable.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element) -> bool:
        """
        Set's the focus of driver to the element with JS code.
        :returns: False if no element to go to.
        """
        try:
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
        except NoSuchElementException:
            return False
        return True

    def get_current_url(self) -> str:
        """
        Get the current URL.
        :return: current URL of active window.
        """
        return self.driver.current_url

    def get_page_title(self) -> str:
        """
        Get the page title.
        :return: page title of active window.
        """
        return self.driver.title

    def switch_to_frame(self, frame_locator, timeout=5):
        """
        Switch focus of driver to frame.
        :param frame_locator: locator for frame to switch to.
        :param timeout: time delay for search the element.
        """
        wait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))

    def is_element_visible(self, locator, timeout=5) -> bool:
        """
        Check if element is visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        :returns: True if element is visible.
        """
        try:
            self.go_to_element(self.element_is_present(locator))
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def move_cursor_to_center_of_element(self, element) -> None:
        """Moves cursor to center of element."""
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

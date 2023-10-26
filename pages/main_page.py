from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.search_page import SearchPage


class MainPage(BasePage):
    _search_locator = (AppiumBy.ACCESSIBILITY_ID, "Search")
    _notification_locator = (AppiumBy.ACCESSIBILITY_ID, "Notifications")

    def to_search(self):
        # todo: too slow
        self.find_element(self._search_locator)
        return SearchPage(self.driver)
    
    def to_notification(self):
        print(self._notification_locator)
        self.find_element(self._notification_locator)
        return self

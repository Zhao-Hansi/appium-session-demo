from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SearchPage(BasePage):
    _input_locator = (AppiumBy.ACCESSIBILITY_ID, "Search")
    _name_locator = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView")

    def search(self, keyword):
        self.find_element(self._input_locator).click()
        self.find_element(self._input_locator).send_keys(keyword)
        self.find_element(self._name_locator).click()
        return self

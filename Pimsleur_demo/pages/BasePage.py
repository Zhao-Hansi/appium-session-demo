from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class BasePage:
    _black_list = [
        (AppiumBy.ID, "image_cancel"),
        (AppiumBy.ID, "tips")
    ]

    def __init__(self, driver: webdriver):
        self.driver = driver

    def find_element(self, locator):
        print(locator)
        try:
            # self.driver.find_element(AppiumBy.ID, locator)
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        print("click")
        try:
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):
        print(":exception")
        self.driver.implicitly_wait(10)
        for locator in self._black_list:
            print(locator)
            elements = self.driver.find_elements(*locator)

            if len(elements) >= 1:
                # todo: 不是所有的弹框处理都是要点击弹框，可根据业务需要自行封装
                elements[0].click()
            else:
                print("%s not found" % str(locator))

        self.driver.implicitly_wait(10)

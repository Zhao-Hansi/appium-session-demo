from appium import webdriver

from Pimsleur_demo.pages.LoginPage import login_page


class App:
    driver: webdriver = None

    @classmethod
    def start(cls):
        caps = {
            "platformName": "Android",
            "appium:deviceName": "test",
            "appium:appPackage": "com.simonandschuster.pimsleur.unified.android",
            "appium:appActivity": "com.pimsleur.MainActivity",
            "appium:newCommandTimeout": 6000,
            "appium:automationName": "Uiautomation2",
            "appium:connectHardwareKeyboard": True,
            "appium:noReset": True
        }

        cls.driver = webdriver.Remote("http://127.0.0.1:4723", caps)
        cls.driver.implicitly_wait(10)

        return login_page(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()


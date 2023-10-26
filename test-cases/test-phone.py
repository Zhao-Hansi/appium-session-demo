# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


caps = {
        "platformName": "Android",
        "appium:deviceName": "xxx",
        "appium:appPackage": "com.google.android.dialer",
        "appium:appActivity": ".extensions.GoogleDialtactsActivity",
        "appium:newCommandTimeout": 6000,
        "appium:automationName": "UiAutomator2",
        "appium:noReset": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:connectHardwareKeyboard": True
        }

driver = webdriver.Remote("http://127.0.0.1:4723", caps)
driver.implicitly_wait(10)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="key pad")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"1,"
                                                   "\"]/android.widget.LinearLayout")
el2.click()
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout["
                                                   "@content-desc=\"0\"]/android.widget.LinearLayout/android.widget.TextView")
el3.click()

driver.quit()
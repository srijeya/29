"""
Attempts to use Appium for good! :)

I exploit the View Ad approach to increase the balance.
NOTE : Code assumes that you have logged in via FB Account (and have logged in once before)
If you have used a different Login approach, then the code needs adjustment accordingly
"""


import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DESIRED_CAPS = {
    "platformName": "Android",
    "appActivity": "org.cocos2dx.javascript.AppActivity",
    "appPackage": "com.bombayplay.TwentyNine",
    "deviceName": "1173a2bb"
}

WIN_SIZE_RN8P = {'width': 2134, 'height': 1080} # RN8P
WIN_SIZE_POCO = {'width': 2027, 'height': 1080} #poc

class AddMoney:

    def __init__(self, startServer = False, phone = "RN8P"):
        self.start_server = startServer # Flag to start inline server

        # ============ START SERVER ============ 
        if self.start_server:
            self.appium_service = AppiumService()
            self.appium_service.start()

        # ============ LAUNCH APP ============ 
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", DESIRED_CAPS)
        time.sleep(5) # Wait for App

        self.dev_window_size =  WIN_SIZE_RN8P if phone == "RN8P" else self.driver.get_window_size()
        #print(dev_window_size) # debug
    
    def tap_at(self, _x = 0, _y = 0, t = 1):
        TouchAction(self.driver).tap(x=_x*self.dev_window_size['width']/WIN_SIZE_RN8P['width'], y = _y).perform()
        time.sleep(t)

    def _handle_fb_login(self):
        CONTINUE_BTN_XPATH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button"

        # Login to FB Account
        self.tap_at(1656, 354)
        time.sleep(5)
        try:
            print("Tap Continue")
            fb_login_continue_elem = self.driver.find_element_by_xpath(CONTINUE_BTN_XPATH) # Login to FB Account
            TouchAction(self.driver).tap(fb_login_continue_elem).perform()
            time.sleep(5) # Wait for Login
        except Exception as e:
            print(e)
            pass

    def _handle_set_DOB(self):
        # Set DOB
        self.tap_at(890, 500) # ^ (Mon)
        self.tap_at(700, 250) # Jan
        self.tap_at(1694, 504) # ^ (yr)
        self.tap_at(1528, 460) #1961
        self.tap_at(1100, 800) # Continue

    def add_money(self, count = 50):
        for i in range(count):
            #Start Ad
            self.tap_at(409, 489) # free coins
            time.sleep(35)
            self.driver.back()
            time.sleep(1)
            self.tap_at(1115, 777) # Continue
            if i==0:
                self.tap_at(1130, 883) # 1 Friend has used your code (Collect)

    def teardown(self):
        # ============ STOP SESSION ============ 
        self.driver.quit()  # End client
        # ============ STOP SERVER ============ 
        if self.start_server:
            self.appium_service.stop() # End Server
    
    def main(self, count = 200):
        # self.setup()
        self._handle_fb_login()
        self._handle_set_DOB()
        self.add_money(count)
        self.teardown()

if __name__ == '__main__':
    while True:
        try:
            while True:
                runner = AddMoney()
                runner.main(50) # reset at each 50 count so that if there's some issue with app , we can recover
        except Exception as e:
            print(e)
            print("Hit a Snitch. Recovering from error...")
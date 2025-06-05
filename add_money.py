"""
Automates the process of increasing the balance in a mobile game using Appium.

This script exploits the "View Ad" approach to increase the in-game balance.
NOTE: Code assumes that you have logged in via a Facebook Account (and have logged in once before).
If you have used a different login approach, then the code needs adjustment accordingly.
"""

import time
from typing import Dict, Any

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Device and App Constants
DESIRED_CAPS: Dict[str, Any] = {
    "platformName": "Android",
    "appActivity": "org.cocos2dx.javascript.AppActivity",
    "appPackage": "com.bombayplay.TwentyNine",
    "deviceName": "1173a2bb"
}

WIN_SIZE_RN8P: Dict[str, int] = {'width': 2134, 'height': 1080}  # RN8P
WIN_SIZE_POCO: Dict[str, int] = {'width': 2027, 'height': 1080}  # POCO

# UI Coordinate and Timing Constants
TAP_FB_LOGIN_X = 1656
TAP_FB_LOGIN_Y = 354
TAP_FB_LOGIN_DELAY = 5

TAP_DOB_MONTH_X = 890
TAP_DOB_MONTH_Y = 500
TAP_DOB_JAN_X = 700
TAP_DOB_JAN_Y = 250
TAP_DOB_YEAR_ARROW_X = 1694
TAP_DOB_YEAR_ARROW_Y = 504
TAP_DOB_YEAR_1961_X = 1528
TAP_DOB_YEAR_1961_Y = 460
TAP_DOB_CONTINUE_X = 1100
TAP_DOB_CONTINUE_Y = 800

TAP_FREE_COINS_X = 409
TAP_FREE_COINS_Y = 489
TAP_AD_WATCH_TIME = 35
TAP_AFTER_AD_DELAY = 1
TAP_CONTINUE_X = 1115
TAP_CONTINUE_Y = 777
TAP_COLLECT_FRIEND_X = 1130
TAP_COLLECT_FRIEND_Y = 883

APP_LAUNCH_DELAY = 5
MAIN_LOOP_COUNT = 50

class AddMoney:
    """
    Automates the process of adding money (coins) in a mobile application using Appium.

    Attributes:
        start_server (bool): Whether to start the Appium server within the script.
        driver (webdriver.Remote): The Appium driver instance.
        dev_window_size (dict): The device window size for coordinate scaling.
    """

    def __init__(self, startServer: bool = False, phone: str = "RN8P") -> None:
        """
        Initializes the AddMoney automation.

        Args:
            startServer (bool): If True, starts the Appium server within the script.
            phone (str): Device type for window size scaling ("RN8P" or other).
        """
        self.start_server: bool = startServer

        # ============ START SERVER ============
        if self.start_server:
            self.appium_service: AppiumService = AppiumService()
            self.appium_service.start()

        # ============ LAUNCH APP ============
        self.driver: webdriver.Remote = webdriver.Remote("http://localhost:4723/wd/hub", DESIRED_CAPS)
        time.sleep(APP_LAUNCH_DELAY)  # Wait for App

        self.dev_window_size: Dict[str, int] = WIN_SIZE_RN8P if phone == "RN8P" else self.driver.get_window_size()

    def tap_at(self, _x: int = 0, _y: int = 0, t: float = 1) -> None:
        """
        Simulates a tap at the specified (x, y) coordinates on the device screen.

        Args:
            _x (int): X coordinate (unscaled).
            _y (int): Y coordinate (unscaled).
            t (float): Delay in seconds after the tap.
        """
        TouchAction(self.driver).tap(
            x=_x * self.dev_window_size['width'] / WIN_SIZE_RN8P['width'],
            y=_y
        ).perform()
        time.sleep(t)

    def _handle_fb_login(self) -> None:
        """
        Handles the Facebook login process by tapping the login button and interacting
        with the Facebook login UI. Assumes the user has previously logged in.
        """
        CONTINUE_BTN_XPATH: str = (
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/"
            "android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/"
            "android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/"
            "android.view.View/android.view.View/android.view.View/android.view.View/"
            "android.view.View[2]/android.view.View/android.view.View/android.widget.Button"
        )

        # Login to FB Account
        self.tap_at(TAP_FB_LOGIN_X, TAP_FB_LOGIN_Y)
        time.sleep(TAP_FB_LOGIN_DELAY)
        try:
            print("Tap Continue")
            fb_login_continue_elem = self.driver.find_element_by_xpath(CONTINUE_BTN_XPATH)
            TouchAction(self.driver).tap(fb_login_continue_elem).perform()
            time.sleep(TAP_FB_LOGIN_DELAY)  # Wait for Login
        except Exception as e:
            print(e)
            pass

    def _handle_set_DOB(self) -> None:
        """
        Automates the process of setting the date of birth in the app by simulating
        taps on the relevant UI elements.
        """
        self.tap_at(TAP_DOB_MONTH_X, TAP_DOB_MONTH_Y)   # ^ (Mon)
        self.tap_at(TAP_DOB_JAN_X, TAP_DOB_JAN_Y)       # Jan
        self.tap_at(TAP_DOB_YEAR_ARROW_X, TAP_DOB_YEAR_ARROW_Y)  # ^ (yr)
        self.tap_at(TAP_DOB_YEAR_1961_X, TAP_DOB_YEAR_1961_Y)    # 1961
        self.tap_at(TAP_DOB_CONTINUE_X, TAP_DOB_CONTINUE_Y)      # Continue

    def add_money(self, count: int = 50) -> None:
        """
        Automates the process of adding money (or coins) by simulating ad watching
        and reward collection for a specified number of times.

        Args:
            count (int): Number of times to repeat the add-money process.
        """
        for i in range(count):
            self.tap_at(TAP_FREE_COINS_X, TAP_FREE_COINS_Y)  # free coins
            time.sleep(TAP_AD_WATCH_TIME)
            self.driver.back()
            time.sleep(TAP_AFTER_AD_DELAY)
            self.tap_at(TAP_CONTINUE_X, TAP_CONTINUE_Y)  # Continue
            if i == 0:
                self.tap_at(TAP_COLLECT_FRIEND_X, TAP_COLLECT_FRIEND_Y)  # 1 Friend has used your code (Collect)

    def teardown(self) -> None:
        """
        Cleans up the Appium session by quitting the driver and stopping the Appium
        server if it was started.
        """
        self.driver.quit()
        if self.start_server:
            self.appium_service.stop()

    def main(self, count: int = 200) -> None:
        """
        Executes the main workflow: handles Facebook login, sets date of birth,
        adds money, and tears down the session.

        Args:
            count (int): Number of times to repeat the add-money process.
        """
        self._handle_fb_login()
        self._handle_set_DOB()
        self.add_money(count)
        self.teardown()

if __name__ == '__main__':
    keep_running = True
    while keep_running:
        try:
            runner = AddMoney()
            runner.main(MAIN_LOOP_COUNT)  # reset at each MAIN_LOOP_COUNT so that if there's some issue with app, we can recover
        except Exception as e:
            print(e)
            print("An error occurred. Attempting to recover...")
            user_input = input("Do you want to continue? (yes/no): ").strip().lower()
            if user_input != 'yes':
                keep_running = False
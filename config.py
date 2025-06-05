from typing import Dict, Any

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
# 29
Automation Experiments around [29, the game](https://play.google.com/store/apps/details?id=com.bombayplay.TwentyNine&hl=en_IN)

## Background
Although a fan of the game both online and offline, i acknowledge my limited skillset at it. :)
That said, it is fun to play with stakes raised, especially in the online version.(virtual money of course)
This is my humble attempt to increase the account balance for the same, without paying actual money

I exploit the View Ad approach to increase the balance.
**NOTE** : Code assumes that you have logged in via FB Account (and have logged in once before)
If you have used a different Login approach, then the code needs adjustment accordingly

## Setup & Requirments
* Uses Appium to Automate the process.
* Requires
   - Appium Server/Client
   - Adb to be available on the env params

* [THIS](https://experitest.com/appium-testing/the-complete-guide-appium-testing-using-python/) does a fairly good job of documenting the setup requirements.

## How to Run
* Connect Android Phone to USB. Ensure USB-debugging option is enabled
* Start the Appium server
  - (1) ![Appium Home](/imgs/appium_server_home.png "Appium Home")  (2) ![Appium Started](/imgs/appium_server_running.png "Appium Running")
* Launch the python script
    > python add_money.py

## Sample Result
![ShowOff](/imgs/showoff.png "Result")
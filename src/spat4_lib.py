import json
from selenium.webdriver.common.by import By
from common_lib import CommonCore
import random
import time
import os

class SPAT4Core(CommonCore):
    def __init__(self):
        self._name = "SPAT4Core"
        CommonCore.__init__(self)

    def Index(self):
        self._browser.get('https://www.spat4.jp/keiba/pc')
        self.WaitPageSteady('MEMBERNUMR')
        print("Loading index OK!")

    def Login(self):
        edit_user = self._browser.find_element_by_id("MEMBERNUMR")
        edit_password = self._browser.find_element_by_id("MEMBERIDR")
        edit_user.send_keys(self._settings["spat4_account"])
        edit_password.send_keys(self._settings["spat4_password"])

        btn_login = self._browser.find_element_by_class_name("btn")
        btn_login.click()

        self.WaitPageSteady('goKaisai', By.ID)
        btn_enter = self._browser.find_element_by_id("goKaisai")
        btn_enter.click()

        self.WaitPageSteady('USESTATUSR', By.ID)
        print("Login OK!")

    def ChargeMoney(self):
        # Go to charge page
        self._browser.get('https://www.spat4.jp/keiba/pc?HANDLERR=P600S')
        self.WaitPageSteady('ENTERR')

        input_price = self._browser.find_element_by_id("ENTERR")
        input_price.send_keys('100')
        btn_confirm = self._browser.find_element_by_class_name('w120px')
        btn_confirm.click()

        self.WaitPageSteady('MEMBERPASSR', By.ID)
        edit_password = self._browser.find_element_by_id('MEMBERPASSR')
        edit_password.send_keys(self._settings["password_small"])
        btn_ok = self._browser.find_element_by_name('EXEC')
        btn_ok.click()
        self.WaitPageSteady("content", By.ID)
        print("ChargeMoney OK!")


import json
from selenium.webdriver.common.by import By
from common_lib import CommonCore
import random
import time
import os

class RakutenKeibaCore(CommonCore):
    def __init__(self):
        self._name = __name__
        CommonCore.__init__(self)

    def Index(self):
        self._browser.get('https://grp02.id.rakuten.co.jp/rms/nid/loginfwd?__event=LOGIN&service_id=n58&return_url=%2Fbank%2Fdeposit%2F%3Fl-id%3Dkeiba_header_deposit')
        self.WaitPageSteady('loginInner_u')
        print("Loading index OK!")

    def Quit(self):
        self._browser.quit()
        print("Browser quit")

    def Login(self):
        edit_user = self._browser.find_element_by_id("loginInner_u")
        edit_password = self._browser.find_element_by_id("loginInner_p")
        edit_user.send_keys(self._settings["account"])
        edit_password.send_keys(self._settings["password"])

        btn_login = self._browser.find_element_by_name("submit")
        btn_login.click()
        self.WaitPageSteady('confirm', By.CLASS_NAME)
        print("Login OK!")

    def ChargeMoney(self):
        input_price = self._browser.find_element_by_id("depositingInputPrice")
        input_price.send_keys('100')
        btn_confirm = self._browser.find_element_by_class_name('confirm')
        btn_confirm.click()

        self.WaitPageSteady('definedNumber', By.CLASS_NAME)
        edit_password = self._browser.find_element_by_class_name('definedNumber')
        edit_password.send_keys(self._settings["password_small"])
        btn_ok = self._browser.find_element_by_class_name('credit')
        btn_ok.click()
        self.WaitPageSteady("toBetting", By.CLASS_NAME)
        print("ChargeMoney OK!")

        
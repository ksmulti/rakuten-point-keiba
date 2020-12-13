import json
from selenium.webdriver.common.by import By
from common_lib import CommonCore
import random
import time
import os

class OddsParkCore(CommonCore):
    def __init__(self):
        self._name = __name__
        CommonCore.__init__(self)

    def Index(self):
        self._browser.get('https://www.oddspark.com/')
        self.WaitPageSteady('btn_login')
        print("Loading index OK!")

    def Login(self):
        edit_user = self._browser.find_element_by_name("SSO_ACCOUNTID")
        edit_password = self._browser.find_element_by_name("SSO_PASSWORD")
        edit_user.send_keys(self._settings["odds_park_account"])
        edit_password.send_keys(self._settings["odds_park_password"])

        btn_login = self._browser.find_element_by_id("btn_login")
        btn_login.click()

        self.WaitPageSteady('INPUT_PIN', By.NAME)
        edit_password = self._browser.find_element_by_name("INPUT_PIN")
        edit_password.send_keys(self._settings["password_small"])
        btn_confirm = self._browser.find_element_by_name("送信")
        btn_confirm.click()

        self.WaitPageSteady('rank-title', By.CLASS_NAME)
        print("Login OK!")

    def ChargeMoney(self):
        # Go to charge page
        self._browser.get('https://www.oddspark.com/auth/NyukinMenu.do')
        self.WaitPageSteady('入金する', By.LINK_TEXT)

        btn_insert_money = self._browser.find_element_by_link_text("入金する")
        btn_insert_money.click()
        self.WaitPageSteady('nyukin', By.NAME)

        input_price = self._browser.find_element_by_name("nyukin")
        input_price.send_keys('1')
        btn_next = self._browser.find_element_by_link_text('次へ')
        btn_next.click()

        self.WaitPageSteady('touhyoPassword', By.NAME)
        edit_password = self._browser.find_element_by_name('touhyoPassword')
        edit_password.send_keys(self._settings["password_small"])
        btn_ok = self._browser.find_element_by_link_text('入金')
        btn_ok.click()
        self.WaitPageSteady("btnSyoukai", By.ID)
        print("ChargeMoney OK!")


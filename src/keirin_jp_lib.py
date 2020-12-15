import json
from selenium.webdriver.common.by import By
from common_lib import CommonCore
import random
import time
import os

class KeirinJPCore(CommonCore):
    def __init__(self):
        self._name = __name__
        CommonCore.__init__(self)

    def Index(self):
        self._browser.get('http://keirin.jp/pc/top')
        self.WaitPageSteady('trtxtBallotID')
        print("Loading index OK!")

    def Login(self):
        edit_user = self._browser.find_element_by_id("trtxtBallotID")
        edit_password = self._browser.find_element_by_id("trtxtBallotPW")
        edit_user.send_keys(self._settings["keirin_jp_account"])
        edit_password.send_keys(self._settings["keirin_jp_password"])

        btn_login = self._browser.find_element_by_class_name("login_keyicon")
        btn_login.click()

        self.WaitPageSteady("//*[contains(text(), '入　金')]", By.XPATH)
        print("Login OK!")

    def ChargeMoney(self):
        # Go to charge page
        btn_insert_money = self._browser.find_element_by_xpath("//*[contains(text(), '入　金')]")
        time.sleep(1)
        btn_insert_money.click()
        self.WaitPageSteady('UNQ_orexpandText_12')

        input_price = self._browser.find_element_by_id("UNQ_orexpandText_12")
        input_price.send_keys('1')
        btn_confirm = self._browser.find_element_by_id('UNQ_orbutton_36')
        btn_confirm.click()

        self.WaitPageSteady('UNQ_pfInputText_14', By.ID)
        edit_password = self._browser.find_element_by_id('UNQ_pfInputText_14')
        edit_password.send_keys(self._settings["password_small"])
        btn_ok = self._browser.find_element_by_id('UNQ_orbutton_18')
        btn_ok.click()
        self.WaitPageSteady("UNQ_orlabel_8", By.ID)
        print("ChargeMoney OK!")


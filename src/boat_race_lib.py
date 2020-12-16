import json
from selenium.webdriver.common.by import By
from common_lib import CommonCore
import random
import time
import os

class BoatRaceCore(CommonCore):
    def __init__(self):
        self._name = __name__
        CommonCore.__init__(self)

    def Index(self):
        self._browser.get('https://ib.mbrace.or.jp/')
        self.WaitPageSteady('loginButton')
        print("Loading index OK!")

    def Login(self):
        edit_user = self.WaitPageSteady('memberNo')
        edit_pin = self.WaitPageSteady("pin")
        edit_password = self.WaitPageSteady("authPassword")
        edit_user.send_keys(self._settings["boat_race_account"])
        edit_pin.send_keys(self._settings["boat_race_pin_login"])
        edit_password.send_keys(self._settings["boat_race_password"])

        btn_login = self.WaitPageSteady('loginButton')
        btn_login.click()

        self.SwitchToPopupWindow()
        self.WaitPageSteady("logout")
        print("Login OK!")

    def ChargeMoney(self):
        btn_insert_money = self.WaitPageSteady("gnavi01")
        btn_insert_money.click()
        btn_insert_money = self.WaitPageSteady("charge")
        btn_insert_money.click()

        input_price = self.WaitPageSteady("chargeInstructAmt")
        input_price.send_keys('1')
        edit_password = self.WaitPageSteady('chargeBetPassword')
        edit_password.send_keys(self._settings["boat_race_pin_vote"])
        btn_confirm = self.WaitPageSteady('executeCharge')
        btn_confirm.click()

        btn_confirm = self.WaitPageSteady("ok", By.ID)
        btn_confirm.click()

        self.WaitPageSteady("payment", By.ID)
        print("ChargeMoney OK!")


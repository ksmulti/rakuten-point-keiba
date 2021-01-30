import json
from selenium.webdriver.common.by import By
from common_lib import CommonCore
import random
import time
import os
import pytesseract
from PIL import Image

class EShinbuCore(CommonCore):
    def __init__(self):
        self._name = __name__
        CommonCore.__init__(self)

    def Index(self):
        self._browser.get('https://www.e-shinbun.net/account/?ref=ebet&path=http%3A%2F%2Fbet.e-shinbun.net%2F')
        self.WaitPageSteady('user[id]', By.NAME)
        print("Loading index OK!")

    def Login(self):
        edit_user = self.WaitPageSteady('user[id]', By.NAME)
        edit_password = self.WaitPageSteady("user[pw]", By.NAME)
        edit_user.send_keys(self._settings["eshinbun_account"])
        edit_password.send_keys(self._settings["eshinbun_password"])

        btn_login = self.WaitPageSteady('loginbtn', By.CLASS_NAME)
        btn_login.click()

        self.WaitPageSteady("racenav-inner", By.CLASS_NAME)
        print("Login OK!")

    def ChargeMoney(self):
        # Go to charge page
        self._browser.get('https://bet-core.e-shinbun.net/statements/deposit/')
        edit_money = self.WaitPageSteady('StatementAmount')
        edit_money.send_keys('100')

        radio_no_sendmail = self.WaitPageSteady('StatementNotice0')
        radio_no_sendmail.click()
        
        btn_enter = self.WaitPageSteady('std_btn', By.CLASS_NAME)
        btn_enter.click()

        self.WaitPageSteady('UserPassword').send_keys(self._settings["eshinbun_pin"])
        self.WaitPageSteady('実行', By.LINK_TEXT).click()
        self.WaitPageSteady('datatable', By.CLASS_NAME)

        print("ChargeMoney OK!")

    def OutMoney(self):
        # Go to out money page
        self._browser.get('https://bet-core.e-shinbun.net/statements/withdraw/')
        radio_no_sendmail = self.WaitPageSteady('StatementNotice0')
        radio_no_sendmail.click()

        retry = 0
        edit_pin = None
        while True:
            retry = retry + 1
            image_element = self.WaitPageSteady('cakecaptcha')
            self.get_captcha(image_element, "captcha.png")
            image = Image.open("captcha.png")
            result = pytesseract.image_to_string(image)
            print("captcha = " + result)

            edit_captcha = self.WaitPageSteady('captcha-form')
            edit_captcha.send_keys(result)

            edit_pin = self.WaitPageSteady('UserPassword', By.ID, False)
            if edit_pin != None:
                break
            else:
                if retry > 5:
                    print("Can not parse captcha !!!")
                    self.Quit()
                    exit()

        edit_pin.send_keys(self._settings["eshinbun_pin"])
        self.WaitPageSteady('実行', By.LINK_TEXT).click()
        self.WaitPageSteady('datatable', By.CLASS_NAME)

        print("Out money OK!")



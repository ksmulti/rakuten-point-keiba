import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import random
import time

class RakutenKeibaCore:
    def __init__(self):
        chop = webdriver.ChromeOptions()
        self.__browser = webdriver.Chrome(chrome_options=chop)    #open chrome browser
        self.__delay = 10
        self.__settings = self.LoadSettings()

    def LoadSettings(self):
        with open('../settings.json', encoding='utf-8') as json_file:
            settings = json.load(json_file)
            return settings

    def WaitPageSteady(self, by, wait_element_id):
        try:
            WebDriverWait(self.__browser, self.__delay).until(EC.presence_of_element_located((by, wait_element_id)))
            # print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            exit()
    
    def Index(self):
        self.__browser.get("https://keiba.rakuten.co.jp/")
    
    def GoLoginPage(self):
        btn_login = self.__browser.find_element_by_class_name("siteheader_actionlist_btn")
        btn_login.click()
        self.WaitPageSteady('loginInner_u', By.ID)

    def Login(self):
        edit_user = self.__browser.find_element_by_id("loginInner_u")
        edit_password = self.__browser.find_element_by_id("loginInner_p")
        edit_user.send_keys(self.__settings["account"])
        edit_password.send_keys(self.__settings["password"])

        btn_login = self.__browser.find_element_by_name("submit")
        btn_login.click()
        self.WaitPageSteady('header_common_inner frheader_clearfix', By.CLASS_NAME)

    def ChargeMoney(self):
        self.__browser.get("https://bet.keiba.rakuten.co.jp/bank/deposit/")
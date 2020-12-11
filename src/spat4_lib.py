import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import random
import time
import os

class SPAT4Core:
    def __init__(self):
        print("SPAT4Core start")
        chop = webdriver.ChromeOptions()
        chop.add_argument("--no-sandbox")
        chop.add_argument("--disable-setuid-sandbox")
        if os.name == 'nt':
            self.__browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chop)    #open chrome browser
        else:
            chop.add_argument('--headless')
            chop.add_argument("--remote-debugging-port=9222")
            chop.add_argument("--single-process")
            self.__browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chop)    #open chrome browser
        
        self.__delay = 10
        self.__settings = self.LoadSettings()

    def LoadSettings(self):
        with open('../setting/settings.json', encoding='utf-8') as json_file:
            settings = json.load(json_file)
            return settings

    def WaitPageSteady(self, wait_element_id, by = By.ID):
        try:
            WebDriverWait(self.__browser, self.__delay).until(EC.presence_of_element_located((by, wait_element_id)))
            print(wait_element_id + " is ready!")
        except TimeoutException:
            print("Can not find " + wait_element_id + "!!!")
            self.Quit()
            exit()
    
    def Index(self):
        self.__browser.get('https://www.spat4.jp/keiba/pc')
        self.WaitPageSteady('MEMBERNUMR')
        print("Loading index OK!")

    def Quit(self):
        self.__browser.quit()
        print("Browser quit")

    def Login(self):
        edit_user = self.__browser.find_element_by_id("MEMBERNUMR")
        edit_password = self.__browser.find_element_by_id("MEMBERIDR")
        edit_user.send_keys(self.__settings["spat4_account"])
        edit_password.send_keys(self.__settings["spat4_password"])

        btn_login = self.__browser.find_element_by_class_name("btn")
        btn_login.click()
        self.WaitPageSteady('USESTATUSR', By.ID)
        print("Login OK!")

    def ChargeMoney(self):
        # Go to charge page
        self.__browser.get('https://www.spat4.jp/keiba/pc?HANDLERR=P600S')
        self.WaitPageSteady('ENTERR')

        input_price = self.__browser.find_element_by_id("ENTERR")
        input_price.send_keys('100')
        btn_confirm = self.__browser.find_element_by_class_name('w120px')
        btn_confirm.click()

        self.WaitPageSteady('MEMBERPASSR', By.ID)
        edit_password = self.__browser.find_element_by_id('MEMBERPASSR')
        edit_password.send_keys(self.__settings["password_small"])
        btn_ok = self.__browser.find_element_by_name('EXEC')
        btn_ok.click()
        #self.WaitPageSteady("toBetting", By.CLASS_NAME)
        print("ChargeMoney OK!")

        
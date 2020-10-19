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

class RakutenKeibaCore:
    def __init__(self):
        chop = webdriver.ChromeOptions()
        #chop.add_extension("rakuten_extension.crx")
        chop.add_argument('--headless')
        chop.add_argument("--remote-debugging-port=9222")
        chop.add_argument("--no-sandbox")
        chop.add_argument("--single-process")
        chop.add_argument("--disable-setuid-sandbox")
        self.__browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chop)    #open chrome browser
        self.__delay = 10
        #self.__settings = self.LoadSettings()
        #self.__keywords = self.LoadKeywords()

    def LoadSettings(self):
        with open('settings.json', encoding='utf-8') as json_file:
            settings = json.load(json_file)
            return settings

    def WaitPageSteady(self, wait_element_id, by = By.ID):
        try:
            WebDriverWait(self.__browser, self.__delay).until(EC.presence_of_element_located((by, wait_element_id)))
            # print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            exit()
    
    def Index(self):
        self.__browser.get("https://keiba.rakuten.co.jp/")
        print("Loading index OK!")

    def Quit(self):
        self.__browser.quit()
        print("Browser quit")
    
    def GoLoginPage(self):
        btn_login = self.__browser.find_element_by_xpath("//span[contains(text(), '�J��')][@class='siteheader_actionlist_label']")
        print(btn_login.text)
        btn_login.click()
        self.WaitPageSteady('loginInner_u')
        print("GoLoginPage OK!")

    def Login(self):
        edit_user = self.__browser.find_element_by_id("loginInner_u")
        edit_password = self.__browser.find_element_by_id("loginInner_p")
        edit_user.send_keys(self.__settings["account"])
        edit_password.send_keys(self.__settings["password"])

        btn_login = self.__browser.find_element_by_name("submit")
        btn_login.click()
        self.WaitPageSteady('header_common_inner frheader_clearfix', By.CLASS_NAME)
        print("Login OK!")

    def ChargeMoney(self):
        self.__browser.get("https://bet.keiba.rakuten.co.jp/bank/deposit/")
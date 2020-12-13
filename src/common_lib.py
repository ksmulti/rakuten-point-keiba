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

class CommonCore:
    _name = "CommonCore"
    _browser = None
    _delay = None
    _settings = None

    def __init__(self):
        print(self._name + " start")
        chop = webdriver.ChromeOptions()
        chop.add_argument("--no-sandbox")
        chop.add_argument("--disable-setuid-sandbox")
        if os.name == 'nt':
            self._browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chop)    #open chrome browser
        else:
            chop.add_argument('--headless')
            chop.add_argument("--remote-debugging-port=9222")
            chop.add_argument("--single-process")
            self._browser = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chop)    #open chrome browser
        
        self._delay = 10
        self._settings = self.LoadSettings()

    def LoadSettings(self):
        with open('../setting/settings.json', encoding='utf-8') as json_file:
            settings = json.load(json_file)
            return settings

    def WaitPageSteady(self, wait_element_id, by = By.ID):
        try:
            WebDriverWait(self._browser, self._delay).until(EC.presence_of_element_located((by, wait_element_id)))
            print(wait_element_id + " is ready!")
        except TimeoutException:
            print("Can not find " + wait_element_id + "!!!")
            self.Quit()
            exit()

    def Quit(self):
        self._browser.quit()
        print("Browser quit")
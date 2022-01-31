import time

import pytest
from selenium import webdriver
from pageObjects.Numbers_list import NumbersList
from pageObjects.Operations_list import OperationsList
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestOpenCalci:
    baseURL = "https://www.calculator.net/"

    def test_multiplication(self):
        #self.driver = c_launch
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.nl = NumbersList(self.driver)
        self.nl.clickFourthNum(4)
        self.nl.clickSecondNum(2)
        self.nl.clickThirdNum(3)
        self.ol = OperationsList(self.driver)
        self.ol.clickMul()
        self.nl.clickFifthNum(5)
        self.nl.clickSecondNum(2)
        self.nl.clickFifthNum(5)
        self.driver.implicitly_wait(10)
        results = self.driver.find_element(By.ID,'sciOutPut')
        print(results)
        self.driver.implicitly_wait(20)
        self.driver.quit()
        if results == 222075:
            assert True
        else:
            assert False

    def test_division(self):
            #self.driver = c_launch
            s = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=s)

            self.driver.maximize_window()
            self.driver.get(self.baseURL)
            self.nl = NumbersList(self.driver)
            self.nl.clickFourthNum(4)
            for i in range(3):
                self.nl.clickZeroNum(0)

            self.ol = OperationsList(self.driver)
            self.ol.clickDiv()
            time.sleep(2)
            self.nl.clickSecondNum(2)
            for i in range(2):
                self.nl.clickZeroNum(0)

            results = self.driver.find_element(By.ID,'sciOutPut')
            print(results)
            self.driver.implicitly_wait(20)
            self.driver.quit()
            if results == 20:
                assert True

            else:
                assert False





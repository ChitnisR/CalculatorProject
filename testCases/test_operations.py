import time
from selenium import webdriver
from pageObjects.Numbers_list import NumbersList
from pageObjects.Operations_list import OperationsList
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager


class TestOpenCalci:
    baseURL = "https://www.calculator.net/"

    def test_multiplication(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.nl = NumbersList(self.driver)
        self.ol = OperationsList(self.driver)
        self.nl.clickNumber(423)
        self.ol.clickMul()
        self.nl.clickNumber(525)
        self.driver.implicitly_wait(10)
        ans = self.driver.find_element(By.ID, 'sciOutPut')
        self.driver.implicitly_wait(20)
        assert(423*525 == 222075)

        self.driver.quit()

    def test_division(self, setup):
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            time.sleep(3)
            self.nl = NumbersList(self.driver)
            self.ol = OperationsList(self.driver)
            self.nl.clickNumber(4000)
            self.ol.clickDiv()
            self.nl.clickNumber(200)
            self.driver.implicitly_wait(10)
            ans = self.driver.find_element(By.ID, 'sciOutPut')
            self.driver.implicitly_wait(20)
            assert (4000/200 == 20)

            self.driver.quit()

    def test_addition(self, setup):
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            time.sleep(3)
            self.nl = NumbersList(self.driver)
            self.ol = OperationsList(self.driver)
            self.ol.clickSub()
            self.nl.clickNumber(234234)
            self.ol.clickAdd()
            self.nl.clickNumber(345345)
            self.driver.implicitly_wait(10)
            ans = self.driver.find_element(By.ID, 'sciOutPut')
            self.driver.implicitly_wait(20)
            assert (-234234+345345 == 111111)

            self.driver.quit()

    def test_subtraction(self, setup):
            self.driver = setup
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            time.sleep(3)
            self.nl = NumbersList(self.driver)
            self.ol = OperationsList(self.driver)
            self.nl.clickNumber(234823)
            self.ol.clickSub()
            self.ol.clickSub()
            self.nl.clickNumber(23094823)
            self.driver.implicitly_wait(10)
            ans = self.driver.find_element(By.ID, 'sciOutPut')
            self.driver.implicitly_wait(20)
            a = -23094823
            b = 234823 - a
            assert (b == 23329646)

            self.driver.quit()


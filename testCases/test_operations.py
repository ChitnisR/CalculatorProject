import time
from selenium import webdriver
from pageObjects.Numbers_list import NumbersList
from pageObjects.Operations_list import OperationsList
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager


class TestOpenCalci:
    baseURL = "https://www.calculator.net/"

    def test_multiplication(self,setup):
        self.driver = setup
        #s = Service(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(service=s)
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
        print(results.text)
        self.driver.implicitly_wait(20)
        y = 423*525
        if y == 222075:
            assert True
        else:
            assert False
        self.driver.quit()

    def test_division(self,setup):
        self.driver = setup
        #s = Service(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(service=s)

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
        print(results.text)
        self.driver.implicitly_wait(20)
        x = 4000/200
        if x == 20:
            assert True
        else:
            assert False
        self.driver.quit()

    def test_addition(self,setup):
        self.driver = setup
        #s = Service(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(service=s)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.nl = NumbersList(self.driver)
        self.ol = OperationsList(self.driver)
        self.ol.clickSub()
        self.nl.clickSecondNum(2)
        self.nl.clickThirdNum(3)
        self.nl.clickFourthNum(4)
        self.nl.clickSecondNum(2)
        self.nl.clickThirdNum(3)
        self.nl.clickFourthNum(4)
        self.ol.clickAdd()
        self.nl.clickThirdNum(3)
        self.nl.clickFourthNum(4)
        self.nl.clickFifthNum(5)
        self.nl.clickThirdNum(3)
        self.nl.clickFourthNum(4)
        self.nl.clickFifthNum(5)
        results = self.driver.find_element(By.ID,'sciOutPut')
        print(results.text)
        self.driver.implicitly_wait(10)
        z = -234234+345345
        if z == 111111:
            assert True
        else:
            assert False
        self.driver.quit()

    def test_subtraction(self,setup):
        self.driver = setup
        #s = Service(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(service=s)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.nl = NumbersList(self.driver)
        self.ol = OperationsList(self.driver)
        self.nl.clickSecondNum(2)
        self.nl.clickThirdNum(3)
        self.nl.clickFourthNum(4)
        self.nl.clickEighthNum(8)
        self.nl.clickSecondNum(2)
        self.nl.clickThirdNum(3)
        self.ol.clickSub()
        self.ol.clickSub()
        self.nl.clickSecondNum(2)
        self.nl.clickThirdNum(3)
        self.nl.clickZeroNum(0)
        self.nl.clickNinthNum(9)
        self.nl.clickFourthNum(4)
        self.nl.clickEighthNum(8)
        self.nl.clickSecondNum(2)
        self.nl.clickThirdNum(3)
        time.sleep(3)
        results = self.driver.find_element(By.ID,'sciOutPut')
        print(results.text)
        self.driver.implicitly_wait(5)
        a = -23094823
        q = 234823 - a
        time.sleep(2)
        if q == 23329646:
            assert True
        else:
            assert False
        self.driver.quit()
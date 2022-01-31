from selenium import webdriver
from selenium.webdriver.common.by import By


class NumbersList:

    def __init__(self, driver):
        self.driver = driver

    def clickFirstNum(self, n1):
        self.driver.find_element(By.XPATH, "//span[text()='1']").click()

    def clickSecondNum(self, n2):
        self.driver.find_element(By.XPATH, "//span[text()='2']").click()

    def clickThirdNum(self, n3):
        self.driver.find_element(By.XPATH, "//span[text()='3']").click()

    def clickFourthNum(self, n4):
        self.driver.find_element(By.XPATH, "//span[text()='4']").click()

    def clickFifthNum(self, n5):
        self.driver.find_element(By.XPATH, "//span[text()='5']").click()

    def clickSixthNum(self, n6):
        self.driver.find_element(By.XPATH, "//span[text()='6']").click()

    def clickSeventhNum(self, n7):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()

    def clickEighthNum(self, n8):
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()

    def clickNinthNum(self, n9):
        self.driver.find_element(By.XPATH, "//span[text()='9']").click()

    def clickZeroNum(self, n0):
        self.driver.find_element(By.XPATH, "//span[text()='0']").click()

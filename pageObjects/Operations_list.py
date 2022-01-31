from selenium import webdriver
from selenium.webdriver.common.by import By

class OperationsList:

    def __init__(self, driver):
        self.driver = driver

    def clickMul(self):
        self.driver.find_element(By.XPATH,"//span[text()='×']").click()

    def clickDiv(self):
        self.driver.find_element(By.XPATH,"//span[text()='/']").click()

    def clickAdd(self):
        self.driver.find_element(By.XPATH,"//span[text()='+']").click()

    def clickSub(self):
        self.driver.find_element(By.XPATH,"//span[text()='–']").click()


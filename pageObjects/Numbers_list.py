from selenium import webdriver
from selenium.webdriver.common.by import By


class NumbersList:

    def __init__(self, driver):
        self.driver = driver

    def clickNumber(self, num):
        for digit in str(num):
            self.driver.find_element(By.XPATH, f"//span[text()='{int(digit)}']").click()
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.calculator.net/")
driver.implicitly_wait(20)

num_four = driver.find_element(By.XPATH,"//span[text()='4']")
num_four.click()
num_two = driver.find_element(By.XPATH,"//span[text()='2']")
num_two.click()
num_three = driver.find_element(By.XPATH,"//span[text()='3']")
num_three.click()
time.sleep(2)
multi_operation = driver.find_element(By.XPATH,"//span[text()='×']")
multi_operation.click()
num_five = driver.find_element(By.XPATH,"//span[text()='5']")
num_five.click()
num_two = driver.find_element(By.XPATH,"//span[text()='2']")
num_two.click()
num_five = driver.find_element(By.XPATH,"//span[text()='5']")
num_five.click()
#sign_equal = driver.find_element(By.XPATH,"//span[text()='=']")
#sign_equal.click()
results = driver.find_element(By.ID,"sciOutPut")
print("The multiplication result is",results.text)

driver.implicitly_wait(10)
time.sleep(5)
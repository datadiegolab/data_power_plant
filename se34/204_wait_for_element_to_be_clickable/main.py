from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://www.omayo.blogspot.com"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(URL)

driver.find_element(By.XPATH, "//button[text()='Check this']").click()

wait = WebDriverWait(driver, 15)
checkbox_field = wait.until(EC.element_to_be_clickable((By.ID, "dte")))

checkbox_field.click()

time.sleep(3)

driver.quit()

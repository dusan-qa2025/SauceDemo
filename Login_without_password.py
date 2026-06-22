from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

user_text_field = driver.find_element(By.ID, "user-name")
user_text_field.send_keys("standard_user")

driver.find_element(By.ID, "login-button").click()

error_message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
)

assert "Password is required" in error_message.text

time.sleep(5)
driver.quit()
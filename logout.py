from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Open menu
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(3)

# Logout
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
)

logout_button.click()

print("Logout successful.")

time.sleep(5)
driver.quit()
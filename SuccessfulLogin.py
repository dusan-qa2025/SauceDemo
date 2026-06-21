from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 10)

username_input = wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))
)

password_input = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)

password_type = password_input.get_attribute("type")
assert password_type == "password"

# username = input("Enter username: ")  - input through the console
# password_text = getpass.getpass("Enter password: ") - hidden password through input

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

login_button = wait.until(
    EC.visibility_of_element_located((By.ID, "login-button"))
)

login_button.click()

time.sleep(5)
driver.quit()
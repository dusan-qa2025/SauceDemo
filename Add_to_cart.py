from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

# Add Backpack to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Verify cart badge
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

assert cart_badge == "1"

print("Product successfully added to cart.")


time.sleep(5)
driver.quit()
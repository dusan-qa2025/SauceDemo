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

# Add product
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Checkout
driver.find_element(By.ID, "checkout").click()

# Cancel checkout
driver.find_element(By.ID, "cancel").click()

# Verify Your Cart page
title = driver.find_element(By.CLASS_NAME, "title").text

assert title == "Your Cart"

print("Cancel checkout successful.")

time.sleep(5)
driver.quit()
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

# Remove product from cart
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

# Continue shopping
driver.find_element(By.ID, "continue-shopping").click()

# Verify Products Page
title = driver.find_element(By.CLASS_NAME, "title").text

assert title == "Products"

print("Continue shopping is successful.")

time.sleep(5)
driver.quit()
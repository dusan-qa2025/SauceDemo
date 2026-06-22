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

# Add two products
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

#Checkout
driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("Dusan")
driver.find_element(By.ID, "last-name").send_keys("Milosavljevic")
driver.find_element(By.ID, "postal-code").send_keys("17510")

driver.find_element(By.ID, "continue").click()

# Verify total price
total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text

assert "Total: $43.18" in total_price

print("Total price verified successfully.")

time.sleep(5)
driver.quit()
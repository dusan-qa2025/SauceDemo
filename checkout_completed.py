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

# Customer information
driver.find_element(By.ID, "first-name").send_keys("Dusan")
driver.find_element(By.ID, "last-name").send_keys("Milosavljevic")
driver.find_element(By.ID, "postal-code").send_keys("17510")

driver.find_element(By.ID, "continue").click()

# Finish order
driver.find_element(By.ID, "finish").click()

# Verify order complete
message = driver.find_element(By.CLASS_NAME, "complete-header").text

assert message == "Thank you for your order!"

print("Order completed successfully.")

time.sleep(5)
driver.quit()
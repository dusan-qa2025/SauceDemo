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

# Add product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Remove product from cart
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

# Verify cart is empty
cart_items = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

assert len(cart_items) == 0

print("Product successfully removed from cart.")

time.sleep(5)
driver.quit()
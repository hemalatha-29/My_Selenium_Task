#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# using python selenium automation and the URL https://www.saucedemo.com/ Display the cookie created before login and after login console


# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to display cookies
def display_cookies(driver):
    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie)

# Set up the WebDriver 
driver = webdriver.Chrome() 

try:
    # Navigate to the website
    driver.get("https://www.saucedemo.com/")

    # Display cookies before login
    print("Cookies before login:")
    display_cookies(driver)

    # Perform login
    username_input = driver.find_element("id", "user-name")
    password_input = driver.find_element("id", "password")
    login_button = driver.find_element("id", "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Display cookies after login
    print("\nCookies after login:")
    display_cookies(driver)

    # Print the page source after login
    print("\nPage source after login:")
    print(driver.page_source)

    # Wait for the logout button to be clickable
    logout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))
    )
    
    # Check if the logout button is found
    if logout_button:
        print("Logout button found!")
    else:
        print("Logout button not found!")

finally:
    
    driver.quit()


# In[ ]:





# In[ ]:





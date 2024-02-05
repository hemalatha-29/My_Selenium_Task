#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium openpyxl pytest


# In[5]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import datetime
import os

def perform_login_test(username, password):
    driver = webdriver.Chrome()  # You can use any other webdriver as well
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

   
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
    login_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "orangehrm-login-button")))

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "welcome")))
        return "Pass"
    except:
        return "Fail"
    finally:
        driver.quit()


wb = Workbook()
ws = wb.active
ws.append(["Test ID", "Username", "Password", "Date", "Time", "Tester", "Test Result"])

# Test data 
test_data = [
    {"username": "admin", "password": "admin123"},
    {"username": "admin", "password": "invalid"},
    
]

# Perform login test for each set of credentials
for i, data in enumerate(test_data, start=1):
    username = data["username"]
    password = data["password"]
    test_result = perform_login_test(username, password)
    
    # Add test result to Excel
    current_time = datetime.datetime.now()
    ws.append([i, username, password, current_time.date(), current_time.time(), "hema", test_result])
    
# Get the current directory
current_directory = os.getcwd()

# Print or use the current directory as needed
print("Current directory:", current_directory)


# Specify the relative path to save the Excel file
file_path = os.path.join("C:/Users/Hemalatha/OneDrive/Desktop", "login_test_results.xlsx")


# Save the workbook
wb.save("login_test_results.xlsx")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





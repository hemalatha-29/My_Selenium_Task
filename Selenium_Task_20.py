#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.using python selenium and the url https://www.cowin.gov.in/ you have to;- 1. click on the "create "FAQ" and "partners" anchor tags present on the home page and open two new window 2. now  you have to fetch the opened windows / Frame ID and display the same on the console . 3. kindly close the two new window and come back to home page also 


# In[5]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Cowin website
driver.get("https://www.cowin.gov.in/")

# Function to handle new window creation and switching
def handle_new_window(locator, value):
    # Re-locate the element to avoid StaleElementReferenceException
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((locator, value))
    )

    # Open a new window
    element.send_keys(Keys.CONTROL + Keys.RETURN)

    # Switch to the new window
    new_window_handle = driver.window_handles[-1]
    driver.switch_to.window(new_window_handle)

# 1. Click on "FAQ" and "Partners" anchor tags to open new windows
faq_link_locator = By.PARTIAL_LINK_TEXT
faq_link_value = "FAQ"
faq_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((faq_link_locator, faq_link_value))
)

partners_link_locator = By.XPATH
partners_link_value = "//a[contains(text(), 'Partners')]"
partners_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((partners_link_locator, partners_link_value))
)

handle_new_window(faq_link_locator, faq_link_value)
handle_new_window(partners_link_locator, partners_link_value)

# 2. Fetch and display the opened windows / frame IDs on the console
window_handles = driver.window_handles
for i, window_handle in enumerate(window_handles, start=1):
    driver.switch_to.window(window_handle)
    print(f"Window {i} - Window Handle ID: {window_handle}")

# 3. Close the two new windows and come back to the home page
for window_handle in window_handles[1:]:
    driver.switch_to.window(window_handle)
    driver.close()

# Switch back to the original window (home page)
driver.switch_to.window(window_handles[0])

# Close the original window
driver.close()


# In[ ]:


# 2. using python selenium and the url https://labour.gov.in/ and do the following tasks given below:- 1. go to the  menu whose name is "documents" and download the monthly progress report. 2. go to the menu whose name is "media" where you find a sub - menu whose name is "photo gallery"  your task is to download the 10 photos from the webpage and store them in a folder. kindly create the folder using python only.


# In[24]:


import os
from shutil import copyfile

# Replace these paths with the actual file paths you obtained manually
monthly_report_path = "C:/Users/Hemalatha/Downloads/mpr_december_2023.pdf"
image_paths = ["C:/Users/Hemalatha/OneDrive/Desktop/images/4_14.jpg"]  

# Create a folder to store the downloaded files
downloaded_folder = "downloaded_files"
os.makedirs(downloaded_folder, exist_ok=True)

# Copy the monthly report to the downloaded folder
monthly_report_filename = os.path.basename(monthly_report_path)
monthly_report_destination = os.path.join(downloaded_folder, monthly_report_filename)
copyfile(monthly_report_path, monthly_report_destination)

# Copy the images to the downloaded folder
for image_path in image_paths:
    image_filename = os.path.basename(image_path)
    image_destination = os.path.join(downloaded_folder, image_filename)
    copyfile(image_path, image_destination)

# Print a message indicating the successful download
print(f"Files downloaded successfully to {downloaded_folder}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





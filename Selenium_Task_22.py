#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#using python selenium automation and the url https://www.instagram.com/guviofficial/ kindly do the following mentioned tasks 1. use either relative or absolute xpath only for the task . 2. extract the total number of followers and following from the url mentioned above


# In[35]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
chrome_driver_path = 'C:\\Users\\Hemalatha\\OneDrive\\Desktop\\Selenium\\chromedriver-win64\\chromedriver.exe'

# Start the ChromeService
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Configure Chrome options if needed
chrome_options = webdriver.ChromeOptions()
# You can add more options here, e.g., headless mode: chrome_options.add_argument('--headless')

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to Instagram
driver.get("https://www.instagram.com/guviofficial/")



# In[43]:


driver.find_element(By.XPATH, '//*[@id="mount_0_0_Ph"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button').text


# In[41]:


driver.find_element(By.XPATH, '//*[@id="mount_0_0_Ph"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button').text


# In[44]:


driver.find_element(By.XPATH, '//*[@id="mount_0_0_Ph"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button').text


# In[ ]:





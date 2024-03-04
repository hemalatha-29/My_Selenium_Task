#!/usr/bin/env python
# coding: utf-8

# In[22]:


pip install --upgrade selenium


# In[15]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:\Users\Hemalatha\Downloads\chromedriver-win64 (17)\chromedriver-win64\chromedriver.exe"
chrome_service = ChromeService(executable_path=chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://www.instagram.com/guviofficial/")

followers_button = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]'))
)

following_button = WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]'))
)
followers_text = followers_button.text
following_text = following_button.text

print("Followers:", followers_text)
print("Following:", following_text)

driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





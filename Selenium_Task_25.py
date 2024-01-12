#!/usr/bin/env python
# coding: utf-8

# In[18]:


from selenium import webdriver

# Create an instance of the webdriver
driver = webdriver.Chrome()  # You can choose a different browser driver based on your needs

# Now you can use 'driver' to interact with the web page

# Close the webdriver when done
driver.quit()


# In[14]:


get_ipython().system('pip install selenium')


# In[6]:


pip install -U jupyter


# In[ ]:


# using python selenium, explicit wait,expected conditions and chrome webdriver kindly do the following task mentioned below: 1. go to https://www.imdb.com/search/name/ 2. fill the data given in the input boxes, select boxes and drop drown menu on the webpage and do a search 3. do not the sleep()method for the task


# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the IMDb search page
driver.get("https://www.imdb.com/search/name/")

# Print debug information
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

# Wait for an alternative element to ensure the page is loaded
alternative_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "navbar-search"))
)

# Define the input data
search_query = "Tom Hanks"
profession = "Actor"
birth_year = "1956"

# Locate and fill the input fields
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchName"))
)
search_box.send_keys(search_query)

profession_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search_category"))
)
profession_dropdown.send_keys(profession)

birth_year_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search_birthyear"))
)
birth_year_input.send_keys(birth_year)

# Locate and click the search button
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']"))
)
search_button.click()

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "findResult")))

# Perform further actions as needed with the search results

# Close the browser
driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





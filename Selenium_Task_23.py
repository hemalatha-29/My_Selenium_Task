#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install webdriver_manager


# In[6]:


pip install selenium --upgrade


# In[ ]:


pip uninstall selenium


# In[1]:


pip install selenium


# In[3]:


pip install --upgrade selenium


# In[ ]:


# using python selenium automation and action chains visit the url https://jqueryui.com/droppable/ and do a drag and drop operation of the white rectangular box in the yellow rectangular box?


# In[5]:


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  

# Open the URL
url = "https://jqueryui.com/droppable/"
driver.get(url)

# Wait for the iframe to be available
wait = WebDriverWait(driver, 10)
iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))
print("Switched to iframe successfully")

# Locate the draggable element within the iframe
draggable_element = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
print("Found draggable element")

# Locate the droppable element dynamically (using class name in this example)
droppable_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-droppable")))
print("Found droppable element")

# Perform the drag-and-drop operation using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Wait for a moment to observe the result (you can adjust the time as needed)
time.sleep(3)

# Switch back to the default content
driver.switch_to.default_content()

# Close the browser window
driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[48]:


from selenium import webdriver


driver = webdriver.Chrome()  


driver.get("https://www.saucedemo.com/")


username_input = driver.find_element("id", "user-name")
password_input = driver.find_element("id", "password")
login_button = driver.find_element("id", "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("standard_user")
login_button.click()

title = driver.title
print("Title:", title)

current_url = driver.current_url
print("Current URL:", current_url)


driver.quit()


# In[ ]:





# In[3]:


get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install requests')


# In[ ]:





# In[62]:


from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.saucedemo.com/"  


driver = webdriver.Chrome()


driver.get("https://www.saucedemo.com/")


driver.implicitly_wait(10)

content = driver.page_source


soup = BeautifulSoup(content, "html.parser")
text_content = soup.get_text()


print(text_content)


filename = "webpage_task_11.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(text_content)
    print(f"Text content saved to {filename}")


driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





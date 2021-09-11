#!/usr/bin/env python
# coding: utf-8

# In[169]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# In[170]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# In[171]:



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)


# In[172]:


outcome = False
while outcome != True:
    browser.get("https://www.seine-saint-denis.gouv.fr/booking/create/9845")
    assert "Pôle 'vie privée et familiale'" in browser.title
    
    checkbox = browser.find_element_by_name("condition")
    checkbox.send_keys(Keys.SPACE)
    checkbox.send_keys(Keys.TAB)
    checkbox.send_keys(Keys.RETURN)
    
    try:
        #Find the radio check for the month of september and click it.
        box2 = browser.find_element_by_id("planning18380")
        box2.click()
    except NoSuchElementException:
        continue
        
        #Confirm the choice and load the next page
        box2.send_keys(Keys.TAB)
        box2.send_keys(Keys.TAB)
        box2.send_keys(Keys.RETURN)
        
    try: 
        #Find the label with the result
        booking = browser.find_element_by_id("FormBookingCreate")
    except NoSuchElementException:
        continue
    
    #check for the outcome
    text = booking.get_attribute('innerText')
    print(text)
    
    if "Il n'existe plus de plage horaire" in text:
        outcome = False
    else: 
        outcome = True


# In[ ]:





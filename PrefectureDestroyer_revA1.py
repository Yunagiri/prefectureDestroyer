#!/usr/bin/env python
# coding: utf-8

# In[169]:

import asyncio
from desktop_notifier import DesktopNotifier
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# In[170]:


from selenium.webdriver.common.keys import Keys

async def notif(title, message):
    await notifier.send(title, message)

# In[171]:

notifier = DesktopNotifier()
#test 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--log-level=1")
browser = webdriver.Chrome(options=chrome_options)


# In[172]:

outcome = False

while outcome is not True:
    browser.get("https://www.rdv-prefecture.interieur.gouv.fr/rdvpref/reservation/demarche/3823/creneau/")
    try:
        captchaBox = browser.find_element("name", "captchaUsercode")
        asyncio.run(notif("CAPTCHA", "Veuillez entrer le captcha"))
        captcha = input("Entrer le captcha et appuyer sur entrée:\n")
        captchaBox.send_keys(captcha)
        captchaBox.send_keys(Keys.RETURN)
        counter = 0
    except NoSuchElementException:
        pass

        browser.get(browser.current_url)
        #Find the radio check for the month of september and click it.
        try : 
            button = browser.find_element("xpath", "//span[text()='Suivant']")
            if button.is_enabled():
                print("Bouton visible")
                href_data = button.get_attribute('href')
                if href_data is None:
                    is_clickable = False
                    print("Bouton non cliquable")
                    browser.refresh()
                    counter += 1
                    print("Compteur de rafracissement: ", counter)
                    sleep(30)      #changer le rafraichissement
                else:
                    asyncio.run(notif("RDV TROUVE,", "Veuillez entrer vos informations"))
                    button.click()
                    info = input("Entrez vos informations")
                # break
        except NoSuchElementException:
            browser.refresh()
            print("Navigateur rafraîchi")
            sleep(2)            






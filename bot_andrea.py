# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:13:00 2019

@author: Andrea Monserrat
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Expediente= "237002"
NIP="IZFHB9E56"
browser = webdriver.Chrome()
browser.get(("https://comunidad2.uaq.mx/portal/index.jsp"))

username = browser.find_element_by_id("clave")
username.send_keys(Expediente)
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "nip")))
password.send_keys(NIP)

KardexButton = browser.find_element_by_id("botonSubmit")
KardexButton.click()
KardexButton = browser.find_element_by_id("modulo4").click()
##Hasta ahí todo cool
#problemas:
#continuar_button = browser.find_element_by_xpath("""//section[@id='mainSection']/input[@value='Continuar >>']""")
#continuar_button.click()
#reimpresion=browser.find_element_by_xpath('//table[@style="width:100%;"]/td/a[@href="Reimprime.do?idDoc=178436"][@target="reimpresion"]')
#reimpresion.click()

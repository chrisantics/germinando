# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:25:57 2019

@author: Erika
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Expediente = '263045'
NIP = '3VPXAT8724'

browser = webdriver.Chrome()
browser.get("https://comunidad2.uaq.mx/portal/index.jsp")

    
usuario = browser.find_element_by_id('clave')
usuario.send_keys(Expediente)

element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "nip")))

password = browser.find_element_by_id('nip')
password.send_keys(NIP)

login = browser.find_element_by_id('botonSubmit')
login.click()

imp = browser.find_element_by_id('modulo1')
imp.click()
#Hasta aquí es la consulta escolar
boton = browser.find_element_by_xpath("//form[input/@onclick= 'Carrera.do']")
boton.click()

sig = browser.find_element_by_xpath(".//input[contains(@value, 'goTo('Siguiente >>')]")
sig.click()

kardex = browser.find_element_by_id('botonKARDEX')
kardex.click()

acep = browser.find_element_by_xpath(".//input[contains(@value, 'Aceptar >>')]")
acep.click()





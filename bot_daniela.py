#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:26:18 2019

@author: danyvargas
"""
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

Expediente="263037"
NIP="K1XEI4MWIG"


browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get(('https://comunidad2.uaq.mx/portal/index.jsp'))

usuario=browser.find_element_by_id('clave')
usuario.send_keys(Expediente)

password=browser.find_element_by_id('nip')
password.send_keys(NIP)

login= browser.find_element_by_id('botonSubmit')
login.click()

kard= browser.find_element_by_id('modulo1')
kard.click()

time.sleep(10)

close=browser.find_element_by_tag_name('body')
close.send_keys(CONTROL+ 'w')
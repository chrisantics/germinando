# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#Se cargan librerías
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Información para acceder
usernameStr = '236760'
passwordStr = 'Q8YYSXIK14'

#Se activa el navegador

browser = webdriver.Chrome("/home/cc/Descargas/chromedriver")
browser.get(('https://comunidad2.uaq.mx/portal/index.jsp'))

#Se rellena la información
username = browser.find_element_by_id('clave')
username.send_keys(usernameStr)

# contraseña =  password.send_keys (passwordStr) 
# signInButton = browser.find_element_by_id ('signIn' ) signInButton.click () 
password = WebDriverWait (browser, 10) .until (EC.presence_of_element_located ((By.ID, 'nip')))
password.send_keys(passwordStr)

#Se hace login
accederBoton = browser.find_element_by_id('botonSubmit')
accederBoton.click()

#Buscar Kardex
Kardex = browser.find_element_by_id('modulo3')
Kardex.click() 

pagina="https://comunidad2.uaq.mx/portal/index.jsp"


for p in pagina:
  if p==pagina[-10]:
       pagina=pagina.replace("index.jsp","cs?idm=3")
print(pagina)
browser.get((pagina))

pagina="https://comunidad2.uaq.mx/DocumentosOficiales/principal.jsp"
for p in pagina:
  if p==pagina[-10]:
       pagina=pagina.replace("principal.jsp","Reimprime.do?idDoc=181922")
print(pagina)
browser.get((pagina))

pagina="https://comunidad2.uaq.mx/DocumentosOficiales/principal.jsp"
browser.get((pagina))

accederBoton = browser.find_element_by_id('botonLogOut')
accederBoton.click()
pagina="https://comunidad2.uaq.mx/portal/index.jsp"
browser.get((pagina))

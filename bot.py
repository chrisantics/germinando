#Se cargan librerías
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Información para acceder
usernameStr = 'expediente'
passwordStr = 'nip'

#Se activa el navegador en modo automático
browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get(('https://comunidad2.uaq.mx/portal/index.jsp'))

#Se rellena la información
username = browser.find_element_by_id('clave')
username.send_keys(usernameStr)
password = browser.find_element_by_id('nip')
password.send_keys(passwordStr)

#Se hace login
accederBoton = browser.find_element_by_id('botonSubmit')
accederBoton.click()

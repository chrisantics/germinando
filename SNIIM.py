# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:45:09 2019

@author: Erika
"""
import pandas as pd
import arrow
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#página inicial
browser = webdriver.Chrome()
browser.get(("http://www.economia-sniim.gob.mx/nuevo/"))
#página secundaria
pagina="http://www.economia-sniim.gob.mx/nuevo/"
for p in pagina:
        if p==pagina[-1]:
            pagina+="/Consultas/MercadosNacionales/PreciosDeMercado/Agricolas/ConsultaFrutasYHortalizas.aspx?SubOpcion=4"
browser.get((pagina))

#Abrir opciones de Destinos
DestinoButton= browser.find_element_by_id("ddlDestino").click()

#Seleccionar Querétaro "220" 
SelectionButton = browser.find_element_by_xpath("//select[@name='ddlDestino']/option[@value='220']").click()

#Abrir calendario fecha de inicio
CalendarioButtonI=browser.find_element_by_id("txtFechaInicio").clear()
CalendarioButtonI=browser.find_element_by_id("txtFechaInicio").click()
#seleccionar día
FechaI=arrow.now().format('DD/MM/YY')
CalendarioButtonI=browser.find_element_by_id("txtFechaInicio").send_keys(FechaI)

#Abrir calendario fecha final
CalendarioButtonF=browser.find_element_by_id("txtFechaFinal").clear()
CalendarioButtonF=browser.find_element_by_id("txtFechaFinal").click()
#seleccionar día
FechaF=arrow.now().format('DD/MM/YY')
CalendarioButtonF=browser.find_element_by_id("txtFechaFinal").send_keys(FechaF)

#Botón buscar
BuscarButton=browser.find_element_by_id("btnBuscar")
BuscarButton.click()

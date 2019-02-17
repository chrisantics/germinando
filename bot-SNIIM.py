# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:27:35 2019

@author: Andrea Monserrat
"""
import arrow
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#Abrir primera pagina:
browser = webdriver.Chrome()
browser.get(("http://www.economia-sniim.gob.mx/nuevo/"))
#Abrir segunda pagina:
pagina="http://www.economia-sniim.gob.mx/nuevo/"
for p in pagina:
        if p==pagina[-1]:
            pagina+="/Consultas/MercadosNacionales/PreciosDeMercado/Agricolas/ConsultaFrutasYHortalizas.aspx?SubOpcion=4"
browser.get((pagina))
#Seleccionar mercado
DestinoButton = browser.find_element_by_id("ddlDestino").click()
SelecionButton = browser.find_element_by_xpath("//select[@name='ddlDestino']/option[@value='220']").click()
#Especificar la fecha:
#Abrir calendario fecha de inicio
CalendarioButton=browser.find_element_by_id("btnCalendarioFI").clear()
CalendarioButton=browser.find_element_by_id("btnCalendarioFF").click()
Fecha0=arrow.now().format("DD/MM/YY")
CalendarioButton=browser.find_element_by_id("txtFechaInicio").send_keys(Fecha0)
#Abrir calendario fecha final
CalendarioButton=browser.find_element_by_id("btnCalendarioFF").clear()
CalendarioButton=browser.find_element_by_id("btnCalendarioFF").click()
Fecha1=arrow.now().format("DD/MM/YY")
CalendarioButton=browser.find_element_by_id("txtFechaInicio").send_keys(Fecha1)
#Botón buscar
BuscarButton = browser.find_element_by_id("btnBuscar").click()
#Descargar tabla:
#table= "//table[@id='tblResultados']//tr//td[child::a|text()]"

#xpath = "//table[@class='tbldata14 bdrtpg']//tr//td[child::a|text()]"
#como descargar datos de tabla html
#("//select[@name='element_name']/option[text()='option_text']")
#driver.findElement(By.xpath("//*[@name='action'][@value='Go']")).click()



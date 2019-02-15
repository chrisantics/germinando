# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:02:12 2019

@author: Erika
"""

import pandas as pd
import arrow
from selenium import webdriver
import datetime

start = datetime.datetime.strptime("21/06/2014", "%d/%m/%Y")
end = datetime.datetime.strptime("07/07/2014", "%d/%m/%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    print(date.strftime("%d/%m/%Y")) 
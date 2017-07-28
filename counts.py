#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:01:09 2017

@author: yajun
"""

import pandas as pd
import json

filename = '/home/yajun/Samba/ecvv/test.xlsx'
file = pd.read_excel(filename)

filename = '/home/yajun/Samba/ecvv/country.json'
contry = pd.read_json(filename)

with open(filename) as json_file:
    data = json.load(json_file)
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

BASE='http://www.ecvv.com'

filename='u_ex170703_x.log'
df = pd.read_table(filename,header=0,encoding='gb2312',delim_whitespace=True, skiprows = 3,usecols=['cs-uri-stem', 'cs-uri-query','c-ip-1','date', 'time']) #usecols=['cs-uri-stem', 'cs-uri-query','c-ip-1','date', 'time']

# group by col
result = df.groupby('cs-uri-stem').size().sort_values(ascending=False).reset_index(name='count')
product = result[result['cs-uri-stem'].str.contains('^\/product\/')]
#url = list()
#for stem in product['cs-uri-stem'].values:
#    urlstr = (BASE+stem)
#    url.append(urlstr)
#product['cs-uri-stem'] = url

product.head(65000).to_excel("stem_product.xlsx")

company = result[result['cs-uri-stem'].str.contains('^\/company\/')]
company.head(65000).to_excel("stem_company.xlsx")


result = df.groupby('cs-uri-query').size().sort_values(ascending=False).reset_index(name='count')
result.to_excel("query.xlsx")

result = df.groupby('c-ip-1').size().sort_values(ascending=False).reset_index(name='count')
result.to_excel("c_ip.xlsx")

cip = pd.read_excel('c_ip.xlsx')
cip_list = cip['c-ip-1']

for ip in cip_list:
    print('get cip: %s'%(ip))

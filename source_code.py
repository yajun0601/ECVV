#!/usr/bin/env python3

import pandas as pd

# delete beginning 
lines = open('u_ex170703_x.log').readlines()
open('newfile1.txt', 'w').writelines(lines[4:-1])

# add headers
user_cols = ['date', 'time', 's-ip', 'cs-method', 'cs-uri-stem', 'cs-uri-query', 's-port', 'cs-username', 'c-ip', 'cs(User-Agent)', 'cs(Referer)', 'sc-status', 'sc-substatus', 'sc-win32-status', 'time-taken', 'c-ip-1']
# parce columns
df = pd.read_table('newfile1.txt', sep=" ", names = user_cols)

# group by col
result = df.groupby('c-ip-1').size().sort_values().reset_index(name='count')

# write dataframe in a text file
f = open("file.txt", "w")
result.to_csv(f)
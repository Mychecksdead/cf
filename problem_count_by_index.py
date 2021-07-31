import requests as rq
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import json
url = 'https://codeforces.com/api/'
def printt(r, param, cond='-1', condp='-1', s='-1', returndata=0):
   data = []
   for _ in r.json()['result']:
      if cond == '-1' or _[condp] == cond:
        if s == '-1':
          if returndata == 0:
            print(_[param])
          else:
            data.append(_[param])
        else:
          if returndata == 0:
            print(_[s][param])
          else:
            data.append(_[s][param])
   if returndata == 1:
      return data

def creq(r):
  if r.status_code == 500:
    print('Connection failed...')

r = rq.get(url+'contest.list')
# for _ in r.json()['result']:
  # print(_['id'])
r.json()['result'][0]

handle = input('Enter handle: ')
# handle = 'mychecksdead'
r = rq.get(url+'user.status?handle='+handle)
creq(r)
data = printt(r, 'index', 'OK', 'verdict', 'problem', 1)
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
arr = np.zeros([8], dtype='uint64')
data = np.array(data)
data = pd.DataFrame(data)

for i in range(8):
   arr[i] = data.loc[data[0] == labels[i]].count()[0]

plt.bar(labels, arr)
plt.title('Submissions of ' + handle + ' by Indexes')
plt.xlabel('Index')
plt.ylabel('Count')
plt.yticks(np.arange(0, (np.max(arr)+9)//10*10+10, 10))
style.use('seaborn')

plt.show()
import requests as rq
import matplotlib.pyplot as plt
from matplotlib import style # Sometimes normal usage didn't worked.
import pandas as pd
import numpy as np
import json
import sys
url = 'https://codeforces.com/api/'
plt.style.use(['default', 'seaborn-darkgrid'])


def creq(r): #check request
    if r.status_code != 200:
        print('Connection failed...')
        sys.exit()


r = rq.get(url+'contest.list')
creq(r)
# for _ in r.json()['result']:
  # print(_['id'])
# print(r.json()['result'][0])

handle = input('Enter handle: ')
r = rq.get(url+'user.status?handle='+handle)
creq(r)

data = []
for _ in r.json()['result']:
    if _['verdict'] == 'OK':
        data.append(_['problem']['index'])

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

plt.show()
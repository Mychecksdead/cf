import requests as rq
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
url = 'https://codeforces.com/api/'
plt.style.use(['default', 'seaborn-darkgrid'])


def creq(r): #check request
    if r.status_code != 200:
        print('Connection failed...')
        sys.exit()

handle = input('Enter handle: ')
r = rq.get(url+'user.status?handle='+handle)
creq(r)
# print(r.json()['result'][2]['problem'])

data = []
for _ in r.json()['result']:
    if _['verdict'] == 'OK' and 'rating' in _['problem']:
        data.append(_['problem']['rating'])

labels = np.arange(800, max(data)+200, 100)
arr = np.zeros([len(labels)], dtype='uint64')
data = np.array(data)
data = pd.DataFrame(data)

for i in range(len(labels)):
    arr[i] = data.loc[data[0] == labels[i]].count()[0]

plt.bar(labels, arr, width=100)
plt.title('Submissions of ' + handle + ' by Ratings')
plt.xlabel('Index')
plt.ylabel('Count')

plt.yticks(np.arange(0, (np.max(arr)+9)//10*10+10, 10))

plt.show()
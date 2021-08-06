from matplotlib import colors
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
        data.append([_['problem']['rating'], _['problem']['name']])



colors = ['#cccccc', '#cccccc', '#cccccc', '#cccccc', '#77ff77', '#77ff77',
'#77ddbb', '#77ddbb', '#aaaaff', '#aaaaff', '#aaaaff', '#ff88ff', '#ff88ff',
'#ffcc88', '#ffcc88', '#ffbb55', '#ff7777', '#ff7777', '#ff3333', '#ff3333', '#ff3333', '#ff3333',
'#aa0000', '#aa0000', '#aa0000', '#aa0000', '#aa0000', '#aa0000']

problems = {}
max_rating = 800
for i in range(800, 3600, 100):
    problems[i] = {}
for problem in data:
    problems[problem[0]][problem[1]] = 1
    max_rating = max(max_rating, problem[0])
labels = np.arange(800, max_rating+200, 100)
arr = []


for r in labels:
    if r <= max_rating:
        arr.append(len(problems[r]))
    else:
        arr.append(0)

arr = np.array(arr)


plt.figure(figsize = (10, 6))
plt.bar(labels, arr, color=colors, width=75)
plt.title('Solved Problems of ' + handle + ' by Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')

mx = np.max(arr)
x = 10 if mx < 100 else 20


plt.yticks(np.arange(0, (mx/x + 2) * x, x))

plt.show()
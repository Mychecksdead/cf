import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import amax
import pandas as pd
import requests as rq
import time
import datetime
current_date = datetime.date.today()
url = 'https://codeforces.com/api/'
plt.style.use(['default', 'seaborn-darkgrid'])

def creq(r): #check request
    if r.status_code != 200:
        print('Connection failed...')
        sys.exit()

def convert(unix):
    year = int(time.ctime(unix).split()[4])
    dt = datetime.datetime(year, 1, 1)
    timestamp = (time.mktime(dt.timetuple()))
    return (unix-timestamp)/31536000+year
handle = input('Enter handle : ')
times = {}

r = rq.get(url + 'user.rating?handle=' + handle)
creq(r)
contests = rq.get(url + 'contest.list?gym=false')
creq(contests)

# print(contests.json()['result'][0])
# print(r.json()['result'][0])

for contest in contests.json()['result']:
    times[contest['id']] = contest['startTimeSeconds']

data = []
t = []
for rating in r.json()['result']:
    data.append(rating['newRating'])
    t.append(convert(times[rating['contestId']]))

min_year = int(time.ctime(times[r.json()['result'][0]['contestId']]).split()[4])
max_year = current_date.year


data = np.array(data)
t = np.array(t)

plt.figure(figsize=(10, 5), dpi=100)

plt.plot(t, data, linewidth=1, color='#000000', marker='.', markersize=11)

plt.title('Rating graph of ' + handle, fontsize=30)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Rating', fontsize=20)

plt.xticks(np.arange(min_year, max_year+2, 1))

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import requests as rq
import time
import datetime
import sys


def creq(r):  #check request
    if r.status_code != 200:
        print('Connection failed...')
        sys.exit()


def convert(unix):
    year = int(time.ctime(unix).split()[4])
    dt = datetime.datetime(year, 1, 1)
    timestamp = (time.mktime(dt.timetuple()))
    return (unix-timestamp)/31536000+year

def get_handles():
    handles = input('Enter handle : ').split()
    return handles



url = 'https://codeforces.com/api/'
contests = rq.get(url + 'contest.list?gym=false')
creq(contests)
current_date = datetime.date.today()


plt.style.use(['default', 'seaborn-darkgrid'])
max_year = current_date.year



def process(handle, index, min_year):
    r = rq.get(url + 'user.rating?handle=' + handle)
    creq(r)
    times = {}
    
    for contest in contests.json()['result']:
        times[contest['id']] = contest['startTimeSeconds']

    data = []
    t = []
    for rating in r.json()['result']:
        data.append(rating['newRating'])
        t.append(convert(times[rating['contestId']]))

    min_year = min(min_year, int(time.ctime(times[r.json()['result'][0]['contestId']]).split()[4]))

    data = np.array(data)
    t = np.array(t)


    plt.plot(t, data, linewidth=1, marker='.', markersize=6, label=handle)
    return min_year


def main():
    handles = get_handles()
    plt.figure(figsize=(10, 5), dpi=100)
    min_year = max_year
    for _user in range(len(handles)):
        min_year = min(min_year, process(handles[_user], _user, min_year))
    plt.xlabel('Time', fontsize=20)
    plt.ylabel('Rating', fontsize=20)
    plt.xticks(np.arange(min_year, max_year+2, 1))
    plt.legend()
    plt.show()

main()
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
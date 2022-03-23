from time import sleep
import pandas as pd
import requests
import time
import matplotlib.pyplot as plt
from datetime import datetime


cnt = 0

block_rate_dict = dict(
    blocks=[],
    block_rate=[],
    request_time=[]
)

while True:
    res = requests.get(
        'https://ic-api.internetcomputer.org/api/metrics/block-rate').json()
    blocks = res['block_rate'][0][0]
    block_rate = float(res['block_rate'][0][1])
    block_rate_dict['block_rate'].append(block_rate)
    block_rate_dict['blocks'].append(blocks)
    block_rate_dict['request_time'].append(time.time())

    cnt += 1

    if cnt % 1 == 0:
        df = pd.DataFrame(block_rate_dict)
        df.to_csv('record.csv')
    sleep(1)

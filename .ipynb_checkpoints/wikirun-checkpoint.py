#! /usr/bin/env python3

import requests
import json
from datetime import date, timedelta
from random import randint

def get_random_date():
    min_date = date(2016,1,1)
    max_date = date.today()
    delta = timedelta(days = randint(0, (max_date - min_date).days - max_date.day - 1))
    rand_date = min_date + delta
    return {'year':rand_date.strftime('%Y'), 'month':rand_date.strftime('%m')}

if __name__ == "__main__":
    headers = {'User-Agent':'wikirn/0.1','accept':'application/json'}
    t_date = get_random_date()
    url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia.org/all-access/{t_date["year"]}/{t_date["month"]}/all-days'
    res = requests.get(url, headers=headers)
    data = res.json()
    for x in data["items"][0]:
        print(x)
        print('-----------------------------------------')
        print('=========================================')

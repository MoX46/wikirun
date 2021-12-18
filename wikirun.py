#! /usr/bin/env python3

import requests
import json
from datetime import date, timedelta
from random import randint
import re

def get_random_date():
    min_date = date(2016,1,1)
    max_date = date.today()
    delta = timedelta(days = randint(0, (max_date - min_date).days - max_date.day - 1))
    rand_date = min_date + delta
    return {'year':rand_date.strftime('%Y'), 'month':rand_date.strftime('%m')}

def get_article(articles):
    blacklist = ['Main_Page','^(.+):']
    target_article = articles[randint(0, len(articles))]
    for re_pattern in blacklist:
        if re.search(re_pattern, target_article['article']):
            ret = get_article(articles)
        else:
            ret = target_article 
    return ret


if __name__ == "__main__":
    headers = {'User-Agent':'wikirn/0.1','accept':'application/json'}
    target_date = get_random_date()
    url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia.org/all-access/{target_date["year"]}/{target_date["month"]}/all-days'
    res = requests.get(url, headers=headers)
    data = res.json()
    articles = data['items'][0]['articles']
    pg1 = get_article(articles)
    pg2 = get_article(articles)


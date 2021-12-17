#! /usr/bin/env python3

import requests
import json

if __name__ == "__main__":
    headers = {'User-Agent':'wikirn/0.1','accept':'application/problem+json'}
    year = '2015'
    month = '11'
    url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia.org/all-access/{year}/{month}/all-days'

    r = requests.get(url, headers=headers)
    print(r.text)

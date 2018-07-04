# -*-coding=utf-8-*-

# author:Alpine

# python3

import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    try:
        response = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('')


def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()



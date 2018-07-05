# -*-coding=utf-8-*-

# author:Alpine

# python3
import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re

'''
request方式模拟网页链接请求
'''
def get_one_page(url):
    try:
        response = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

'''
用正则表达式筛选解析到数据
'''
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'+'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'+'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield  {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'star': item[3].strip()[3:],
            'releaseTime': item[4],
            'score': item[5] + item[6]
        }

'''
将筛选结果存入result.txt文件中
'''
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()



'''
爬取网页链接所有页面数据循环
'''
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


'''
线程循环爬取数据
'''
if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
    pool.close()
    pool.join()



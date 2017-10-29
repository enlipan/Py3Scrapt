# -*- coding: UTF-8 -*-

import sys
import webbrowser

import requests
import bs4

if __name__ == '__main__':
    print('google...')

    info = input('input search info...\n')

    res = requests.get('https://www.google.com/search?q=' + ' ' + info)  # ' '.join(sys.argv[1:]) join 函数 链接序列数组
    res.raise_for_status()

    # retrieve top search result
    if res.status_code == requests.codes.ok:
        soup = bs4.BeautifulSoup(res.text)
        # 分析 html 数据获取对应 class 或者其他属性信息 select 获取

        # open browser for each result
        # 打开指定的 href 链接信息
        webbrowser.open('')

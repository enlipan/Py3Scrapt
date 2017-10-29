# -*- coding: UTF-8 -*-

# 获取当前页面内容,得到前一页的跳转链接,进一步循环获取前一页内容,进而再次获取上一页链接
# 当前页
# 前一页
# 下载当前页面内容

import os

import bs4
import requests
import multiprocessing
from multiprocessing import Process

baseXkcdUrl = 'https://xkcd.com/'


def downloadImg(imgUrl):
    print(str(multiprocessing.current_process()) + ' img is => ' + imgUrl)
    if not os.path.exists('xhcd'):
        os.mkdir('xhcd')

    imgFile = open(os.path.join('xhcd', os.path.basename(imgUrl)), 'wb+')

    imgRes = requests.get(imgUrl)
    imgRes.raise_for_status()
    for chunk in imgRes.iter_content(100000):
        imgFile.write(chunk)

    imgFile.close()


def scrapXkcd(baseUrl):
    res = requests.get(baseUrl)
    res.raise_for_status()
    content = res.text
    sou = bs4.BeautifulSoup(content, 'lxml')

    # prev  ref 属性  url  value  1906  => 相对路径   拼接 url http://xkcd.com/1906/
    # <li><a rel="prev" href="/1907/" accesskey="p">&lt; Prev</a></li>
    prevElem = sou.select('li > a[rel="prev"]')
    if not prevElem == []:
        prevElemLink = prevElem[0].get('href')
        multiProcessScrap('http://xkcd.com' + prevElemLink)

    # img id = 'comic'
    # tag 标签逐级寻找
    comicElem = sou.select('#comic img')
    if not comicElem == []:
        # download //imgs.xkcd.com/s/a899e84.jpg
        downloadImg(('http:' + comicElem[0].get('src')))


def multiProcessScrap(baseUrl):
    pro = Process(target=scrapXkcd, args=(baseUrl,))
    pro.start()


# 分析: 爬虫本质是人工的模拟,人类可以肉眼识别什么是图标,什么是文本等等,从而点击右键鼠标,另存为本地
# 那么如何让计算机,一张张图片持续下载?
# 核心的问题就在于: 打开网页,分析网页内容组成(找到目标内容的规律),告诉程序要下载什么内容(什么才是目标),最后下载目标内容

if __name__ == '__main__':
    # scrapXkcd(baseXkcdUrl)
    multiProcessScrap(baseXkcdUrl)

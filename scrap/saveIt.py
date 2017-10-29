import requests
import os

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()

try:
    playFile = open('caches/juliet.txt', 'wb+')  # w+
except Exception as exe:
    os.mkdir('caches')  # 注意相对路径与绝对路径
    # os.system('mkdir caches')
    playFile = open('caches/juliet.txt', 'wb+')
    # chmod a+w

# read info from res and save info to file
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

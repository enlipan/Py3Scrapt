import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

type(res)

print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

res = requests.get('http://inventwithpython.com/page_not_exist')

try:
    res.raise_for_status()  # 失败时立即停止
except Exception as exc:
    print('Exception is %s', exc)

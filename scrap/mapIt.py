# -*- coding: utf-8 -*-

import webbrowser
import sys
import pyperclip

# 利用系统浏览器打开 url
if __name__ == '__main__':
    print(sys.argv[0])  # module name
    print(sys.argv[1])
    address = ''
    if len(sys.argv) > 1:
        address = sys.argv[1]
    else:
        address = pyperclip.paste()
    webbrowser.open(address)

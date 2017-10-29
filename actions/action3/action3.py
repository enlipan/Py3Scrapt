# -*- coding: UTF-8 -*-

# selenuim 模块

import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

folder = 'bugtags'
bugtagsBugUrl = 'https://work.bugtags.com/apps/1542817734197397/issues/1582377118729453/tags/1582377118731195?members=1542876607545594'


def getChrome():
    # download 驱动版本  http://blog.csdn.net/huilan_same/article/details/51896672
    # http://chromedriver.storage.googleapis.com/index.html
    # 不正确的驱动版本导致  raise RemoteDisconnected("Remote end closed connection without"
    driverLocation = '/usr/local/bin/chromedriver'
    return webdriver.Chrome(driverLocation)


def loadCookies():
    return pickle.load(open(os.path.join(folder, 'cookies.pkl'), 'rb'))


def loginBugtags():
    browser = getChrome()
    # chrome 使用 其他账户
    browser.get('https://work.bugtags.com/apps/1542817734197397/issues')
    elemEmail = browser.find_element_by_id('login_email')
    elemEmail.send_keys('lipan')
    elemPwd = browser.find_element_by_id('login_pwd')
    elemPwd.send_keys('pwd')
    # elemPwd.submit() 等同执行所在表单的 submit
    btnLogin = browser.find_element_by_id('btn_login')
    btnLogin.click()
    # 键盘特殊按键
    # from selenium.webdriver.common.keys import Keys
    # html = browser.find_element_by_tag_name('html')
    # html.send_keys(Keys.END)
    return browser


def saveCookies(driver):
    if not os.path.exists(folder):
        os.mkdir(folder)
    pickle.dump(driver.get_cookies(), open(os.path.join(folder, 'cookies.pkl'), 'wb'))
    pass


def toDetailInfo(driver):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'tab_dd'))
        )
        element.click()
    except Exception as e:
        print(e.strerror)
        driver.quit()


def checkCookiesWithRequest(cookies):
    import requests
    s = requests.session()
    headers = \
        {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        }
    s.headers = headers
    for cookie in cookies:
        for key in cookie.keys():
            s.cookies.set(key, cookie[key])
    res = s.get(bugtagsBugUrl)
    print(res.text)


def toDetailBugTagsInfo(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.title_contains('大风车')
        )
        # time.sleep(3) 最笨重的方式
        driver.get(bugtagsBugUrl)
    except Exception as e:
        print(e.strerror)
        driver.quit()


def print(obj):
    from pprint import pprint
    pprint(obj)


if __name__ == "__main__":
    browser = loginBugtags()

    toDetailBugTagsInfo(browser)

    saveCookies(browser)
    cookies = loadCookies()
    print(cookies)
    # checkCookiesWithRequest(cookies)

    toDetailInfo(browser)
    browser.quit()

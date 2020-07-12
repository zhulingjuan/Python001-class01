from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://github.com/Python001-class01/Python001-class01/issues/25')
    time.sleep(1)

    btm1 = browser.find_element_by_xpath('//*[@id="js-progressive-timeline-item-container"]/form/div/div/button[2]')
    while True:
        try:
            btm1 = browser.find_element_by_xpath('//*[@id="js-progressive-timeline-item-container"]/form/div/div/button[2]')
            btm1.click()
            time.sleep(10)
        except Exception as e:
            break    

    
    cookies = browser.get_cookies() # 获取cookies

    
    bs_info = bs(browser.page_source, 'html.parser')

    count1 = 0
    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    for tags in bs_info.find_all('td', attrs={'class': 'js-comment-body'}):
        text = tags.find('p').text
        if text.find("3班") == -1: 
            continue
        if text.find("5组") == -1:
            continue        
        count = count+1

    print(count)

    #print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()
    
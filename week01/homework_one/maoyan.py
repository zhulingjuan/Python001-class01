# 使用BeautifulSoup解析网页

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
# bs4是第三方库需要使用pip命令安装




user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

Cookie = '__mta=143547274.1593266422635.1593283558067.1593285636999.30; uuid_n_v=v1; uuid=89B2ADC0B87E11EA80F64D80EBA969F73AA3FE036ADB41CE9C408BF4E92E9FB3; _csrf=1d5301085108361c5f13cec05a41aab4c8bf42f08e093ef5b2a637ae78e385a7; mojo-uuid=9dfc62d29abe31cfca81d46f99f2d969; _lxsdk_cuid=172f6144329c8-0e20cfa8fe5329-31657402-1ea000-172f6144329c8; _lxsdk=89B2ADC0B87E11EA80F64D80EBA969F73AA3FE036ADB41CE9C408BF4E92E9FB3; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593266422,1593266486,1593282850; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-session-id={"id":"7537f3c81e43ac80dda2a10db787d287","time":1593285635987}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593285638; __mta=143547274.1593266422635.1593285636999.1593285637688.31; _lxsdk_s=172f7396aae-be9-209-a15%7C%7C5'


header = {
    'user-agent':user_agent,
    'Cookie':Cookie
 }

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
print(response.text)
bs_info = bs(response.text, 'html.parser')

mylist = []
# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    # 电影名称
    film_name = tags.find('span', attrs={'class': 'name'}).text
    print(f'上映日期: {film_name}')

    # 电影类型
    movie_type = tags.find_all('div', attrs={'class': 'movie-hover-title'})[1].text
    # 上映时间
    plan_date = tags.find_all('div', attrs={'class': 'movie-hover-brief'})[0].text
    mylist = [film_name, movie_type, plan_date]
    movie1 = pd.DataFrame(data = mylist)
    # windows需要使用gbk字符集
    movie1.to_csv('./movie1.csv', encoding='utf8', index=True, header=False)









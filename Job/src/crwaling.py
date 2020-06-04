from selenium import webdriver
import pandas as pd
from datetime import datetime

driver = webdriver.Chrome('./chromedriver')

# url에 접근한다.

url_list = []
indus_list = []
# 280
n = 1
for num in range(1, 280):
    num = str(num)
    url = 'http://www.jobkorea.co.kr/starter/spec?IsFavorOn=0&IsAlumniOn=0&Page=' + num
    
    driver.implicitly_wait(3)
    driver.get(url)
    
    for i in range(1, 11):
        i = str(i)
        try:
            # temp = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[4]/ul/li['+ i +']/div[2]/dl/dt/a[1]').get_attribute("href")
            # url_list.append(temp)

            industry = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[4]/ul/li['+ n +']/div[2]/dl/dd[1]/span')
            indus_list.append(industry)
            n += 1
        except:
            pass

# print(url_list)

# df_url = pd.DataFrame(url_list)
# # print(df_url.columns)

# df_url.to_csv('./raw_data/url_list.csv', index=False)

now = datetime.now()  # 파일이름 현 시간으로 저장하기
outputFileName = '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)

df_ind = pd.DataFrame(indus_list)
df_ind.to_csv('./raw_data/' + outputFileName, index=False)

from selenium import webdriver
import pandas as pd
from datetime import datetime
import time


now = datetime.now()  # 파일이름 현 시간으로 저장하기
outputFileName = '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)



driver = webdriver.Chrome('./kakao/chromedriver')
url = 'https://www.catch.co.kr/Comp/CompMajor?flag=Search'

driver.get(url)
x = 1

# IT 산업 선택
driver.find_element_by_xpath('//*[@id="chkJinhakCodeViewE"]').click()
# 검색 클릭
time.sleep(1)
driver.find_element_by_xpath('//*[@id="imgSearch"]').click()
view_url = []
pn = 2

count = 1
try:
    while x:
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="Contents"]/p[3]/a['+ str(pn) +']').click() 
        for i in range(1, 12):
            # url 가져오기
            if i == 6:
                pass
            else:
                time.sleep(0.3)
                sub_url1 = driver.find_element_by_xpath('//*[@id="updates"]/tbody/tr['+ str(i) +']/td[1]/dl/dt[2]/a').get_attribute("href")
                sub_url2 = driver.find_element_by_xpath('//*[@id="updates"]/tbody/tr['+ str(i) +']/td[2]/dl/dt[2]/a').get_attribute("href")
                view_url.append(sub_url1)
                view_url.append(sub_url2)
        pn += 1
        count += 1
        if pn == 12:
            pn = 2
        if count == 20:
            x = 0
except:
    pass

# 페이지 넘기기
# driver.find_element_by_xpath('//*[@id="Contents"]/p[3]/a['+ str(i) +']').click() 

print(view_url)

print(len(view_url))



df_ind = pd.DataFrame(view_url)
df_ind.to_csv('./kakao/raw_data/' + outputFileName, index=False, encoding='utf-8-sig')

from selenium import webdriver
import pandas as pd
from datetime import datetime
import time


now = datetime.now()  # 파일이름 현 시간으로 저장하기
outputFileName = '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)

driver = webdriver.Chrome('./kakao/chromedriver')

df_url = pd.read_csv('./kakao/raw_data/2020-6-8  16시 47분.csv')
df_url = df_url['0']

for i in df_url:    
    url = i
    driver.get(url)

    company = driver.find_element_by_xpath('//*[@id="Contents"]/div[1]/div[1]/div[1]/div[2]/h2').text
    indus = driver.find_element_by_xpath('//*[@id="Contents"]/div[1]/div[1]/div[1]/div[2]/p/span[2]').text
    size = driver.find_element_by_xpath('//*[@id="Contents"]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[1]').text
    sales = driver.find_element_by_xpath('//*[@id="Contents"]/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[1]/text()[1]').text
    profit = driver.find_element_by_xpath('//*[@id="Contents"]/div[2]/div[1]/div[1]/table/tbody/tr[4]/td[1]/text()[1]').text
    employee = driver.find_element_by_xpath('//*[@id="Contents"]/div[2]/div[1]/div[1]/table/tbody/tr[5]/td[1]').text
    


    time.sleep(0.1)
    # driver.find_element_by_xpath('//*[@id="Contents"]/div[1]/div[1]/div[2]/ul/li[2]/a/img').click()
    
    time.sleep(3)
    # detail = driver.find_element_by_xpath('//*[@id="Contents"]/div[4]/div[2]/div[2]').text

    # info = [company, indus, tbody, detail]

    # print(info)

from selenium import webdriver
import pandas as pd
from datetime import datetime
import time
import sys

now = datetime.now()  # 파일이름 현 시간으로 저장하기
outputFileName = '%s-%s-%s  %s시 %s분.csv' % (
    now.year, now.month, now.day, now.hour, now.minute)


cop = ['NIKE', 'JP MORGAN', 'COCA COLA', 'global net lease', 'aapl', 'starbucks', 'at&t',
'master card', 'p&g', 'OHI', 'COST', 'VZ', 'Morgan stanley', 'MSFT', 'visa', 'JNJ', 'macdonald', 'boeing', 'bank of america', 'pepsico', 'walmart',
'intel', 'wells fargo', 'honeywell international', 'dominos', 'qcom', 'blackrock', 'gild', 'mmm',
'unh', 'amgn', 'hd', 'adi', 'rost', 'swks', 'k', 'el', 'gs', 'dis', 'o', 'spy', 'ivv', 'voo',
'qqq', 'div', 'soxx', 'xlf', 'ibb', 'vig', 'ewq', 'arkq']

driver = webdriver.Chrome('./chromedriver')
url = "http://www.google.co.kr"
driver.get(url)

n = len(cop)
print(n)

temp = dict()
try:
    for i, j in enumerate(cop):

        elem = driver.find_element_by_name("q")
        query = j + ' stock'
        time.sleep(0.2)
        elem.clear()
        elem.send_keys(query)
        elem.submit()

        stock_name = driver.find_element_by_xpath(
            '//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[1]/div/div[1]').text
        market_stock_code = driver.find_element_by_xpath(
            '//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/div[1]/div/div[2]').text
        stock_code = market_stock_code.split(':')[1]
        market_code = market_stock_code.split(':')[0]
        
        today_close = driver.find_element_by_xpath(
            '//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span[1]').text
        dividen_ratio = driver.find_element_by_xpath(
            '//*[@id="knowledge-finance-wholepage__entity-summary"]/div/div/g-card-section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]').text
        market_cap = driver.find_element_by_xpath(
            '//*[@id="knowledge-finance-wholepage__entity-summary"]/div/div/g-card-section[2]/div/div/div[1]/table/tbody/tr[4]/td[2]').text
        per = driver.find_element_by_xpath(
            '//*[@id="knowledge-finance-wholepage__entity-summary"]/div/div/g-card-section[2]/div/div/div[1]/table/tbody/tr[5]/td[2]').text

        info_list = [market_code, stock_name, stock_code, today_close, dividen_ratio, market_cap.replace('억', '').replace('조', '').replace('-', '0'), per]

        temp[n] = info_list
        n += 1
except EOFError as error:
    # Output expected EOFErrors.
    print(error)
except Exception as exception:
    # Output unexpected Exceptions.
    print(exception)



stock_df = pd.DataFrame(temp)
stock_df = stock_df.T
stock_df.columns = ['market_code', 'stock_name', 'stock_code', 'today_close', 'dividen_ratio', 'market_cap', 'per']

# df_ind = pd.DataFrame(indus_list)
# df_ind.to_csv('./raw_data/' + outputFileName, index=False)

stock_df.to_csv('./raw_data/' + outputFileName, index=False, encoding='utf-8-sig')

from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('./chromedriver')

df = pd.read_csv('./url_list.csv')
df2 = df['0']
print(df2.head())

url_list = []
for url in df2:
    driver.implicitly_wait(3)
    driver.get(url)
    x = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/ul').text
    print(x)


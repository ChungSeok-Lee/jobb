from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('../chromedriver')

df = pd.read_csv('../raw_data/url_list.csv')
df2 = df['0']
# print(df2.head())


features = ['grade', 'toeic', 'speaking', 'opic', 'cert', 'abr', 'inte', 'prize', 'vol']
# globals()['{}'.format(features[])] = df
print(features[0])


# all_body = []

# title = []

# grade = []
# toeic = []
# speaking = []
# opic = []
# cert = []
# abr = []
# inte = []
# prize = []
# vol = []

# major = []

# for url in df2[:1]:
#     # print(url)
#     driver.implicitly_wait(3)
#     time.sleep(1)
#     driver.get(url)

#     company = driver.find_element_by_xpath('//*[@id="devPassSpecForm"]/div/h2/strong/a').text
#     title.append(company)

#     spec = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/ul').text
#     specs = spec.split('\n')


#     college = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/ol[4]').text
#     colleges = college.split('\n')


#     driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[2]/a').click()
#     upSpec = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div/ul').text
#     upSpecs = upSpec.split('\n')

#     for i, j in enumerate(specs):
#         word = j
#         if '보유' in str(word):
#             specs.remove(word)
#     print(specs)
#     n = 0
#     for idx, fea in enumerate(specs):
#         if idx%2 != 0:
#             globals()['{}'.format(features[n])] = []
#             globals()['{}'.format(features[n])].append(fea)
            
#             n += 1

#         else:
#             pass
    



# print(grade)








# df_body = pd.DataFrame(all_body)
# df_body.to_csv('../raw_data/url_list.csv', index=False)
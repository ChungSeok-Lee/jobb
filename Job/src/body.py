from selenium import webdriver
import pandas as pd
import time


driver = webdriver.Chrome('./chromedriver')

df = pd.read_csv('./raw_data/url_list.csv')
df2 = df['0']
# print(df2.head())


features = ['company', 'grade', 'toeic', 'speaking', 'opic', 'lang', 'cert', 'abr', 'inte', 'prize', 'vol']
# globals()['{}'.format(features[])] = []



title = []

# grade = []
# toeic = []
# speaking = []
# opic = []
# lang = []
# cert = []
# abr = []
# inte = []
# prize = []
# vol = []


spec_dict = dict()

major = []
n = 0
try:
    for url in df2[:1000]:
        # print(url)
        driver.implicitly_wait(3)
        time.sleep(0.2)
        driver.get(url)

        company = driver.find_element_by_xpath('//*[@id="devPassSpecForm"]/div/h2/strong/a').text
        title.append(company)

        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[3]/a').click()
        downSpec = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[4]/div[1]/div/ul').text
        downSpecs = downSpec.split('\n')

        # spec = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div/ul').text
        # specs = spec.split('\n')


        # college = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div/ol[4]').text
        # colleges = college.split('\n')

        temp = [company]

        for i, j in enumerate(downSpecs):
            word = j
            if '보유' in str(word):
                downSpecs.remove(word)


        for idx, spec in enumerate(downSpecs):
            if idx%2 != 0:
                temp.append(spec)
        spec_dict[n] = temp
        n += 1
except:
    pass
# print(spec_dict)

df = pd.DataFrame.from_dict(spec_dict).T
df.columns = features
print(df.head())
df.to_csv('./raw_data/down_body.csv', index=False)


# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[1]/ul/li[2]/a').click()
# upSpec = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[3]/div[3]/div[1]/div/ul').text
# upSpecs = upSpec.split('\n')

#     for i, j in enumerate(specs):
#         word = j
#         if '보유' in str(word):
#             specs.remove(word)
#     # print(specs)
#     for idx, fea in enumerate(specs):
#         if '학점' == str(fea):
#             grade.append(specs[idx+1])
#         elif '토익' == str(fea):
#             toeic.append(specs[idx+1])
#         elif '토익스피킹' == str(fea):
#             speaking.append(specs[idx+1])
#         elif 'OPIC' == str(fea):
#             opic.append(specs[idx+1])
#         elif '외국어(기타)' == str(fea):
#             lang.append(specs[idx+1])
#         elif '자격증' == str(fea):
#             cert.append(specs[idx+1])
#         elif '해외경험' == str(fea):
#             abr.append(specs[idx+1])    
#         elif '인턴' == str(fea):
#             inte.append(specs[idx+1])
#         elif '수상내역' == str(fea):
#             prize.append(specs[idx+1])
#         elif '교내/사회/봉사' == str(fea):
#             vol.append(specs[idx+1])
#     for idx, col in enumerate(colleges):
#         if col == '1':
#             major.append(colleges[idx+1])
        


# print(title)
# print(grade)
# print(major)

# title = pd.DataFrame(title)
# grade = pd.DataFrame(grade)
# toeic = pd.DataFrame(toeic)
# speaking = pd.DataFrame(speaking)
# opic = pd.DataFrame(opic)
# lang = pd.DataFrame(lang)
# cert = pd.DataFrame(cert)
# abr = pd.DataFrame(abr)
# inte = pd.DataFrame(inte)
# prize = pd.DataFrame(prize)
# vol = pd.DataFrame(vol)

# pdList = [title, grade, toeic, speaking, opic, lang, cert, abr, inte, prize, vol]  # List of your dataframes
# new_df = pd.concat(pdList, axis=1)
# print(new_df.head())


df = pd.read_csv('./raw_data/down_body.csv')
print(df.head())
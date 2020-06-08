import pandas as pd
import os

path = './raw_data/'
file_list = os.listdir(path)

df = pd.read_csv(path + '2020-6-8  11시 56분.csv')
print(df.head())

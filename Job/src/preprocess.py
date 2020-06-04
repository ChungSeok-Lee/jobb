import pandas as pd
import os

path = './raw_data/'
file_list = os.listdir(path)

df = pd.read_csv(path + 'totalspecs.csv')
print(df)
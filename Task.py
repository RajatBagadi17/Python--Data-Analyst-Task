# -*- coding: utf-8 -*-
"""TASK.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d4sSTLB3rcmR4iaq0H-VnxZj3b5BmPyd
"""

import pandas as pd

sbi_data = pd.read_csv('SBIN_Data.csv')

sbi_data.head()

print(sbi_data.head())

print(sbi_data['Date'].dtype)

print(sbi_data['Date'].isnull().sum())

sbi_data['Date'] = sbi_data['Date'].astype(str)

sbi_data['Date'] = sbi_data['Date'].apply(lambda x: x.zfill(10))

sbi_data['Date'] = pd.to_datetime(sbi_data['Date'], format="%d-%m-%Y")

sbi_data['Rank'] = sbi_data.groupby('Time')['Volume'].transform(lambda x: x.rank(ascending=False, method='dense'))

sbi_data.head()

sbi_data


# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 11:15:53 2023

@author: Jagrati Garg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

df = pd.read_json("bitly.json", lines=True)
df.isna()
df=df.replace(np.NaN,'Missing')
df.isna()
df.isnull().any(axis=0)
df=df.replace(" ","Unknown")
df


df.columns
df_10=df['tz'].value_counts()
df_=df_10.head(10)
df_

df_.plot(kind='bar')



token=df['a'].str.split(n=1,expand=True).add_prefix('token_')
token
tokenfreq=token['token_0'].value_counts()
tokenfreq

tokenfreq.head().plot(kind='bar')
token.isna()
token=token.replace(np.nan,"Missing")
token


token['os']='not windows'
token['os'][token['token_1'].str.find('Windows')==1]='windows'
token

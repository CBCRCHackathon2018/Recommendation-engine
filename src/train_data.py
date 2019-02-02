import pandas as pd
import numpy as np
import sklearn as skl
import requests as rq

dataset_path = "../hackathon/train.csv"
base_url = "https://www.cbc.ca/json/cmlink/"
ds = pd.read_csv(dataset_path)
ds = ds.head(3000)
ds['deck'] = ''
ds['section'] = ''
for index, entity in ds.iterrows():
    try:
        r = rq.get(url = base_url + "%.7f" %entity['contentId'] ).json()
        ds.at[index, 'deck'] = r['deck']
        ds.at[index, 'section'] = r['advertising']['section']
    except Exception as e:
        print("%.7f" %entity['contentId'])
    if index>3000:
        break 

ds.to_csv('../hackathon/train_w_content.csv')

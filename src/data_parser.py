import pandas as pd
import numpy as np
import sklearn as skl
import requests as rq
import json

dataset_path = "../hackathon/train_w_content.csv"
ds = pd.read_csv(dataset_path)

# empty dictionary
d = dict()

for index, entity in ds.iterrows():

    user = entity["userId"]

    evId = entity['eventId']
    dec = entity["deck"]
    section = entity["section"]

    if user not in d:
        d[user] = list()
    
    d[user].append([evId, dec, section])

with open('../hackathon/parsed_train_w_content.json', 'w') as outfile:
    json.dump(d, outfile)

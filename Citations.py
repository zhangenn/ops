_name_ = 'main'
import json
import pandas as pd
from pandas import DataFrame
import requests
import re

def get_title_list(df):
    '''Get title list from Emily's json file'''
    result = df.loc[:,'title']
    title_list = [ ]
    for i in result:
        i = i.encode("utf-8")
        title_list.append(i)
    return (title_list)

def get_id_list(df):
    '''Get id list from Emily's json file'''
    result = df.loc[:,'id']
    id_list = [ ]
    for i in result:
        i = i.encode("utf-8")
        id_list.append(i)
    return (id_list)

def get_citation_list(id_list):
    i = 0 
    citation_list = [ ]
    for i in range (0,10):
        id1 = str(id_list[i])
        id1 = id1.replace('http://arxiv.org/abs/','')
        id1 = id1.replace("b'","")
        id2 = re.match(r'(.*)v', id1, re.M|re.I)
        id3 = id2.group(1)
        url = ("http://api.semanticscholar.org/v1/paper/arXiv:" + id3)
        response = requests.get(url)
        result = response.json()
        result1 = len(result['citations'])
        citation_list.append(result1)
    return (citation_list)


if __name__ == "__main__":
    data = pd.read_json("DL.json")
    df = DataFrame (data=data)
    df = df.transpose ()
    #with open ('DL.json','r') as f:
    #    DL_file = json.load(f)
    title_list = get_title_list(df)
    id_list = get_id_list(df)
    citation_list = get_citation_list(id_list)

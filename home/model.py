from re import search
from turtle import color
import pandas as pd
import pytrends
import matplotlib.pyplot as plt
import io
import urllib,base64
from urllib.parse import quote
from pytrends.request import TrendReq
import seaborn as sns
trends = TrendReq()
def graph(qu):
    trends.build_payload(kw_list=[qu],timeframe='2020-01-01 2021-01-01',geo='IN')
    data = trends.interest_by_region()
    data = data.sort_values(by=qu, ascending=False)
    data = data.head(10)

    data=data.reset_index()
    sns.set(rc={'figure.figsize':(15, 6)})
    data.plot(x="geoName", y=qu, kind="barh") 
    #plt.show()

    
    #data.reset_index().plot(x="geoName", y=qu, kind="barh")
    #fig, ax = plt.subplots(figsize=(15, 5))

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='jpeg')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = quote(string)

    return uri

def graph2(qu):
    data = TrendReq(hl='en-US', tz=360)
    data.build_payload(kw_list=[qu])
    data = data.interest_over_time()
    fig, ax = plt.subplots(figsize=(10, 5))
    data[qu].plot()
    plt.style.use('fivethirtyeight')
    plt.title('Total Google Searches for '+qu, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Total Count')

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='jpeg')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = quote(string)

    return uri
import re
import json
from urllib.request import urlopen,quote
import requests
import pandas as pd


def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '你的百度地图ak'  # 百度地图ak，具体申请自行百度，提醒需要在“控制台”-“设置”-“启动服务”-“正逆地理编码”，启动
    address = quote(address)  # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat, lng  # 纬度 latitude   ，   经度 longitude  ，


def getlnglat_arr(data):
    for indexs in data.index:
        get_location = getlnglat(data.loc[indexs, '圈定区域'])
        get_lat = get_location[0]
        get_lng = get_location[1]
        data.loc[indexs, '纬度'] = get_lat
        data.loc[indexs, '经度'] = get_lng
    return data


def address_extraction(data):
    data = str(data)
    pattern = re.compile(r'(?<=\|).*')
    return pattern.search(data)


def address_extraction_arr(arr):
    resultarr = []
    for i in arr:
        result = address_extraction(i)
        if result is None:
            pass
        else:
            result = result.group()
            #print(result)
            #print(type(result))
            resultarr.append(result)
    return resultarr


def main1():
    data = pd.read_excel('rawdata.xls')
    result = getlnglat_arr(data)
    data_html = pd.DataFrame(columns=['content'])
    for indexs in data.index:
        data_html.loc[indexs, 'content'] = '{' + \
                                           '"lat":' + str(data.loc[indexs, '纬度']) + ',' + \
                                           '"lng":' + str(data.loc[indexs, '经度']) + ',' + \
                                           '"quyu":' + '"' + str(data.loc[indexs, '圈定区域']) + '"' + \
                                           '}' + ','

    data_html.to_csv("data_html.csv", encoding="utf-8")

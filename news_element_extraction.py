# -*- coding: UTF-8 -*-
import requests
import json
from config import appcode


host = 'http://xwys.market.alicloudapi.com'
path = '/rest/160601/text_analysis/news_element_extraction.json'
url = host+path

headers = {
    'Authorization': 'APPCODE ' + appcode,
    'Content-Type': 'application/json; charset=UTF-8'
}


def news_element_extraction_body(data):
    body = {
    "inputs": [{
        "title": {
            "dataType": 50,
            "dataValue": ""
        },
        "content": {
            "dataType": 50,
            "dataValue": data
        },
        "config": {
            "dataType": 50,
            "dataValue": "{\"topN\": 5}"
        }
    }]
}
    return body


def news_element_extraction(data):
    r = requests.post(url, data=json.dumps(news_element_extraction_body(data)), headers=headers)
    outputs = json.loads(r.text)
    datavalue = json.loads(outputs["outputs"][0]["outputValue"]["dataValue"])
    return datavalue['data']


def test():
    data = "【H7N9禽流感最新疫情通报】诸暨市疾控中心通报，截至2014年1月8日12时，我市未发现人感染H7N9禽流感新发病例，密切接触者未见异常。据市动物疫病预防控制中心通报，截至2014年1月8日12时，我市未检测到家禽H7N9禽流感阳性样本。望广大市民不信谣，不传谣。 ​"
    outputs = news_element_extraction(data)

    print(outputs)
    print(type(outputs))
    #for key in outputs:
    #    print(str(key) + " is coor to " + str(outputs[key]))




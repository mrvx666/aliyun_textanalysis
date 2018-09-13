# -*- coding: UTF-8 -*-
import requests
import json
from config import appcode


host = 'http://gjccq.market.alicloudapi.com'
path = '/rest/160601/text_analysis/key_words_extraction.json'
url = host+path


headers = {
    'Authorization': 'APPCODE ' + appcode,
    'Content-Type': 'application/json; charset=UTF-8'
}


def key_words_extraction_body(data):
    body = {
    "inputs": [{
        "text": {
            "dataType": 50,
            "dataValue": data
        },
        "config": {
            "dataType": 50,
            "dataValue": "{\"topN\": 3, \"similarityType\": \"lcs\",\"delimiter\":\"。！？\"}"
        }
    }]
}
    return body


def key_words_extraction(data):
    r = requests.post(url, data=json.dumps(key_words_extraction_body(data)), headers=headers)
    outputs = json.loads(r.text)
    datavalue = json.loads(outputs["outputs"][0]["outputValue"]["dataValue"])
    return datavalue['words weight']

def test():
    data = "副省长、省食安委副主任看望慰问一线人感染H7N9禽流感防控工作人员。​"
    outputs = key_words_extraction(data)
    print(type(outputs))
    for key in range(0,len(outputs),1):
        print(str(key) + " is coor to " + str(outputs[key]))

    #print(outputs)

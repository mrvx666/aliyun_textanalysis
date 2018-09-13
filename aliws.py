# -*- coding: UTF-8 -*-
import requests
import json
from config import appcode

host = 'http://wbfxfc.market.alicloudapi.com'
path = '/rest/160601/text_analysis/aliws.json'
url = host+path

headers = {
    'Authorization': 'APPCODE ' + appcode,
    'Content-Type': 'application/json; charset=UTF-8'
}


def aliws_body(data):
    body = {
  "inputs": [
    {
      "text": {
        "dataType": 50,
        "dataValue": data
      }
    }
  ]
}
    return body


def aliws(data):
    r = requests.post(url, data=json.dumps(aliws_body(data)), headers=headers)
    outputs = json.loads(r.text)
    datavalue = json.loads(outputs["outputs"][0]["outputValue"]["dataValue"])
    return datavalue['tokens']


def test():
    data = "副省长、省食安委副主任看望慰问一线人感染H7N9禽流感防控工作人员。​"
    outputs = aliws(data)

    print(outputs)
    print(type(outputs))
    #for key in outputs:
    #    print(str(key) + " is coor to " + str(outputs[key]))




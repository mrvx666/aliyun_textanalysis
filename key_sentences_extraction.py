# -*- coding: UTF-8 -*-
import requests
import json
from config import appcode


host = 'http://gjjcq.market.alicloudapi.com'
path = '/rest/160601/text_analysis/key_sentences_extraction.json'
url = host+path


headers = {
    'Authorization': 'APPCODE ' + appcode,
    'Content-Type': 'application/json; charset=UTF-8'
}


def key_sentences_extraction_body(data):
    body = {
  "inputs": [
    {
      "text": {
        "dataType": 50,
        "dataValue": data
      },
      "config": {
        "dataType": 50,
        "dataValue": "{\"topN\": 3, \"similarityType\": \"lcs\",\"delimiter\":\"。！？\"}"
      }
    }
  ]
}
    return body


def key_sentences_extraction(data):
    r = requests.post(url, data=json.dumps(key_sentences_extraction_body(data)), headers=headers)
    outputs = json.loads(r.text)
    datavalue = json.loads(outputs["outputs"][0]["outputValue"]["dataValue"])
    return datavalue['data']


def test():
    data = "副省长、省食安委副主任看望慰问一线人感染H7N9禽流感防控工作人员。​"
    outputs = key_sentences_extraction(data)

    print(outputs)
    print(type(outputs))
    #for key in outputs:
    #    print(str(key) + " is coor to " + str(outputs[key]))

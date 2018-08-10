#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

url = "http://info.trustnote.org:6552"
headers = {'content-type': 'application/json'}

def get_result(payload):
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    return json.dumps(response)



def get_balance(address):
    payload = {
        "method": "getbalance",
        "params": [address],
        "jsonrpc": "2.0",
        "id": 1,
    }
    balance = json.loads(get_result(payload))
    stable = balance["result"]["base"]["stable"]
    pending = balance["result"]["base"]["pending"]
    amount = stable+pending
    return amount/1000000

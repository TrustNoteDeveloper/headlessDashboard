#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

url = "http://localhost:6552"
headers = {'content-type': 'application/json'}

def get_result(payload):
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    return json.dumps(response)

def get_all_address():
    payload = {
        "method": "getalladdress",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)

def make_a_new_address():
    payload = {
        "method": "getnewaddress",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)

def get_balance():
    payload = {
        "method": "getbalance",
        "params": {},
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)

def get_balance_of(address):
    payload = {
        "method": "getaddressbalance",
        "params": [address],
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)

def payTTT(address,amount):
    payload = {
        "method": "sendtoaddress",
        "params": [address,amount],
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)

def pay(address,amount,token):
    payload = {
        "method": "sendtoaddress",
        "params": [address,amount,token],
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)

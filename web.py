# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from flask import make_response,Response
app = Flask(__name__)
import rpc,json

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/api/pay',methods=['POST'])
def pay():
    if request.method == 'POST':
        address = request.form['address']
        amount = request.form['amount']
        token = request.form['token']
        content = rpc.pay(address,int(amount),token)
        resp = Response_headers(content)
        return resp

@app.route('/api/payTTT',methods=['POST'])
def payTTT():
    if request.method == 'POST':
        address = request.form['address']
        amount = request.form['amount']
        content = rpc.payTTT(address,amount)
        resp = Response_headers(content)
        return resp

@app.route('/api/address/all',methods=['GET'])
def all_address():
    content = rpc.get_all_address()
    resp = Response_headers(content)
    return resp

@app.route('/api/address/new',methods=['GET'])
def new_address():
    content = rpc.make_a_new_address()
    resp = Response_headers(content)
    return resp

@app.route('/api/balance',methods=['GET'])
def balance():
    content = rpc.get_balance()
    resp = Response_headers(content)
    return resp

@app.route('/api/balance/<string:address>',methods=['GET'])
def balance_of(address):
    content = rpc.get_balance_of(address)
    resp = Response_headers(content)
    return resp

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)

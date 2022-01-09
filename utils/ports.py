from flask import Flask, render_template, jsonify
import requests

#GET PORTS :------------------------------------------------------

API_URL2 = "http://192.168.37.69:50000/port"

port = 0

def getPort():
    res = requests.get(API_URL2)
    port = res.json()
    return port.get('numport') # our port

port = getPort()
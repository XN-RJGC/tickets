# coding: utf-8
import re
import requests
import json

#12306网站上所有车站信息
url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"

def spase_statons():
    # Request
    request = requests.get(url, verify=False)

    # Re
    pattern = r'([A-Z]+)\|([a-z]+)'
    stations = dict(re.findall(pattern, request.text))
    # item reverse
    stations = dict(zip(stations.values(), stations.keys()))

    #for key in stations.keys():
    #    print key, stations.get(key)
    return stations

def store(stations):
    with open('stations.json', 'w') as f:
        f.write(json.dumps(stations))

def load_staion():
    with open('stations.json', 'r') as f:
        print type(json.load(f))

if __name__ == '__main__':
    #store(spase_statons())
    load_staion()


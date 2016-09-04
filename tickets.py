# coding: utf-8
"""Train tickets query on command-line

Usage: tickets [-gdtkz] <from> <to> <date>

Options:
    -h, --help      帮助
    -v, --version   版本
    -g              高铁
    -d              动车
    -t              特快
    -k              快速
    -z              直达

Example:
    tickets xi'an to baihe 2016-09-05
"""
from docopt import docopt
import train_collection
import json
import requests


def command_line():
    """
    Command-line interface.
    :return:
    """
    arguments = docopt(__doc__, version='1.1')
    #from_station =  arguments['<from>']
    #to_station = arguments['<to>']
    #date_station = arguments['<date>']

    stations = {}
    with open('stations.json', 'r') as f:
        stations = json.load(f)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date_station = arguments['<date>']

    # Construct url
    # 查询车票信息url
    url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s" % (date_station, from_station, to_station)
    #print url
    try:
        request = requests.get(url, verify=False)
        #for item in request.json()['data']['datas']:
        #    print item
        datas = request.json()['data']['datas']

        trains = train_collection.train_collection(datas)
        # 利用prettytable实现类似mysql格式
        trains.pretty_print()
        #
    except:
        print 'error'

if __name__ == '__main__':
    command_line()

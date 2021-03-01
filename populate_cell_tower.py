import csv
import requests
from pymongo import MongoClient
import json

client = MongoClient(
    'mongodb+srv://zedblox:zedblox%40564@cluster0.z8odo.mongodb.net/cellTower?retryWrites=true&w=majority')
db = client.zedblox_production
devicedata = db.devicedatas
dbcell = client.cellTower
cell = dbcell.celltowers

if __name__ == '__main__':
    count = 0
    cursor = devicedata.find({})
    for x in cursor:
        print(x['_id'])
        l = len(x['rawData'])
        # print(l)
        cells = []
        for i in range(l):
            print(i)
            if(x['rawData'][i]['GP']):
                print('GPS')
            else:
                if(x['rawData'][i]['CT']):
                    celltower = x['rawData'][i]['CT'].split(";")
                    for c in celltower:
                        if(c != ''):
                            # print(c.split(","))
                            radio = c.split(",")[0][1:4]
                            mcc = int(c.split(",")[1])
                            mnc = int(c.split(",")[2])
                            cells.append({
                                'lac': int(c.split(",")[3], 16),
                                'cid': int(c.split(",")[4], 16)
                            })
                    body = {
                        "token": "pk.e1a93d1d285c26b555cf3be8da579aa0",
                        "id": x['deviceID'],
                        "radio": radio,
                        "mcc": mcc,
                        "mnc": mnc,
                        "cells": cells,
                        "address": 1
                    }
                    # print(body)
                    filldata = requests.post('http://65.0.206.23:5000/api/v1.0/location',
                                             json=body, verify=False)
                    print(json.loads(filldata.text))
                    print('celltower')

        count = count+1
        # cursor.close()

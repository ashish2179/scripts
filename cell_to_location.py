import requests
import json
cell = "*GSM*,404,49,13AE,183A,5,66,-81,20,22,0,0;*GSM*,404,49,13AE,183C,11,26,-85,12,16,0,0;*GSM*,404,49,13AE,8F05,19,65,-85,12,16,0,0;*GSM*,404,49,13AE,8F04,2,70,-88,15,15,0,0;*GSM*,404,49,13AE,C992,33,28,-92,9,9,0,0;"
cells = []
deviceID= "ZN092004N82515"
celltower = cell.split(";")
print(celltower)
for c in celltower:
    print(c)
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
        "token": "pk.f9819b2f074bf1c58611637a6c01ed3d",
        "id": deviceID,
        "radio": radio,
        "mcc": mcc,
        "mnc": mnc,
        "cells": cells,
        "address": 1
    }
print(body)
print()
print()
print('****************************************************')
print()
print()
filldata = requests.post('http://65.0.206.23:5000/api/v1.0/location',
                            json=body, verify=False)
print(json.loads(filldata.text))
print()
print()
print('/////////////////////////////////////////')
print()
print()
odata = requests.post('https://ap1.unwiredlabs.com/v2/process.php',
                            json=body, verify=False)
print(json.loads(odata.text))
print()
print()
print('****************************************************')
print()
print()
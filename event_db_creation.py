from pymongo import MongoClient
from faker import Factory
import time
import datetime
import random
from random import uniform
import math



clientnew = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/zedbloxnew?retryWrites=true&w=majority')
dbnew = clientnew.zedbloxnew
col = dbnew.devicedatas

if __name__ == '__main__':
    count = 0
    for x in col.find({}):
       

        #print(x['deviceID'])
        data = {}
        event = []
        for y in x['rawData']:
            for z in y['status']:
                e = {}
                e['date'] = y['DT']
                #print(z.split(',')[0])
                if z.split(',')[1]=='3':
                    e['type'] = 'warning'
                    #print('warning')
                if z.split(',')[1]=='1':
                    e['type'] = 'info'
                    #print('info')
                e['message'] = z.split(',')[0]
                e['description'] = ''
            #print(e)
            event.append(e)
        #print(event)
        data['deviceID'] = x['deviceID']
        data['events'] = event
        data['createdAt'] = x['createdAt']
        data['updatedAt'] = x['updatedAt']

        #print(data)
            
        result = dbnew.events.insert_one(data)
        print( 'id: ' + str(result.inserted_id) )
    
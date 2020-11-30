from pymongo import MongoClient
from faker import Factory
import time
import datetime
import random
from random import uniform
import math

client = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/zedblox?retryWrites=true&w=majority')
db = client.zedblox
col = db.devicedatas

clientnew = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/zedbloxnew?retryWrites=true&w=majority')
dbnew = clientnew.zedbloxnew
# recods = db.users
# print(list(recods.find()))


# def create_devicedata(device_id):
#     result = dbnew.devicedatas.insert_one({
#         'rawData': [],
#         'location': [],
#         'temperature': [],
#         'sampledAt': [],
#         'battery': [],
#         'targetTemperature': [],
#         'signalQuality': 'good',
#         'deviceID': device_id,
#         'version': 'v1.0',
#         'sentAt': datetime.datetime.now(),
#         'receivedAt': datetime.datetime.now(),
#         'createdAt': datetime.datetime.now(),
#         'updatedAt': datetime.datetime.now()
#     })
#     print('id: ' + str(result.inserted_id) + ' device_data')


if __name__ == '__main__':
    # fake = Factory.create()
    # create_users(fake)
    # create_devices(fake)
    # link_device_and_user()

    count = 0
    for x in col.find({'ID':'15L_AP-ZB-01'}):
        print('////////////////////////////////////////////////////////')
        print(x['_id'])
        location, temperature, sampledAt, battery, targetTemperature = [],[],[],[],[]
        for y in x['D']:
            temperature.append(round(int(y['T2'])/100,1))
            if y['GP']=="":
                continue
            lat = math.floor(float(y['GP'].split(',')[1])/100)+(float(y['GP'].split(',')[1])%100)/60
            log = math.floor(float(y['GP'].split(',')[3])/100)+(float(y['GP'].split(',')[3])%100)/60
            location.append(str(lat)+','+str(log))
            sampledAt.append(y['DT'])
            battery.append(y['B'])
            targetTemperature.append(round(int(y['TG'])/100,1))
        # print(x)
        print(location)
        print(temperature)
        print(sampledAt)
        print(battery)
        print(targetTemperature)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        # result = dbnew.devicedatas.insert_one({
        #     'rawData': x['D'],
        #     'location':location,
        #     'temperature':temperature,
        #     'sampledAt':sampledAt,
        #     'battery':battery,
        #     'targetTemperature':targetTemperature,
        #     'signalQuality':'good',
        #     'deviceID': 'ZE092015K46978',
        #     'version': x['V'],
        #     'sentAt': x['DT'],
        #     'receivedAt': x['DT'],
        #     'createdAt': x['created_at'],
        #     'updatedAt': x['updated_at']
        # })
        # print('id: ' + str(result.inserted_id)) 
        print(count)
        count = count+1
        print('////////////////////////////////////////////////////////')
    # x = col.find_one({'ID': 'Default_test_1'})
    # print(x['D'][0]['DT'])
    # print(x)
    # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    # location, temperature, sampledAt, battery, targetTemperature = [], [], [], [], []
    # for y in x['D']:
    #         print(y['DT'])
    #         temperature.append(round(int(y['T2'])/100, 1))
    #         # print(math.floor(float(y['GP'].split(',')[1])/100))
    #         # print((float(y['GP'].split(',')[1])%100)/60)
    #         print(math.floor(float(y['GP'].split(',')[1]) /
    #                          100)+(float(y['GP'].split(',')[1]) % 100)/60)
    #         print(math.floor(float(y['GP'].split(',')[3]) /
    #                          100)+(float(y['GP'].split(',')[3]) % 100)/60)
    #         lat = math.floor(float(y['GP'].split(',')[1])/100) + \
    #             (float(y['GP'].split(',')[1]) % 100)/60
    #         log = math.floor(float(y['GP'].split(',')[3])/100) + \
    #             (float(y['GP'].split(',')[3]) % 100)/60
    #         location.append(str(lat)+','+str(log))
    #         sampledAt.append(y['DT'])
    #         battery.append(y['B'])
    #         targetTemperature.append(round(int(y['TG'])/100, 1))
    #         # print(y['GP'].split(',')[3])
    # print(temperature)
    # print(location)
    # print(sampledAt)
    # print(battery)
    # print(targetTemperature)
    # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    # result = dbnew.devicedatas.insert_one({
    #         'rawData': x['D'],
    #         'location': location,
    #         'temperature': temperature,
    #         'sampledAt': sampledAt,
    #         'battery': battery,
    #         'targetTemperature': targetTemperature,
    #         'signalQuality': 'good',
    #         'deviceID': 'ZC092004W60796',
    #         'version': x['V'],
    #         'sentAt': x['DT'],
    #         'receivedAt': x['DT'],
    #         'createdAt': x['created_at'],
    #         'updatedAt': x['updated_at']
    # })
    # print('id: ' + str(result.inserted_id))

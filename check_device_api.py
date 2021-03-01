import requests
import json
from pymongo import MongoClient
import math
import time
import datetime
import random

# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token
# from telegram as described above
api_id = '2503357'
api_hash = '43e1f3da2d32b20fee69c7ef6a27fa3f'
token = '1224110922:AAGrdZsnOX66_VxT4Tw0UUqFY4zLh0two58'

# your phone number
phone = '+919740951971'
rphone = 'https://t.me/joinchat/Hk9GIBjyTOwlV4v7qy9jJg'

clientnew = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/zedbloxnew?retryWrites=true&w=majority')
dbnew = clientnew.zedbloxnew
data = dbnew.devicedatas
device = dbnew.devices

deviceID = 'ZR112015Y67854'

u = requests.post('https://65.0.206.23:3000/api/v1.0/login_dev', json={
    "id": deviceID, "hash": deviceID, 'version': 'v1.0'}, verify=False)
user = json.loads(u.text)
print(user)

if(len(user) > 2):
    print('logging successfully')

    nrml_inner_temp_min = 0
    nrml_inner_temp_max = 20

    abnrml_inner_temp_min = -25
    abnrml_inner_temp_max = 115

    outer_temp_inhot_max = 55
    outer_temp_inhot_min = 35

    outer_temp_incold_min = -15
    outer_temp_incold_max = 0

    nrml_cmp_rpm_min = 2000
    nrml_cmp_rpm_max = 3500
    abnrml_cmp_rpm_max = 5500
    abnrml_cmp_rpm_min = 1800

    nrml_battery_volt_max = 1260
    nrml_battery_volt_min = 960

    nrml_battery_amp_max = 3
    nrml_battery_amp_min = 6
    abnrml_battery_amp_max = 0.2
    abnrml_battery_amp_min = 9

    # atmospheric pressure range in INDIA 90 t0 115
    nrml_pressure_max = 115
    nrml_pressure_min = 90

    nrml_humidity_max = 100
    nrml_humidity_min = 0

    # INDIA is situated north of the equator
    # between 8'4' north to 37'6' north latitude and 68'7' east to 97'25' east longitude.
    # north = 90, south=270, east = 0, west=180
    R = 6378.1  # Radius of the Earth
    brng = float(90)  # Bearing is 90 degrees converted to radians.
    d = 0.1  # Distance in km
    lat1 = float(17.23543)  # Current lat point converted to radians
    lon1 = float(78.3645)  # Current long point converted to radians

    raw_data = []
    glat2 = (math.modf(lat1))[0]*60+(math.modf(lat1))[1]*100
    glon2 = (math.modf(lon1))[0]*60+(math.modf(lon1))[1]*100
    x = datetime.datetime.now()
    raw_date = str(x.strftime("%y"))+'/'+str(x.strftime("%m"))+'/'+str(x.strftime("%d"))+','+str(
        x.strftime("%H"))+':'+str(x.strftime("%M"))+':'+str(x.strftime("%S"))+'.'+str(x.strftime("%f"))
    raw_data.append({
        'DT': raw_date,
        'T1': int(round(random.uniform(nrml_inner_temp_max, abnrml_inner_temp_max), 2)*100),
        'T2': int(round(random.uniform(outer_temp_inhot_max, outer_temp_inhot_max*2), 2)*100),
        'HP1': str(int(round(random.uniform(nrml_humidity_max, nrml_humidity_max*2), 2)*100))+',' +
        str(int(round(random.uniform(
            nrml_pressure_max, nrml_pressure_max*2), 2)*100)),
        'HP2': str(int(round(random.uniform(nrml_humidity_max, nrml_humidity_max*2), 2)*100))+',' +
        str(int(round(random.uniform(
            nrml_pressure_max, nrml_pressure_max*2), 2)*100)),
        'IM1': "-246,-306,0,-136,-169,9935,-6,7,5",
        'GP': "000058.263,"+str(glat2+1)+",N,"+str(glon2+1)+",E,0,0,,221.0,M,-71.0,M,,*76",
        'M': str(round(random.uniform(abnrml_cmp_rpm_min, abnrml_cmp_rpm_max))) +
        ',0,0,0',
        'B': str(round(random.uniform(nrml_battery_volt_min-100, nrml_battery_volt_max+100)))+',' +
        str(int(round(random.uniform(abnrml_battery_amp_min, abnrml_battery_amp_max), 2)*100)) +
        ',0,0,0,0,0,0',
        'CT': '',
        'TG': round(random.uniform(-20, 80))*100,
    })

    body = {
        "ID": deviceID,
        "auth_key": user["auth_key"],
        "V": "v1.0",
        "DT": raw_date,
        "D": raw_data
    }

    filldata = requests.post('https://65.0.206.23:3000/api/v1.0/send_data',
                             json=body, verify=False)
    data = json.loads(filldata.text)
    print(data)

    if data["CS"] == 'S':
        print('send data api work successfully')
    else:
        print('error in send data api')
        # creating a telegram session and assigning
        # it to a variable client
        client = TelegramClient('session', api_id, api_hash)

        # connecting and building the session
        client.connect()

        # in case of script ran first time it will
        # ask either to input token or otp sent to
        # number or sent or your telegram id
        if not client.is_user_authorized():

            client.send_code_request(phone)

            # signing in the client
            client.sign_in(phone, input('Enter the code: '))

        try:
            # receiver user_id and access_hash, use
            # my user_id and access_hash for reference
            receiver = InputPeerUser('user_id', 'user_hash')

            # sending message using telegram client
            client.send_message(
                rphone, 'Device send data api error', parse_mode='html')
        except Exception as e:

            # there may be many error coming in while like peer
            # error, wwrong access_hash, flood_error, etc
            print(e)

        # disconnecting the telegram session
        client.disconnect()
else:
    print('logging error')

    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient('session', api_id, api_hash)

    # connecting and building the session
    client.connect()

    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or sent or your telegram id
    if not client.is_user_authorized():

        client.send_code_request(phone)

        # signing in the client
        client.sign_in(phone, input('Enter the code: '))

    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        receiver = InputPeerUser('user_id', 'user_hash')

        # sending message using telegram client
        client.send_message(
            rphone, 'Device logging api error', parse_mode='html')
    except Exception as e:

        # there may be many error coming in while like peer
        # error, wwrong access_hash, flood_error, etc
        print(e)

    # disconnecting the telegram session
    client.disconnect()

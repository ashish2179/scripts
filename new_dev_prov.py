import argparse
import requests
import json
import configparser

parser = argparse.ArgumentParser(description='Parse provision args')
# parser.add_argument('-mfgdt', '--manufacturing_date', required=True,
#                     help='manufacturing date in MMYY')
# parser.add_argument('-cap', '--capacity', required=True,
#                     help='capacity of actipod in liter ')

parser.add_argument('-abi', '--acrux_brd_id', required=True,
                    help='Acrux board id')
parser.add_argument('-blebi', '--BLE_brd_id', required=True,
                    help='BLE board id')
parser.add_argument('-mbi', '--modem_brd_id', required=True,
                    help='Modem board id')
parser.add_argument('-dbi', '--display_brd_id', required=True,
                    help='Display board id')
parser.add_argument('-imn', '--imei_no', required=True,
                    help='IMEI no.')
parser.add_argument('-simi', '--sim_id', required=True,
                    help='SIM ID')
parser.add_argument('-pn', '--phone_number', required=True,
                    help='Phone no.')
parser.add_argument('-msn', '--modem_serial_no', required=True,
                    help='Modem serial no.')
parser.add_argument('-bmsbi', '--bms_brd_id', required=True,
                    help='BMS board ID')
parser.add_argument('-batbi', '--battery_pack_id', required=True,
                    help='Battery pack ID')
parser.add_argument('--device_id', required=True,
                    help='Device ID (Primary key for this data set)')
parser.add_argument('-compi', '--compressor_id', required=True,
                    help='Compresor ID')
parser.add_argument('-fani', '--fan_id', required=True,
                    help='Fan ID')
parser.add_argument('-disi', '--display_id', required=True,
                    help='Display ID')


args = parser.parse_args()
# x = requests.get('https://localhost:3000/api/v1.0/generate/deviceid', json={
#                  "monthyear": args.manufacturing_date, "capacity": args.capacity}, verify=False)
# print(x.text)
# data = json.loads(x.text)
# print(data["deviceId"])


response = {
    "admin_id": "zedblox",
    "password": "12345678",
    "version": "v1.0",
    "deviceName": "Actipod "+args.device_id,
    "deviceId": args.device_id,
    "property": {
        "acrux_brd_id": args.acrux_brd_id,
        "BLE_brd_id": args.BLE_brd_id,
        "modem_brd_id": args.modem_brd_id,
        "display_brd_id": args.display_brd_id,
        "imei_no": args.imei_no,
        "sim_id": args.sim_id,
        "phone_number": args.phone_number,
        "modem_serial_no": args.modem_serial_no,
        "bms_brd_id": args.bms_brd_id,
        "battery_pack_id": args.battery_pack_id,
        "compressor_id": args.compressor_id,
        "fan_id": args.fan_id,
        "display_id": args.display_id
    },
    "setting": {
        "UP": 0,
        "UI": 300000,
        "DCI": 600000,
        "PS": "https://ec2-44-233-13-28.us-west-2.compute.amazonaws.com:3000",
        "SS": "https://www.zedblox.com:443",
        "LU": "/api/v1.0/login_dev",
        "DU": "/api/v1.0/send_data",
        "PU": "/api/v1.0/provision_dev",
        "OU": "/api/v1.0/ota",
        "TU": "/api/v1.0/trip",
        "SN": "979720401",
        "SC": "FR86W"
    }
}
responsedump = json.dumps(response)
responsejson = json.loads(responsedump)
# print(responsejson)

y = requests.post('https://44.233.13.28:3000/api/v1.0/provision_dev',
                  json=responsejson, verify=False)
# print the response text (the content of the requested file):
print(y.text)



config = configparser.ConfigParser()
config['Default'] = {}
default = config['Default']

default['PRIMARY_SERVER'] = '"https://ec2-44-233-13-28.us-west-2.compute.amazonaws.com:3000"'
default['SECONDARY_SERVER'] = '"https://www.zedblox.com:443"'
default['SERVER_PORT'] = '3000'
default['PROVISION_URL'] = '"/api/v1.0/provision_dev"'
default['LOGIN_URL'] = '"/api/v1.0/login_dev"'
default['OTA_URL'] = '"/api/v1.0/ota"'
default['TRIP_URL'] = '"/api/v1.0/trip"'
default['SEND_DATA_URL'] = '"/api/v1.0/send_data"'
default['DEVICE_ID'] = args.device_id
default['SIM_ID'] = args.sim_id
default['PHONE_NUMBER'] = args.phone_number
default['UPLOAD_INTERVAL'] = '"300000"'
default['DATA_INTERVAL'] = '"600000"'
default['SMS_CODE'] = '"FR86W"'
default['POST_SMS_NUMBER'] = '"979720401"'

with open('setup.cfg', 'w') as configfile:
    config.write(configfile)
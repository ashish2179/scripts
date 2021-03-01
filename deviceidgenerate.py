# import requests
# from requests.exceptions import HTTPError

# for url in ['https://localhost:3000/api/v1.0/generate/deviceid']:
#     try:
#         response = requests.get(url, verify=False)

#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')

import requests
import json
import argparse
# import pandas as pd
#
parser = argparse.ArgumentParser(description='Parse provision args')
parser.add_argument('-mfgdt', '--manufacturing_date', required=True,
                    help='manufacturing date in MMYY')
parser.add_argument('-cap', '--capacity', required=True,
                    help='capacity of actipod in liter ')

args = parser.parse_args()
# the required first parameter of the 'get' method is the 'url':
my_list = []
for i in range(50):
    x = requests.get('https://localhost:3000/api/v1.0/generate/deviceid', json={
    "monthyear": args.manufacturing_date, "capacity": args.capacity}, verify=False)
    # print(x.text)
    data = json.loads(x.text)
    # print(data["deviceId"])
    my_list.append(data["deviceId"])
print(my_list)

# df = pd.DataFrame()
# df['deviceId'] = my_list[0::1]
# df.to_excel('result.xlsx', index = False)
# print(my_list)
# print(data["deviceId"])


# y = requests.post('https://localhost:3000/api/v1.0/provision_dev', json=json.loads(x.text),verify=False)
# #print the response text (the content of the requested file):
# print(y.text)

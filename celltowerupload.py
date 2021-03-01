import csv
from pymongo import MongoClient
import requests
import datetime

client = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/cellTower?retryWrites=true&w=majority')
db = client.cellTower
celltower = db.celltowers

with open('G:\zedblox\Downloads\cell405.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]}, {row[1]}, {row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]},{row[9]}')

            # # print(body)
            # filldata = requests.post('https://localhost:3500/api/v1.0/cell/info',
            #                          json=body, verify=False)
            # print(filldata)
            # line_count += 1
            if row[0] == 'GSM':
                body = {
                    "radio": row[0],
                    "mcc": row[1],
                    "mnc": row[2],
                    "area": row[3],
                    "cellid": row[4],
                    "latitude": row[7],
                    "longitude": row[6],
                    "range": row[8],
                    "samples": row[9],
                    "createdAt": datetime.datetime.utcnow(),
                    "updatedAt": datetime.datetime.utcnow()
                }
                result = celltower.insert_one(body)
                print('id: ' + str(result.inserted_id) +
                      ' inserted successfully ')
                line_count += 1
    print(f'Processed {line_count} lines.')

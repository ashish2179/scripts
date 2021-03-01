import csv
import requests
from pymongo import MongoClient

# cell = MongoClient(
#     'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/zedbloxnew?retryWrites=true&w=majority')
cell = MongoClient(
    'mongodb+srv://zedblox:zedblox%40564@cluster0.z8odo.mongodb.net/cellTower?retryWrites=true&w=majority')
db = cell.cellTower
celltower = db.celltowers

with open('E:\Zedblox\Old Download\cell404.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    find_count = 0
    not_find = 0
    find_count_id = 0
    not_find_id = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
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
                    "samples": row[9]
                }
                result = celltower.find({
                    "radio": row[0],
                    "mcc": row[1],
                    "mnc": row[2],
                    "area": row[3],
                    "cellid": row[4],
                    "latitude": row[7],
                    "longitude": row[6],
                    "range": row[8],
                    "samples": row[9]
                })
                print(result)
                if(result):
                    find_count += 1
                    print("find cell tower")
                else:
                    not_find += 1
                    print("not found")
                # filldata = requests.get('https://localhost:5000/api/v1.0/cell/info',
                #                          json=body, verify=False)
                # print(filldata)

    print(f'Processed {line_count} lines.')

import csv
import requests

with open('E:\Zedblox\Old Download\cell404.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
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
                # filldata = requests.post('http://65.0.206.23:5000/api/v1.0/cell/info',
                #                          json=body, verify=False)
                # print(filldata)
                print(body)
                line_count += 1
                break
    print(f'Processed {line_count} lines.')

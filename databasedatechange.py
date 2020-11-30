from pymongo import MongoClient
import datetime

client = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/test?retryWrites=true&w=majority')
db = client.test
mycol = db.devicedatas
count = 0
for x in mycol.find():
  print(x["DT"])
  print((x["DT"].split(',')[0]).split('/')[0])
  year = "20"+(x["DT"].split(',')[0]).split('/')[0]
  print((x["DT"].split(',')[0]).split('/')[1])
  month = (x["DT"].split(',')[0]).split('/')[1]
  print((x["DT"].split(',')[0]).split('/')[2])
  day = (x["DT"].split(',')[0]).split('/')[2]
  print((x["DT"].split(',')[1]))
  time = (x["DT"].split(',')[1])
  #print(datetime.datetime(year, month, day,time)
  print(len(x["D"]))
  for y in range(len(x["D"])):
      print(y)
      print(x["D"][y]["DT"])
      count = count+1
print(count)
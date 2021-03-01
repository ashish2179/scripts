from pymongo import MongoClient
import time
import datetime


clientnew = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/zedbloxnew?retryWrites=true&w=majority')
dbnew = clientnew.zedbloxnew
data = dbnew.devicedatas
device = dbnew.devices 
user = dbnew.users

result = user.find_one({'email':'ashish21798@gmail.com'})
print(result)
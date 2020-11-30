from pymongo import MongoClient
client = MongoClient('mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/test?retryWrites=true&w=majority')
db = client.test
recods = db.users
print(list(recods.find()))

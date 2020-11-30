from pymongo import MongoClient
from faker import Factory
import time
import datetime
import random
from random import uniform


client = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/testdb?retryWrites=true&w=majority')
db = client.testdb
# recods = db.users
# print(list(recods.find()))


def create_users(fake):
    department = ['admin', 'OPD', 'specilist', 'surgen', 'management']
    organisation = ['applo credial', 'L V prasad',
                    'continetal', 'applo clinic', 'Maxvision']
    for x in range(5):
        genName = fake.first_name()
        genSurname = fake.last_name()
        genEmail = fake.email()
        genAddress = fake.address()

        result = db.users.insert_one(
            {
                'permission_level': 4,
                'device_id': [],
                'firstName': genName,
                'lastName': genSurname,
                'email': genEmail,
                'address': genAddress,
                'password': '',
                'versionKey': 'v1.0',
                'department': random.choice(department),
                'organisation': random.choice(organisation),
                'created_at': datetime.datetime.now(),
                'updated_at': datetime.datetime.now()
            }
        )

        print( 'id: ' + str(result.inserted_id) + ' firstName: ' + genName)
        # time.sleep(1)


def create_devices(fake):
    department = ['admin', 'OPD', 'specilist', 'surgen', 'management']
    organisation = ['applo credial', 'L V prasad',
                    'continetal', 'applo clinic', 'Maxvision']
    device_name = ['fridge', 'button', 'curdmaker']
    number = [1, 2, 3, 4]
    sms_no = ['324657346326', '5235218234',
              '23654326321', '4231324231', '3475731263']
    sms_code = ['38746', '34569', '34765', '437658', '435647', '34758']

    # rand = random.random()  # rand will be a floating point between 0 to 1.
    # created_record = collection.find_one({ 'random' => { '$gte' => rand } })


    for x in range(5):
        genName = fake.first_name()
        genSurname = fake.last_name()
        genEmail = fake.email()
        genAddress = fake.address()

        

        result = db.devices.insert_one({
            'property': {
                'property1': 'property1',
                'property2': 'property2',
                'property3': 'property3',
                'property4': 'property4',
                'property5': 'property5',
            },
            'setting': {
                'update_req': random.choice(number),
                'data_up_inv': random.choice(number),
                'data_col_inv': random.choice(number),
                'Login_url': "https://localhost:3000/api/v1.0/login_dev",
                'send_data_url': "https://localhost:3000/api/v1.0/send_data",
                'provision_url': "https://localhost:3000/api/v1.0/rovision_dev",
                'sms_no': random.choice(sms_no),
                'sms_code': random.choice(sms_code),
            },
            'deviceName': random.choice(device_name),
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now()
        })


        result1 = db.users.insert_one(
            {
                'permission_level': 4,
                'device_id': [str(result.inserted_id)],
                'firstName': genName,
                'lastName': genSurname,
                'email': genEmail,
                'address': genAddress,
                'password': '',
                'versionKey': 'v1.0',
                'department': random.choice(department),
                'organisation': random.choice(organisation),
                'created_at': datetime.datetime.now(),
                'updated_at': datetime.datetime.now()
            }
        )

        print( 'id: ' + str(result1.inserted_id) + ' firstName: ' + genName)
        
        print( 'id: ' + str(result.inserted_id) + ' device' )
        for x in range(5):
            create_devicedata(str(result.inserted_id))
            create_trips(str(result.inserted_id),str(result1.inserted_id),str(result1.inserted_id))
        # time.sleep(1)
def create_trips(device_id,created_by,assigned_by):
    status = ['good','warn','error']
    mode = ['road','air','walk','ocean','rail','autonomous','spaceship']
    action = ['start','stop']
    x, y = uniform(-180,180), uniform(-90, 90)
    start_location = str(x)+','+str(y)
    x1, y1 = uniform(-180,180), uniform(-90, 90)
    stop_location = str(x1)+','+str(y1)
    for x in range(5):
        result = db.trips.insert_one({
            'device_id': device_id,
            'start_time': datetime.datetime.now(),
            'status': random.choice(status),
            'reason': random.choice(status),
            'start_location': start_location,
            'destination': stop_location,
            'content':"",
            'description':"",
            'assigned_by':assigned_by,
            'created_by': created_by,
            'insights':"reserved",
            'mode': random.choice(mode),
            'action': random.choice(action)
        })
        print( 'id: ' + str(result.inserted_id) + ' trip')


def create_devicedata(device_id):
    number = [1, 2, 3, 4, 5]
    for x in range(5):
        result = db.devicedatas.insert_one({
            'Set': {
                'SE': {
                    'v': random.choice(number),
                    'msg': 'network'
                },
                'RBT': random.choice(number),
                'UE': random.choice(number),
            },
            'data': [{
                    'DT': datetime.datetime.now(),
                    'T1': round(random.uniform(-40, 60), 2),
                    'T2': round(random.uniform(-40, 60), 2),
                    'H1': round(random.uniform(-40, 60), 2),
                    'P1': round(random.uniform(-40, 60), 2),
                    'IM1': round(random.uniform(-40, 60), 2),
                    'L1': round(random.uniform(-40, 60), 2),
                    'GP': round(random.uniform(-40, 60), 2),
                    'M': round(random.uniform(-40, 60), 2),
                    'B': round(random.uniform(-40, 60), 2),
                    'TG': round(random.uniform(-40, 60), 2),
            },
            {
                    'DT': datetime.datetime.now(),
                    'T1': round(random.uniform(-40, 60), 2),
                    'T2': round(random.uniform(-40, 60), 2),
                    'H1': round(random.uniform(-40, 60), 2),
                    'P1': round(random.uniform(-40, 60), 2),
                    'IM1': round(random.uniform(-40, 60), 2),
                    'L1': round(random.uniform(-40, 60), 2),
                    'GP': round(random.uniform(-40, 60), 2),
                    'M': round(random.uniform(-40, 60), 2),
                    'B': round(random.uniform(-40, 60), 2),
                    'TG': round(random.uniform(-40, 60), 2),
            }
            ],
            'id': device_id,
            'version': 'v1.0',
            'date': datetime.datetime.now(),
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now()
        })
        print( 'id: ' + str(result.inserted_id) + ' device_data')

def link_device_and_user():
    myCollection = db.col_trip
    print(myCollection.count())
    for document in myCollection.find():
        print(document['created_by'])
        print(document['device_id'])
        db.col_user.update({"_id":document['created_by']},{"$set": {"device_id":document['device_id']}})

if __name__ == '__main__':
    fake = Factory.create()
    #create_users(fake)
    create_devices(fake)
    #link_device_and_user()
    

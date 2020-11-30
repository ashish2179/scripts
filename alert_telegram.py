# importing all required libraries 
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 


# get your api_id, api_hash, token 
# from telegram as described above 
api_id = '1924648'
api_hash = '60851275640091fc66868a6cd4309f92'
token = '1437375593:AAFsKddD5k5IKiBx6dmIXwkV3_fAINlvfX8'

# your phone number 
phone = '+918826109383'
rphone = 'https://t.me/joinchat/AAAAAE5MSHmaZAGx27-SGw'

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
	client.send_message(rphone, 'hello', parse_mode='html') 
except Exception as e: 
	
	# there may be many error coming in while like peer 
	# error, wwrong access_hash, flood_error, etc 
	print(e); 

# disconnecting the telegram session 
client.disconnect() 

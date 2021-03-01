# -*- coding: UTF8 -*-
import requests
import datetime
import re
from pymongo import MongoClient
import json

# for validating an Email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

clientnew = MongoClient(
    'mongodb+srv://ashish2:ashish123@cluster0-su4fz.mongodb.net/zedbloxnew?retryWrites=true&w=majority')
dbnew = clientnew.zedbloxnew
user = dbnew.users


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    # url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '1483387411:AAEPP2hb5u6ybwVgLTIOg3kE0nWkH0NLUPA'  # Token of your bot
magnito_bot = BotHandler(token)  # Your bot's name


def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates = magnito_bot.get_updates(new_offset)
        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text = 'New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "Stranger"

                if first_chat_text == '/start':
                    magnito_bot.send_message(
                        first_chat_id, 'Hi ' + first_chat_name + '! Please authorize me to set up a Zedblox integration.')
                    magnito_bot.send_message(
                        first_chat_id, 'please enter your zedblox email..')
                    new_offset = first_update_id + 1
                elif re.search(regex, first_chat_text):
                    result = user.find_one({'email': first_chat_text})
                    if(result):
                        u = requests.post('https://65.0.206.23:3000/api/v1.0/email', json={
                            "email": first_chat_text, "telegramID": first_chat_id, }, verify=False)
                        v = requests.post('https://65.0.206.23:3000/api/v1.0/otp', json={
                            "email": first_chat_text, "otp": first_chat_id, }, verify=False)
                        magnito_bot.send_message(
                            first_chat_id, 'check you email and enter code')
                    else:
                        magnito_bot.send_message(
                            first_chat_id, 'This email is not register with Zedblox')
                    new_offset = first_update_id + 1
                elif first_chat_text == str(first_chat_id):
                    w = requests.get('https://65.0.206.23:3000/api/v1.0/telegram/verify', json={
                        "otp": first_chat_text, }, verify=False)
                    telegram = json.loads(w.text)
                    if(telegram["otp"] == first_chat_text):
                        v = requests.post('https://65.0.206.23:3000/api/v1.0/telegram', json={
                            "email": telegram["email"], "telegramID": first_chat_text, }, verify=False)
                        magnito_bot.send_message(
                            first_chat_id, 'your telegram account associated with Zedblox')
                        magnito_bot.send_message(
                            first_chat_id, 'Now you can get alert on Telegram')
                    new_offset = first_update_id + 1
                else:
                    magnito_bot.send_message(
                        first_chat_id, 'incorrect email or otp')
                    magnito_bot.send_message(
                        first_chat_id, 'Please check email in smallcase and correct')
                    new_offset = first_update_id + 1
                # else:
                #     magnito_bot.send_message(first_chat_id, 'Welcome to ZedBlox \nHow can i help you '+first_chat_name)
                #     new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

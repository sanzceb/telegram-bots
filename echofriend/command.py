#!/usr/bin/env python3

import os

import requests

TOKEN = os.environ['BOT_TOKEN'] # presetup with export or env
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def _help(chat_id):
    msg_params = {
        'chat_id' : chat_id,
        'text' : 'Sorry, if you need help you’ll have to find a friend because\
            I only echo'
    }
    requests.get(f"{BASE_URL}/sendMessage", params=msg_params)

def _start(chat_id):
    params = {
        'chat_id' : chat_id,
        'text' : 'Hello, I am EchoFriend and I only echo'
    }
    requests.get(f"{BASE_URL}/sendMessage", params=params)

def execute(cmdname, chat_id):
    if cmdname == '/start':
        return _start(chat_id)
    else:
        return _help(chat_id)

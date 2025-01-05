#!/usr/bin/env python3

import os

import requests

TOKEN = os.environ['BOT_TOKEN'] # presetup with export or env
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def is_command(msg):
    return ('text' in msg) and (msg['text'].startswith('/'))

def execute(msg):
    if not is_command(msg): return
    
    cmdname = msg['text'][1:]
    params = {'chat_id' : msg['chat']['id']}
    if cmdname == 'start':
        _start(params)
    else:
        _help(params)

def _help(params):
    params['text'] = ("Sorry, if you need help you’ll have to find a friend"
                      " because I only echo")
    requests.get(f"{BASE_URL}/sendMessage", params=params)

def _start(params):
    params['text'] = 'Hello, I am EchoFriend and I only echo'
    requests.get(f"{BASE_URL}/sendMessage", params=params)
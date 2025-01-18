#!/usr/bin/env python3

import os

import requests

TOKEN = os.environ['BOT_TOKEN'] # presetup with export or env
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def handle_msg(msg):
    if not _is_command(msg): 
        _help({'chat_id' : msg['chat']['id']})
        return
    cmd = msg['text'].removeprefix('/').split(' ', 1)
    cmdname = cmd[0]
    cmdargs = cmd[1] if len(cmd) > 1 else None
    _execute(cmdname, cmdargs, msg)

def _execute(cmdname, cmdargs, msg):
    params = {'chat_id' : msg['chat']['id']}
    if cmdname == 'start':
        _start(params)
    elif cmdname == 'echo':
        _echo(cmdargs, params)
    else:
        _help(params)

def _help(params):
    params['text'] = ("Sorry, if you need help you’ll have to find a friend"
                      " because I only echo")
    requests.post(f"{BASE_URL}/sendMessage", params=params)

def _start(params):
    params['text'] = 'Hello, I am EchoFriend and I only echo'
    requests.post(f"{BASE_URL}/sendMessage", params=params)

def _echo(cmdargs, params):
    params['text'] = cmdargs
    requests.post(f"{BASE_URL}/sendMessage", params=params)
    print(f"Message echoed")

def _is_command(msg):
    return ('text' in msg) and (msg['text'].startswith('/'))

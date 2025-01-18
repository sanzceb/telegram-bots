#!/usr/bin/env python3

"""
This script implements a simple Telegram bot that handles two global commands:
start and help. When a text message is received it echoes back
"""

import os

import requests

import command 

TOKEN = os.environ['BOT_TOKEN'] # presetup with export or env
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

# Update Parameters
# - offset: Ensures we don't process the same update twice
# - timeout: Maximum time to wait for new updates (in seconds)
# - allowed_updates: Update types the bot will receive
update_params = {
        'offset' : 0,
        'timeout' : 300,
        'allowed_updates' : ['message']
}

def process_update(update):
    if 'message' in update:
        msg = update['message']
        command.handle_msg(msg)
    else:
        print(f"Update {update['update_id']} ignored")

updates = []
try:
    while True:
        res_json = requests.get(f"{BASE_URL}/getUpdates", update_params).json()
        if res_json['ok']:
            updates = res_json['result']
            for update in updates:
                process_update(update) 
            # Telegram won't send again the updates below the offset
            if updates: 
                update_params['offset'] = updates[-1]['update_id'] + 1
except KeyboardInterrupt:
    print('\nShutting down echofriend. Processing remaining updates if any')
    for update in updates:
        process_update(update)
    print('Program ended')

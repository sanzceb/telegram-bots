#!/usr/bin/env python3

"""
This script implements a simple Telegram bot that echoes back
any message it receives. It uses long polling to check for
new messages
"""

import os

import requests

TOKEN = os.environ['BOT_TOKEN'] # presetup with export or env
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

def process_updates(update):
    if 'message' in update:
        msg = update['message']
        msg_txt = msg['text']
        chat_id = msg['chat']['id']
        user = msg['from']['username']
        print(f"Message read from {user}")
        # Echo back the message
        msg_params = {
            'chat_id' : chat_id,
            'text' : msg_txt
        }
        requests.post(f"{BASE_URL}/sendMessage", params=msg_params)

# Update Parameters
# - offset: Ensures we don't process the same update twice
# - timeout: Maximum time to wait for new updates (in seconds)
# - allowed_updates: Update types the bot will receive
update_params = {
        'offset' : 520691962,
        'timeout' : 300,
        'allowed_updates' : ['message']
}

updates = []
try:
    while True:
    # Process the updates
        res_json = requests.get(f"{BASE_URL}/getUpdates", update_params).json()
        if res_json['ok']:
            updates = res_json['result']
            for update in updates:
                process_updates(update)
                print(f"Message echoed")
            else:
                print(f"Update {update['update_id']} ignored")
        
        # Telegram won't send again the updates below the offset
        if updates: 
            update_params['offset'] = updates[-1]['update_id'] + 1
except KeyboardInterrupt:
    print('\nShutting down echo. Processing remaining updates if any')
    for update in updates:
        process_updates(update)
    print('Program ended')
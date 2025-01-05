#!/usr/bin/env python3

"""
This script implements a simple Telegram bot that handles two global commands:
start and help. When a text message is received it echoes back
"""

import os
import sys

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

while True:
    # Process the updates
    res_json = requests.get(f"{BASE_URL}/getUpdates", update_params).json()
    if res_json['ok']:
        updates = res_json['result']
        for update in updates:
            # Process only incoming messages
            if 'message' in update:
                msg = update['message']
                if command.is_command(msg):
                    command.execute(msg)
                else: # Echo back the message
                    user = msg['from']['username']
                    print(f"Message read from {user}")
                    msg_params = {
                        'chat_id' : msg['chat']['id'],
                        'text' : msg['text']
                    }
                    requests.post(f"{BASE_URL}/sendMessage", params=msg_params)
                    print(f"Message echoed")
            else:
                print(f"Update {update['update_id']} ignored")
        
        # Telegram won't send again the updates below the offset
        if updates: 
            update_params['offset'] = updates[-1]['update_id'] + 1
        elif update_params['offset'] > 0:
            print('Nothing to read, exiting')
            sys.exit()

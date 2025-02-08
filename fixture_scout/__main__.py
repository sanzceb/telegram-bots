#!/usr/bin/env python3
import os

from . import bot
from . import telegram

TOKEN = os.environ['BOT_TOKEN'] # presetup with export or env
BASE_URL = "https://api.telegram.org"

client = telegram.TelegramClient(TOKEN, BASE_URL)
bot = bot.Bot(client)

try:
    client.start()
except KeyboardInterrupt:
    client.stop()

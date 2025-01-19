#!/usr/bin/env python3
import os

from bot import Bot
from telegram import TelegramClient

TOKEN = os.environ['BOT_TOKEN'] # presetup with export or env
BASE_URL = "https://api.telegram.org"

client = TelegramClient(TOKEN, BASE_URL)
bot = Bot(client)

try:
    client.start()
except KeyboardInterrupt:
    client.stop()

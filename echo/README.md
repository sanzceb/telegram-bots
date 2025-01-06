# Telegram Echo Bot

A simple Telegram bot implementation that echoes back the messages it receives,
demonstrating a basic functionality using long polling.

## Key Concepts Learned

1. **Long Polling Strategy**
   - Mantaining persistent connection with Telegram API
   - Setting a timeout to allow a more efficient communication with the server.

2. **Bot API Interaction**
   - Base URL structure: `https://api.telegram.org/bot<TOKEN>`
   - Endpoints utilized:
     - `/getUpdates`: Receives new messages
     - `/sendMessage`: Sends echo responses

3. **Message Handling**
   - The response object from `requests` can be managed as a json dict.
   - Manipulating an offset to avoid processing updates multiple times.
   - Message metadata extraction using JSON API.

## Setup and Configuration

1. Run the [basic setup](https://github.com/sanzceb/telegram-bots?tab=readme-ov-file#installation)

2. Run the bot (within the virtual enviroment):

```bash
python -m echo
```

import requests

class TelegramClient:
    
    def __init__(self, apikey, BASE_URL):
        self.apiKey = apikey
        self.URL = f"{BASE_URL}/bot{apikey}"
        self._offset = 520692050
    
    def send_text_message(self, chat_id, text):
        params = {'text' : text, 'chat_id' : chat_id}
        requests.post(f"{self.URL}/sendMessage", params=params)

    def register(self, bot):
        self.bot = bot
    
    def start(self):
        while True:
            updates = self.__updates()
            for update in updates:
                self.__process_update(update) 
                self.__set_offset(update)

    def stop(self):
        print('\nShutting down fixture_scout. \
              Processing remaining updates if any')
        updates = self.__updates(0)
        for update in updates:
            self.__process_update(update)
            self.__set_offset(update)

    def __process_update(self, update):
        if 'message' in update:
            msg = update['message']
            self.bot.handle_msg(msg)
        else:
            print(f"Update {update['update_id']} ignored")
    
    def __updates(self, timeout=3000):
        update_params = {
            'offset' : self._offset,
            'timeout' : timeout,
            'allowed_updates' : ['message']
        }
        res_json = requests.get(f"{self.URL}/getUpdates", update_params).json()
        updates = []
        if res_json['ok']:
            updates = res_json['result']
        return updates
    
    def __set_offset(self, update):
        # Telegram won't send again the updates below the offset
        self._offset = update['update_id'] + 1

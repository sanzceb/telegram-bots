
#import fixture

class Bot:
    def __init__(self, msg_client):
        self.msg_client = msg_client
        msg_client.register(self)

    @staticmethod
    def is_command(msg):
        return ('text' in msg) and (msg['text'].startswith('/'))
    
    def handle_msg(self, msg):
        if not Bot.is_command(msg): 
            self._help({'chat_id' : msg['chat']['id']})
            return
        cmd = msg['text'].removeprefix('/').split(' ', 1)
        cmdname = cmd[0]
        cmdargs = cmd[1] if len(cmd) > 1 else None
        self._execute(cmdname, cmdargs, msg)
    
    
    def _execute(self, cmdname, cmdargs, msg):
        chat_id = msg['chat']['id']
        if cmdname == 'start':
            self._start(chat_id)
        elif cmdname == 'fixtures':
            team = cmdargs if cmdargs else 'your team'
            self._fixtures(chat_id, team)
        else:
            self._help(chat_id)
    
    def _start(self, chat_id):
        txt = "I am fixture scout, ask me about the upcoming matches of your \
        team by using the command /fixture followed by the name of your \
        favourite team."
        self.msg_client.send_text_message(chat_id, txt)
    
    def _help(self, chat_id):
        txt = "Use the command /fixture followed by the name of your team"
        self.msg_client.send_text_message(chat_id, txt)

    def _fixtures(self, chat_id, team):
        txt = f"Soon I will how you the upcoming matches of {team}"
        self.msg_client.send_text_message(chat_id, txt)
    

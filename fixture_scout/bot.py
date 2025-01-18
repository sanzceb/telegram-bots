
#import fixture

class Bot:
    def __init__(self, msg_client):
        self.msg_client = msg_client
        msg_client.register(self.handle_msg)

    @staticmethod
    def __is_command(msg):
        return ('text' in msg) and (msg['text'].startswith('/'))
    
    def handle_msg(self, msg):
        if not __is_command(msg): 
            self._help({'chat_id' : msg['chat']['id']})
            return
        cmd = msg['text'].removeprefix('/').split(' ', 1)
        cmdname = cmd[0]
        cmdargs = cmd[1] if len(cmd) > 1 else None
        self._execute(cmdname, cmdargs, msg)
    
    
    def _execute(self, cmdname, cmdargs, msg):
        params = {'chat_id' : msg['chat']['id']}
        if cmdname == 'start':
            self._start(params)
        elif cmdname == 'fixtures':
            self._fixtures(params, cmdargs)
        else:
            self._help()
    
    def _start(self, params):
        txt = "I am fixture scout, ask me about the upcoming matches of your \
        team by using the command /fixture followed by the name of your \
        favourite team."
        self.msg_client.send_text(params['chat_id'], txt)
    
    def _help(self, params):
        raise NotImplementedError

    def _fixtures(self, params, cmdargs):
        raise NotImplementedError
    

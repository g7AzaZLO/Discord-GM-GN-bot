# -*- coding: utf-8 -*-

import requests as req
from datetime import datetime
from websocket import create_connection
from threading import Timer
import random

buffer_list_message = []

class Connection:
    def __init__(self, token, channelid, message, timer, name, random=0):
        self.token = token
        self.channelid = channelid
        self.message = message
        self.timer = timer
        self.log = []
        self.name = name
        self.thread = None
        self.random = random

    def get_name(self):
        return self.name

    def get_token(self):
        return self.token

    def get_channelid(self):
        return self.channelid

    def get_message(self):
        return self.message

    def get_timer(self):
        return self.timer

    def get_log(self):
        return self.log

    def get_random_message(self):
        file_message = open('message.txt', 'r', encoding='utf-8')
        list_message = []
        for line in file_message:
            list_message.append(line.strip())
        return (random.choice(list_message))

    def get_smart_random_message(self):
        global buffer_list_message
        file_message = open('message.txt', 'r', encoding='utf-8')
        list_message = []
        for line in file_message:
            list_message.append(line.strip())
        while True:
            if list(set(list_message) - set(buffer_list_message)) == []:
                buffer_list_message = []
            un_message = random.choice(list_message)
            if un_message not in buffer_list_message:
                buffer_list_message.append(un_message)
                return un_message

    def set_token(self, new_token):
        self.token = new_token

    def set_channelid(self, new_channelid):
        self.channelid = new_channelid

    def set_message(self, new_message):
        self.message = new_message

    def set_timer(self, new_timer):
        self.timer = new_timer

    def set_name(self, new_name):
        self.name = new_name

    def add_log(self, new_log):
        self.log.append(new_log)

    def stop_thread(self):
        try:
            self.thread.cancel()
            if self.thread is not None:
                self.stop_thread()
        except RecursionError:
            pass
        except:
            print('ERROR произошла ошибка, попробуйте еще раз')

    def send_message(self):
        token = self.token
        channelid = self.channelid
        if self.random == 1:
            message = self.get_random_message()
        elif self.random == 2:
            message = self.get_smart_random_message()
        else:
            message = self.message
        timer = int(self.timer)
        s = req.session()
        s.headers.update({'authorization': token, 'Content-Type': 'application/json'})
        payload = {"content": message, "tts": False}
        ws = create_connection("wss://gateway.discord.gg/")
        data = '''
        {
            "op": 2,
            "d":{
                "token": "%s",
                "properties": {
                    "$os": "linux",
                    "$browser": "ubuntu",
                    "$device": "ubuntu"
                },
            }
        }
        ''' % token
        ws.send(data)
        b = s.post("https://discordapp.com/api/v6/channels/%s/messages" % channelid, json=payload)
        try:
            ws.close()
        except:
            pass
        current_datetime = datetime.now()
        log = ("[X] " + str(current_datetime) + " | Сообщение '" + str(message) + "' отправлено в " + channelid)
        self.add_log(log)
        thread = Timer(timer, self.send_message)
        thread.start()
        self.thread = thread
        return

    def __del__(self):
        print("")

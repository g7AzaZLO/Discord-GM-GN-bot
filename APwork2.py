import requests as req
import schedule
from time import sleep, time
from datetime import datetime
from websocket import create_connection
print("""
╔═══╗╔╗─╔╗╔════╗╔═══╗╔═══╗╔╗─╔╗╔═══╗╔════╗
║╔═╗║║║─║║║╔╗╔╗║║╔═╗║║╔═╗║║║─║║║╔═╗║║╔╗╔╗║ 
║║─║║║║─║║╚╝║║╚╝║║─║║║║─╚╝║╚═╝║║║─║║╚╝║║╚╝
║╚═╝║║║─║║──║║──║║─║║║║─╔╗║╔═╗║║╚═╝║──║║──
║╔═╗║║╚═╝║──║║──║╚═╝║║╚═╝║║║─║║║╔═╗║──║║── By 
╚╝─╚╝╚═══╝──╚╝──╚═══╝╚═══╝╚╝─╚╝╚╝─╚╝──╚╝──    AzaZlo""")


token = input("[X] Вставьте токен юзера от которого будет производится отправка\n>> ")
channelid = input("[X] Вставьте id канала в который будут отправляться сообщения (пользователь должен находиться на сервере)\n>> ")
message = input("[X] Введите сообщение которое нужно отправлять в чат\n")
question = input('[X] Введите "1" для задержки в секундах, "2" в минутах, "3" в часах, "4" в днях\n>> ')
timer = input("[X] Введите через какое количество секунд/минут/часов/дней будет отправляться сообщение\n>> ")


def sendMessage(token, channelid, message):
    s = req.session()
    message = message
    s.headers.update({'authorization': token, 'Content-Type': 'application/json'})
    payload = {"content":message,"tts":False}
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
    print("[X] " + str(current_datetime) + " | Сообщение удачно отправлено")
    return


def time():
    sendMessage(token, channelid, message)
if question == "1":
    schedule.every(int(timer)).seconds.do(time)
elif question == "2":
    schedule.every(int(timer)).minutes.do(time)
elif question == "3":
    schedule.every(int(timer)).hours.do(time)
elif question == "4":
    schedule.every(int(timer)).days.do(time)
else:
    print("[X] Указано неверное значение задержки")
print("[X] Автоотправка сообщений успешно запущена, приятного пользования.")
while True:
    schedule.run_pending()
    sleep(1)

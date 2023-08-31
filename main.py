import threading as th
from cConnection import Connection
import os

print("""
░█████╗░██╗░░░██╗████████╗░█████╗░░██████╗░███╗░░░███╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝░████╗░████║
███████║██║░░░██║░░░██║░░░██║░░██║██║░░██╗░██╔████╔██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░╚██╗██║╚██╔╝██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝╚██████╔╝██║░╚═╝░██║ By
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░░░░╚═╝   AzaZlo""")

all_threads = {}


def get_all_threads_key():
    for key in all_threads.keys():
        print(key)


all_thread_names = []
def new_thread():
    global all_thread_names
    token = input("[X] Вставьте токен юзера от которого будет производится отправка\n >> ")
    channelid = input("[X] Вставьте id канала в который будут отправляться сообщения (пользователь должен находиться на сервере)\n >> ")
    message = input("[X] Введите сообщение которое нужно отправлять в чат\n >> ")
    timer = input("[X] Введите переодичность отправки в секундах\n >> ")
    name = input("[X] Введите уникальное название процесса\n >> ")
    if name in all_thread_names:
        print('ERROR: Такой процесс  уже существует, введите другое название')
    else:
        new_con = Connection(token, channelid, message, timer, name)
        new_con.send_message()
        all_threads[new_con.name] = new_con
        all_thread_names.append(new_con.name)
        print('Процесс запущен!\n')


def main():
    global all_thread_names
    while True:
        print(
            '1) Создать новый процесс\n2) Удалить процесс\n3) Просмотреть лог процесса\n4) Список процессов\nq) Выход\n')
        switch = input(' >> ')
        if switch == '1':
            new_thread()
        elif switch == '2':
            print("Введите название процесса:\n")
            name_thread = input(' >> ')
            try:
                buffer = all_threads[name_thread]
                buffer.stop_thread()
                del all_threads[name_thread]
                print('Удален из справочника процессов')
                all_thread_names.remove(name_thread)
                print('Удален из списка имен')
            except KeyError:
                print('ERROR: такого процесса не существует')

        elif switch == '3':
            print("Введите название процесса:\n")
            name_thread = input(' >> ')
            try:
                print("Логи процесса " + name_thread + "\n---------------------")
                buffer = all_threads[name_thread]
                logs = buffer.get_log()
                for i in logs:
                    print(i)
                print('---------------------')
            except KeyError:
                print('ERROR: такого процесса не существует')
        elif switch == '4':
            print('Все процессы:\n---------------------')
            get_all_threads_key()
            print('---------------------')
        elif switch == '5':
            print(th.enumerate())
        elif switch == 'q':
            os.abort()
        else:
            print('\nУказан неверный номер действия\n')


main()

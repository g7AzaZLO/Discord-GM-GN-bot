# -*- coding: utf-8 -*-

import threading as th
from cConnection import Connection
import os
import colorama
from colorama import Fore, Style, init
import random

init()

print(Fore.CYAN + """
░█████╗░██╗░░░██╗████████╗░█████╗░░██████╗░███╗░░░███╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝░████╗░████║
███████║██║░░░██║░░░██║░░░██║░░██║██║░░██╗░██╔████╔██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░╚██╗██║╚██╔╝██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝╚██████╔╝██║░╚═╝░██║ By
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░░░░╚═╝   [G7]AzaZlo""")
print(Style.RESET_ALL)
all_threads = {}


def get_all_threads_key():
    for key in all_threads.keys():
        print(key)


all_thread_names = []


def new_thread():
    global all_thread_names
    token = input("[X] Вставьте токен юзера от которого будет производится отправка\n >> ")
    channelid = input(
        "[X] Вставьте id канала в который будут отправляться сообщения (пользователь должен находиться на сервере)\n >> ")
    message = input("[X] Введите сообщение которое нужно отправлять в чат\n >> ")
    timer = input("[X] Введите переодичность отправки в секундах\n >> ")
    name = input("[X] Введите уникальное название процесса\n >> ")
    if name in all_thread_names:
        print(Fore.RED + '\nERROR: Такой процесс  уже существует, введите другое название')
        print(Style.RESET_ALL)
    else:
        new_con = Connection(token, channelid, message, timer, name)
        new_con.send_message()
        all_threads[new_con.name] = new_con
        all_thread_names.append(new_con.name)
        print(Fore.GREEN + 'Процесс запущен!\n')
        print(Style.RESET_ALL)


def table_thread():
    global all_thread_names
    file_token = open('token.txt', 'r', encoding='utf-8')
    list_token = []
    for line in file_token:
        list_token.append(line.strip())
    file_channel = open('channel.txt', 'r', encoding='utf-8')
    list_channel = []
    for line in file_channel:
        list_channel.append(line.strip())
    message = input('Введите сообщение которое будет отправлено\n >> ')
    timer = input("[X] Введите переодичность отправки в секундах\n >> ")
    for line_token in list_token:
        for line_channel in list_channel:
            token = line_token
            channelid = line_channel
            name = f'{token}_{channelid}'
            if name in all_thread_names:
                print(Fore.RED + '\nERROR: Такой процесс  уже существует')
                print(Style.RESET_ALL)
            else:
                new_con = Connection(token, channelid, message, timer, name)
                new_con.send_message()
                all_threads[new_con.name] = new_con
                all_thread_names.append(new_con.name)
                print(Fore.GREEN + 'Процесс запущен!\n')
                print(Style.RESET_ALL)


def random_message(choise):
    global all_thread_names
    if choise == 1:
        token = input("[X] Вставьте токен юзера от которого будет производится отправка\n >> ")
        channelid = input(
            "[X] Вставьте id канала в который будут отправляться сообщения (пользователь должен находиться на сервере)\n >> ")
        timer = input("[X] Введите переодичность отправки в секундах\n >> ")
        name = input("[X] Введите уникальное название процесса\n >> ")
        if name in all_thread_names:
            print(Fore.RED + '\nERROR: Такой процесс  уже существует, введите другое название')
            print(Style.RESET_ALL)
        else:
            message = None
            new_con = Connection(token, channelid, message, timer, name, random=1)
            new_con.send_message()
            all_threads[new_con.name] = new_con
            all_thread_names.append(new_con.name)
            print(Fore.GREEN + 'Процесс запущен!\n')
            print(Style.RESET_ALL)
    elif choise == 2:
        token = input("[X] Вставьте токен юзера от которого будет производится отправка\n >> ")
        channelid = input(
            "[X] Вставьте id канала в который будут отправляться сообщения (пользователь должен находиться на сервере)\n >> ")
        timer = input("[X] Введите переодичность отправки в секундах\n >> ")
        name = input("[X] Введите уникальное название процесса\n >> ")
        if name in all_thread_names:
            print(Fore.RED + '\nERROR: Такой процесс  уже существует, введите другое название')
            print(Style.RESET_ALL)
        else:
            message = None
            new_con = Connection(token, channelid, message, timer, name, random=2)
            new_con.send_message()
            all_threads[new_con.name] = new_con
            all_thread_names.append(new_con.name)
            print(Fore.GREEN + 'Процесс запущен!\n')
            print(Style.RESET_ALL)
    else:
        print(Fore.RED + 'ERROR: такого варианта')
        print(Style.RESET_ALL)


def main():
    global all_thread_names
    while True:
        print(
            '1) Создать новый процесс\n2) Удалить процесс\n3) Просмотреть лог процесса\n4) Список процессов\n5) База токенов х база каналов х время\n6) Отправка рандом сообщения из файла\nq) Выход\n')
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
                print(Fore.RED + '\nERROR: такого процесса не существует')
                print(Style.RESET_ALL)

        elif switch == '3':
            print("Введите название процесса:\n")
            name_thread = input(' >> ')
            try:
                print(Fore.YELLOW + "Логи процесса " + name_thread + "\n---------------------")
                buffer = all_threads[name_thread]
                logs = buffer.get_log()
                for i in logs:
                    print(i)
                print('---------------------')
                print(Style.RESET_ALL)
            except KeyError:
                print(Fore.RED + '\nERROR: такого процесса не существует')
                print(Style.RESET_ALL)
        elif switch == '4':
            print('Все процессы:\n---------------------')
            get_all_threads_key()
            print('---------------------')
        elif switch == '5':
            print('Режим создания процессов для большого  количество аккаунтов, с большим количеством каналов')
            print('В файле token.txt укажите токены всех аккаунтов. Каждый токен на новой строке')
            print('В файле channel.txt укажите id всех каналов, в которые должна происходить рассылка')
            print('каждый id на новой строке(пользователь должен находиться на сервере)')
            x = input("Напишите 'start', когда заполните файлы, для начала работы программы\n >> ")
            if x == 'start':
                print('Запуск')
                table_thread()
            else:
                print(Fore.RED + '\nERROR: Команды не существует, проверьте не опечатались ли вы')
                print(Style.RESET_ALL)
        elif switch == '6':
            print('Режим отправки рандомных сообщений')
            print('Список сообщений, которые будут выбираться на угад запишите в файл message.txt')
            print('Кажое новое сообщение на новой строке')
            print(Fore.YELLOW + 'WARNING: если слишком часто писать сообщения, то вас могут забанить как бота')
            print(Style.RESET_ALL)
            print('')
            print('1) Использовать обычный рандом')
            print(
                '2) Использовать умный рандом(Ни один аккаунт не повторит фразу с другим, пока не кончатся все сообщения в файле)')
            x = input("\n >> ")
            if x == '1':
                print('Запуск')
                random_message(choise=1)
            elif x == '2':
                print('Запуск')
                random_message(choise=2)
            else:
                print(Fore.RED + '\nERROR: Команды не существует, проверьте не опечатались ли вы')
                print(Style.RESET_ALL)
        elif switch == 'q':
            os.abort()
        else:
            print(Fore.RED + '\nERROR: Указан неверный номер действия\n')
            print(Style.RESET_ALL)


main()

from bot import *

with open("/home/cubeuser/token.txt") as f:
    auth_token = f.readline()

action = input("Введите команду: ")
if action.upper() == "Регистрация".upper():
    register()
elif action.upper() == "Авторизация".upper():
    auth_token = auth()
    if auth_token != 0:
        print("Успешная авторизация")
    else:
        print("Ошибка авторизации")
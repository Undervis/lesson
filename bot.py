import requests
import json

base_url = "http://cinema.areas.su"


def register():
    email = input("Введите ваш Email: ")
    password = input("Введите пароль: ")
    firstName, lastName = input("Введите имя и фамилию: ").split()

    reg = requests.post(base_url + "/auth/register",
                        params={
                            "email": email,
                            "password": password,
                            "firstName": firstName,
                            "lastName": lastName
                        })
    if reg.status_code != 400:
        print("Успешная регистрация")
    else:
        print("Ошибка регистрации")


def auth():
    email = input("Введите ваш Email: ")
    password = input("Введите пароль: ")
    login = requests.post(base_url + "/auth/login",
                          params={
                              "email": email,
                              "password": password
                          })

    token = json.loads(login.text)["token"]
    with open("/home/cubeuser/token.txt", "w") as f:
        f.write(token)
        return token
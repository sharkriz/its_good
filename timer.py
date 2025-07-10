import time
import keyboard

start = time.time()  # Запоминаем время старта программы

print("Секундомер запущен! (Напишите Insert для выхода)")

while True:
    if keyboard.is_pressed("Insert"):
        exit()

    current_time = time.time() - start  # Прошедшее время в секундах
    hours = int(current_time // 3600)
    minutes = int((current_time % 3600) // 60)
    seconds = int(current_time % 60)

    print(f"\rПрошло времени:", hours, ":", minutes, ":", seconds, end=" ")  # вывод время на экран

    time.sleep(0.01)  # Ждём 0.01 секунду перед обновлением(чтобы не нагружать процессор). Сделано так мало для того, чтобы отслеживать нажатие Q.
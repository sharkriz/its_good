import time
import keyboard

start = time.time()

print("Секундомер запущен! (Напишите Insert для выхода)")

while True:
    if keyboard.is_pressed("Insert"):
        exit()

    current_time = time.time() - start
    hours = int(current_time // 3600)
    minutes = int((current_time % 3600) // 60)
    seconds = int(current_time % 60)

    print(f"\rПрошло времени:", hours, ":", minutes, ":", seconds, end="", flush=True)

    time.sleep(0.01)

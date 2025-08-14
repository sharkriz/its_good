from tkinter import Tk, Button, Label
from datetime import datetime

root = Tk()

root.geometry("300x200")
root.title("Секундомер")
root.resizable(width=False, height=False)

def start():
    button_start.pack_forget()
    button_stop.pack()
    show_second()

second = 0
after_id = ""

def show_second():
    global second, after_id
    after_id = root.after(1000, show_second)
    f_second = datetime.fromtimestamp(second).strftime("%M:%S")
    label_second["text"] = f_second
    second += 1

def stop():
    button_stop.pack_forget()
    button_continue.pack()
    button_reset.pack()
    root.after_cancel(after_id)

def continue_show_second():
    button_continue.pack_forget()
    button_reset.pack_forget()
    button_stop.pack()
    show_second()

def reset():
    global second
    button_continue.pack_forget()
    button_reset.pack_forget()
    button_start.pack()
    second = 0
    label_second["text"] = "00:00"

label_second = Label(root, text="00:00", font=("Comis Sans MS", 20, "bold"), width=15, pady=20)
label_second.pack()

button_start = Button(root, text="Старт", font=("Comic Sans MS", 15, "bold"), width=15, command=start)
button_start.pack()

button_stop = Button(root, text="Стоп", font=("Comic Sans MS", 15, "bold"), width=15, command=stop)

button_continue = Button(root, text="Продолжить", font=("Comic Sans MS", 15, "bold"), width=15, command=continue_show_second)

button_reset = Button(root, text="Сброс", font=("Comic Sans MS", 15, "bold"), width=15, command=reset)

root.mainloop()
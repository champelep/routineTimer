import time
import datetime
import os
from tkinter import *


morning_routine_1 =  "Toilet and Make Coffee"
morning_routine_2 = "Music and Reflect"
morning_routine_3 = "Read Quran"
morning_routine_4 = "Exercise and Visualize"
morRouTime1 = 3
morRouTime2 = 3
morRouTime3 = 3
morRouTime4 = 3

night_routine_1 = "Read Quran"
night_routine_2 = "Meditate"
night_routine_3 = "Observe your mind. Detachment"
nightRouTime1 = 3
nightRouTime2 = 3
nightRouTime3 = 3


# MORNING--------------------------------------------------------------------------------------------------------
def morning_countdown_1():
    total_seconds = morRouTime1
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        timer_label.config(text=f"{morning_routine_1}   {timer}")
        root.update()
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_1 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


def morning_countdown_2():
    total_seconds = morRouTime2
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        timer_label.config(text=f"{morning_routine_2}   {timer}")
        root.update()
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_2 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


def morning_countdown_3():
    total_seconds = morRouTime3
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        timer_label.config(text=f"{morning_routine_3}   {timer}")
        root.update()
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_3 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


def morning_countdown_4():
    total_seconds = morRouTime4
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        timer_label.config(text=f"{morning_routine_4}   {timer}")
        root.update()
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_4 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


# NIGHT--------------------------------------------------------------------------------------------------------
def night_countdown_1():
    total_seconds = nightRouTime1
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        timer_label.config(text=f"{night_routine_1}   {timer}")
        root.update()
        time.sleep(1)
        total_seconds -= 1
    print(night_routine_1 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


def night_countdown_2():
    total_seconds = nightRouTime2
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        timer_label.config(text=f"{night_routine_2}   {timer}")
        root.update()
        time.sleep(1)
        total_seconds -= 1
    print(night_routine_2 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


def night_countdown_3():
    total_seconds = nightRouTime3
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        timer_label.config(text=f"{night_routine_3}   {timer}")
        root.update()
        time.sleep(1)
        total_seconds -= 1
    print(night_routine_3 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')


# MAIN --------------------------------------------------------------------------------------------------------
def start_morning_routine():
    morning_countdown_1()
    morning_countdown_2()
    morning_countdown_3()
    morning_countdown_4()
    print("Have a good day")


def start_night_routine():
    night_countdown_1()
    night_countdown_2()
    night_countdown_3()


def quit_program():
    root.destroy()


root = Tk()
root.title("Morning and Night Routine")
root.geometry("800x600")
root.configure(bg="black")

title_label = Label(root, text="Morning and Night Routine", fg="white", bg="black", font=("Arial", 20))
title_label.pack(pady=20)

morning_button = Button(root, text="Start Morning Routine", command=start_morning_routine)
morning_button.pack(pady=10)

night_button = Button(root, text="Start Night Routine", command=start_night_routine)
night_button.pack(pady=10)

timer_label = Label(root, text="", fg="white", bg="black", font=("Arial", 16))
timer_label.pack(pady=20)

quit_button = Button(root, text="Quit", command=quit_program)
quit_button.pack(pady=10)

root.mainloop()

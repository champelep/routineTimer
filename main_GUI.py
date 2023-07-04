import tkinter as tk
from tkinter import messagebox
import time
import datetime
import os

morning_routine_1 = "Toilet and Make Coffee"
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


class RoutineWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Morning and Night Routines")
        self.configure(bg="black")
        self.geometry("200x200")
        self.label = tk.Label(self, text="Select Routine", fg="white", bg="black", font=("Arial", 20, "bold"))
        self.label.pack(pady=10)
        self.morning_button = tk.Button(self, text="Morning", command=self.start_morning_routine, font=("Arial", 16))
        self.morning_button.pack(pady=10)
        self.night_button = tk.Button(self, text="Night", command=self.start_night_routine, font=("Arial", 16))
        self.night_button.pack(pady=10)

    def start_morning_routine(self):
        self.morning_button.config(state=tk.DISABLED)
        self.night_button.config(state=tk.DISABLED)
        self.label.config(text="Morning Routine in Progress...")
        self.update()
        time.sleep(1)
        self.morning_routine()
        messagebox.showinfo("Morning Routine", "Morning routine completed!")
        self.reset()

    def start_night_routine(self):
        self.morning_button.config(state=tk.DISABLED)
        self.night_button.config(state=tk.DISABLED)
        self.label.config(text="Night Routine in Progress...")
        self.update()
        time.sleep(1)
        self.night_routine()
        messagebox.showinfo("Night Routine", "Night routine completed!")
        self.reset()

    def reset(self):
        self.morning_button.config(state=tk.NORMAL)
        self.night_button.config(state=tk.NORMAL)
        self.label.config(text="Select Routine")

    def morning_routine(self):
        self.countdown(morning_routine_1, morRouTime1)
        self.countdown(morning_routine_2, morRouTime2)
        self.countdown(morning_routine_3, morRouTime3)
        self.countdown(morning_routine_4, morRouTime4)

    def night_routine(self):
        self.countdown(night_routine_1, nightRouTime1)
        self.countdown(night_routine_2, nightRouTime2)
        self.countdown(night_routine_3, nightRouTime3)

    def countdown(self, routine, duration):
        total_seconds = duration
        while total_seconds > 0:
            self.label.config(text=f"{routine}: {datetime.timedelta(seconds=total_seconds)}")
            self.update()
            time.sleep(1)
            total_seconds -= 1

        self.label.config(text=f"{routine} is done.")
        self.update()
        time.sleep(1)
        os.system('afplay /System/Library/Sounds/Glass.aiff')
        os.system('afplay /System/Library/Sounds/Glass.aiff')
        os.system('afplay /System/Library/Sounds/Glass.aiff')


if __name__ == "__main__":
    app = RoutineWindow()
    app.mainloop()

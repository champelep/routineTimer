import time
import datetime
import os



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
        timer = datetime.timedelta(seconds = total_seconds)
        print(morning_routine_1+"   ", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_1 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')

def morning_countdown_2():
    total_seconds = morRouTime2
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(morning_routine_2+"   ", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_2 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')

def morning_countdown_3():
    total_seconds = morRouTime3
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(morning_routine_3+"   ", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_3 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')

def morning_countdown_4():
    total_seconds = morRouTime4
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(morning_routine_4+"   ", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(morning_routine_4 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')


# NIGHT--------------------------------------------------------------------------------------------------------
def night_countdown_1():
    total_seconds = nightRouTime1
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(night_routine_1+"   ", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(night_routine_1 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')

def night_countdown_2():
    total_seconds = nightRouTime2
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(night_routine_2+"   ", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(night_routine_2 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')

def night_countdown_3():
    total_seconds = nightRouTime3
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(night_routine_3+"   ", timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(night_routine_3 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')

#MAIN --------------------------------------------------------------------------------------------------------
def main():
    while True:
        when = input("Morning or Night? (Enter 'q' to quit): ").lower()
        if when == "morning":
            morning_countdown_1()
            morning_countdown_2()
            morning_countdown_3()
            morning_countdown_4()
            print ("Have a good day")
            break
        elif when == "night":
            night_countdown_1()
            night_countdown_2()
            night_countdown_3()
            break
        elif when == "q":
            break
        else:
            print("Please enter a valid command.")


main()

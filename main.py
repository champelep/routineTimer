import time
import datetime
import os



morning_routine_1 =  "first morning"
morning_routine_2 = "second morning"
morning_routine_3 = "third morning"
morRouTime1 = 600
morRouTime2 = 600
morRouTime3 = 600

night_routine_1 =  "first night"
night_routine_2 = "second night"
night_routine_3 = "third night"
nightRouTime1 = 600
nightRouTime2 = 600
nightRouTime3 = 600


 
# MORNING--------------------------------------------------------------------------------------------------------
def morning_countdown_1():
    morRouTime1 = 3
    while morRouTime1 > 0:
        timer = datetime.timedelta(seconds = morRouTime1)
        print(morning_routine_1+"   ", timer, end="\r")
        time.sleep(1)
        morRouTime1 -= 1
    print(morning_routine_1 + "  is done  ")
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    os.system('afplay /System/Library/Sounds/Glass.aiff')
    #os.system('say "your program has finished"')


# NIGHT--------------------------------------------------------------------------------------------------------

#MAIN --------------------------------------------------------------------------------------------------------
def main():
    while True:
        when = input("Morning or Night? (Enter 'q' to quit): ").lower()
        if when == "morning":
            morning_countdown_1()
            morning_countdown_2()
            morning_countdown_3()
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

from user import User
from workout import Workout
from workout import log_workout
from storage import show_log
name = input("Please enter your name: ")
U1 = User(name)

while True :
    print("Welcome",U1.name,"please choose out of the following options")
    print("Log Workout - Type A")
    print("Show History - Type B")
    print("Exit - Type C")
    a = input("Please enter your response :")
    if a == "A":
        log_workout()
    elif a == "B":
        print(show_log())
    elif a == "C":
        break
    else:
        print("Please choose out of the options")
    
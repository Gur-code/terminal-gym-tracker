from datetime import datetime
current = datetime.now()
current_str1 = current.strftime("%d-%B-%Y, %I:%M %p")
current_str2 = current.strftime("%I:%M %p")

class Workout:
    def __init__(self, exercise, weight, reps):
        self.exercise = exercise
        self.weight = weight
        self.reps = reps
    
def log_workout():
    ex = input("Enter the name of the exercise :")
    we = int(input("Enter the weight you used in Kgs :"))
    re = int(input("Enter the amount of reps you did :"))
    W1 = Workout(ex, we, re)
    print("You did",W1.exercise,"of", W1.weight, "Kgs for",W1.reps,"reps.")
    print("Workout Recorded at",current_str2)
    save_workout(W1)


def save_workout(abc):
    with open ("data.txt","a") as f:
        f.write(f"{current_str1} \n")
        f.write(f"Exercise -{abc.exercise}\n")
        f.write(f"Weight - {abc.weight}\n")
        f.write(f"Reps - {abc.reps}\n")
        

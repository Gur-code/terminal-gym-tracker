def show_log():
    with open ("data.txt","r") as f:
        abc = f.read()
        return abc


def Personal_rec(word): 
    with open("data.txt","r") as f:
        PR = 0
        while True:
            abc = f.readline()
            if abc == "":
                break
            if (abc.find(word)!= -1):
                W = f.readline()
                if PR <= int(W[9:]):
                    PR = int(W[9:])
        print("Your personal record for",word,"is :",PR,"Kgs")

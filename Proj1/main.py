import random
# 1 - snake 
# -1 - water 
# 0 gun
computer = random.choice([-1,0,1])
you = input("Enter your choice: ")
youDict = {
    "s":1, "w":-1,"g":0
}
youNum = youDict[you]

if(computer == youNum):
    print("It's a draw")
else:
    if(computer == -1 and youNum == 1):
        print("You Win!")

    elif(computer == -1 and youNum == 0):
        print("You Lose...")

    elif(computer == 1 and youNum == -1):
        print("You Lose...")

    elif(computer == 1 and youNum == 0):
        print("You Win!")

    elif(computer == 0 and youNum == -1):
        print("You Win!")

    elif(computer == 0 and youNum == 1):
        print("You Lose...")

    else:
        print("Something went wrong")
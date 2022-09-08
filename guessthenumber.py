import random
import time

def test(ran):
    i = 1
    while(i<6):
        time.sleep(1)
        gus = int(input("guess a number\n"))
        if(gus == ran):
            print("You won !\n")
            break
        elif(gus > ran):
            time.sleep(1)
            print("Your number is greater")
        else:
            print("Your number is lesser\n")
        print("you have {} times left\n".format(5-i))
        i = i + 1
    else:
        print("You lost\n")
    print("Answer:{}\n".format(ran))

abc = input("Do you want to play guessing game ?").lower()
while(abc=='yes'):

    print("\n")
    print("Welcome to Number guessing game")
    time.sleep(1)
    print("You have 5 chances to guess the correct number !\n")
    time.sleep(1)
    level = input("What level do you want to choose ?? (easy / medium / hard)").lower()

    if(level == 'easy'):
        ran =  random.randint(0,10)
        #print(ran)
        print("Number range is from 0 to 10")
        test(ran)

    elif(level == 'medium'):
        ran =  random.randint(0,50)
        #print(ran)
        print("Number range is from 0 to 50")
        test(ran)

    elif(level == 'hard'):
        ran =  random.randint(0,100)
        #print(ran)
        print("Number range is from 0 to 100")
        test(ran)
    
    abc = input("Do you want to play the game again ?\n").lower()
else:
    print("TaTa bye bye")
    


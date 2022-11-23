import random
print ("Guess the Animal")
print("To win this game you have to guess minimum 2 animals correctly, You have one clue")
print("Lets Go")
print ("Choose a number")
li=["1", "2" ,"3" , "4"]
random.shuffle(li)
print(li)
alphabet=input()
if alphabet=="a":
    print("I have no sword, I have no spear yet rule a horde which many fear, my soldier fight with a wicket sting, I rule with might, yet am no king. What am I?")
    answer=input()
    if answer!="Bee":
        print("You want some clue? Yes or No")
        clue=input()
        if clue=="Yes":
            print("When it stings it hurts")
            second_try=input()
            if second_try=="Bee":
                print("You are right!")
            elif second_try!="Bee":
                print("You have lost your clue")
                print("I am frog")

        elif clue== "No":
            print("You have kept your clue")

            
        else:
            print("You lost!")
    elif answer=="Bee":
        print("You won")
elif alphabet== "c":
    print("I have four legs but no tail, usually you can hear me only at night. What am I?")
    answer=input()
    if answer!="Frog":
        print("You want some clue? Yes or No")
        clue=input()
        if clue=="Yes":
            print("They are loud at night")
            second_try=input()
            if second_try=="Frog":
                print("You are right")
            elif second_try!="Frog":
                print("You have lost your clue")
                print("I am frog")
        elif clue=="No":
            print("You have kept your clue")
        else:
            print("You lost")
    elif answer=="Frog":
        print("You are right")
    
elif alphabet=="d":
    print("I am too big to be a pet, I might be large with a small head, but once i've seen something i will never forget")
    answer=input()
    if answer!="Elephant":
        print("You want some clue? Yes or No")
        clue=input()
        if clue=="Yes":
            print("It has huge trunk")
            second_try=input()
            if second_try=="Elephant":
                print("You are right")
            elif second_try!="Elephant":
                print("You have lost your clue")
                print("I am Elephant")

        elif clue== "No":
            print("You have kept your clue")

            
        else:
            print("You lost")
    elif answer=="Elephant":
        print("You are right!")
elif alphabet=="b":
    print("I am one of the most beautiful bird you will find with two eyes in front and hundreds behind. Who am I?")
    answer=input()
    if answer!="Peacock":
        print("You want some clue? Yes or No")
        clue=input()
        if clue=="Yes":
            print("I love to dance")
            second_try=input()
            if second_try=="Peacock":
                print("You are right")
            elif second_try!="Peacock":
                print("You have lost your clue")
                print("I am Elephant")

        elif clue== "No":
            print("You have kept your clue")

            
        else:
            print("You lost")
    elif answer=="Peacock":
        print("You are right!")
import random

def roll_dice():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print ("Roll the dice? (y/n): ")
    user_response = input().lower()
    if user_response == "y":
        print(f"({num1}, {num2})")
    elif user_response ==  "n":
        print("Thanks for playing")
    else:
        print("Invalid Choice!")
roll_dice()
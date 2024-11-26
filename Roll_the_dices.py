import random


def roll_the_dice_1():
    return random.randint(1, 6)

def roll_the_dice_2():
    return random.randint(1, 6)

def rolls():
    return roll_the_dice_1(), roll_the_dice_2()

def user_answer():
    while True:
        user_answer = input("Enter your answer (y/n): ")
        if user_answer.lower() == "y":
            user_answer = True
            break
        elif user_answer.lower() == "n":
            user_answer = False
            break
        else:
            print("\nWrong answer! Enter correct answer again! (y/n): ")
    return user_answer

def game_roll():
    my_name = input("Hello! What's your name?: ")
    print(f"\nNice to meet you, {my_name}. Do you want to roll the dices?")
    while True:
        my_answer = user_answer()
        if my_answer:
            dice_1, dice_2 = rolls()
            print(f"\nYour dices are: {dice_1}, {dice_2}")
            if dice_1 == dice_2:
                print("Wow! It's a double!")
            print("\nDo you want to roll again?: ")
        else:
            print(f"\nOk. Have a good day, {my_name}! Bye!")
            break

game_roll()
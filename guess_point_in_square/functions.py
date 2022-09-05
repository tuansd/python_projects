"""
Tuan(Tony) Tran
"""
import random
from classes import Point, Square


# def show_game(is_playing):
def show_game():
    print('\nY')
    print("|")
    print("|")
    print("|             . point(x,y)")
    print("|")
    print("|__ __ __ __ __ X\n")


def ask_to_play():
    print("============ Let Guess ==============")
    print("\nAny key to Play")
    playing = input("q to Quit: ")

    if playing == "q" or playing == "Q":
        print("Thanks for playing! Play again soon.")
        return False

    return True


def what_level():
    while True:
        print("What level do you like to play: 1) Easy, 2) Medium, 3) Hard\n")
        try:
            level = input("Enter your level: ")
        except:
            print("Invalid level! Enter again")
            continue

        if level == "1" or level == "easy" or level == "Easy":
            return 15
        if level == "2" or level == "medium" or level == "Medium":
            return 10
        if level == "3" or level == "hard" or level == "Hard":
            return 5


def generate_secret_square(length):
    x = random.randint(0, 35)
    y = random.randint(0, 35)

    return Square(x, y, length)


def get_input_point():
    while True:
        print("Please guess your point(x,y) now:\n")
        x = y = 0
        try:
            x = int(input("X (0-50): "))
            y = int(input("Y (0-50): "))
        except:
            print("Invalid Input")

        if 0 <= x <= 50 and 0 <= y <= 50:
            return Point(x, y)
        else:
            print("Invalid input")


def play_game(square):
    while ask_to_play():
        show_game()
        point = get_input_point()
        square.is_in_square(point)

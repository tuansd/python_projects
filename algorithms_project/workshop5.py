'''
Python Guessing Game 3 ways: User Input, Linear Search, Binary Search
    Tuan(Tony) Tran - 2022
'''
import random

# Guess the Number by User Input:


def guess_random_num(tries, start, stop):
    guess_list = []

    secret_number = random.randint(start, stop)

    while tries != 0:
        print("Number of tries left: ", tries)

        try:
            while True:
                pick_number = int(input("Guess a number between 0 and 10: "))
                if pick_number in guess_list:
                    print(f"You already guessed this number {pick_number}")
                    print("Please enter different number")
                    continue
                else:
                    break

        except:
            print("Invalid Input")
            continue

        if pick_number == secret_number:
            print("\nYou guessed the correct number!")
            return
        elif pick_number < secret_number:
            print("\nGuess higher!")
        else:
            print("\nYGuess lower!")

        tries -= 1

        # store the user inputs
        guess_list.append(pick_number)
        print("Your Guessed: ", guess_list)

    print(f" {tries} You loss!")

# Guess the Number Computer Linear Search:
#     - Create a game where a program does the search for you.
#     - The search algorithm must run in O(n) - Linear Time


def guess_random_num_linear(tries, start, stop):

    the_number = random.randint(start, stop)

    print("The number for the program to guess is: ", the_number)

    for n in range(tries):
        print("Number of tried left: ", tries - n)
        random_number = random.randint(start, stop)
        print("The program is guessing: ", random_number)

        if random_number == the_number:
            print("\nThe program has guessed the correct number!")
            return True

    print("The program has failed to guess the correct number.")
    return False


# Guess the Number Computer Linear Search:
#     - Create a game where a program does the search for you.
#     - The search algorithm must run in O(log(n)) - Logarithmic Time


def guess_random_num_binary(tries, start, stop):

    the_number = random.randint(start, stop)

    print("The number for the program to guess is: ", the_number)

    lower_bound = start
    upper_bound = stop

    while lower_bound <= upper_bound and tries != 0:

        pivot_number = (upper_bound + lower_bound) // 2

        # print("Number of tried left: ", tries)
        random_number = random.randint(lower_bound, upper_bound)
        print("The program is guessing: ", random_number)

        if random_number == the_number:
            print("\nThe program has guessed the correct number!")
            return

        if pivot_number > the_number:
            print("Guessing lower!")
            upper_bound = pivot_number - 1

        else:
            print("Guessing higher!")
            lower_bound = pivot_number + 1

        tries -= 1

    print("The program has failed to guess the correct number.")


# Add bonus task 1 - 3 here
def guess_user_choice():

    try:
        tries = int(input("Enter the number of tries: "))
        start = int(input("Enter the START of range: "))
        stop = int(input("Enter the STOP of range: "))
    except:
        print("Invalid Input")
        return

    try:
        print("1. Guess the Number by User Input")
        print("2. Guess the Number by Linear Search")
        print("3. Guess the Number by Binary Search")
        option = input("Enter your option: ")
    except:
        print("Invalid Input")
        return

    if option == "1":
        guess_random_num(tries, start, stop)
    elif option == "2":
        guess_random_num_linear(tries, start, stop)
    elif option == "3":
        guess_random_num_binary(tries, start, stop)
    else:
        print("Invalid choice!")


def gambling_game():  # bonus task 4
    '''this is for bonus task 4 - make a game where you bet if the computer
    will win or not using the function from task two guess_random_num_linear(...).
    '''

    player_balance = 10

    while True:
        print("Your balance: $", player_balance)
        try:
            bet = int(input("\nEnter your bet (1-10): $"))
        except:
            print("\nInvalid bet")

        # check bet 1 to 10
        if bet < 1 or bet > 10:
            print("Invalid bet")
            continue

        if guess_random_num_linear(5, 0, 10):
            player_balance += bet
        else:
            player_balance -= bet

        if player_balance <= 0:
            print("\nYou lost!")

        if player_balance >= 50:
            print("\nYou WIN!")

        if player_balance <= 0 or player_balance >= 50:
            start_game = input("Any key to play again or 'q' to Quit: ")
            if start_game == 'q' or start_game == 'Q':
                print("Thanks for playing")
                return
            else:
                print("\nStart New game\n")
                player_balance = 10
                continue


# Test case 1
# guess_random_num(5, 0, 10)
# Test case #2
# guess_random_num_linear(5, 0, 10)
# Test case #3
# guess_random_num_binary(5, 0, 100)
# Test user choice Bonus Task 2
guess_user_choice()
# Test gambling game Bonus
# gambling_game()

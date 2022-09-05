"""
Tuan(Tony) Tran
"""
from classes import Point, Square

from functions import show_game, ask_to_play, get_input_point, generate_secret_square, what_level


NUMBER_PLAY = 5

highscore = NUMBER_PLAY

points_miss = set()

# Start playing game

while ask_to_play():

    # Start new game
    length = what_level()
    secret_square = generate_secret_square(length)
    points_miss = set()

    number_guess = 0
    while number_guess < NUMBER_PLAY:
        show_game()
        player_point = get_input_point()

        # Display square to test
        print("Square: ")
        secret_square.draw_square()

        if secret_square.is_in_square(player_point):
            print("\n🎉 Great Job! YOU WIN!")
            if number_guess < highscore:
                highscore = number_guess
                print("High Score is: ", highscore)

            break
        else:
            points_miss.add(tuple([player_point.x, player_point.y]))
            secret_square.compare_message(player_point)
            number_guess += 1

    # print out missing points
    print("++++++++++++++++++++++++")
    for p in points_miss:
        print("missing points", p[0], p[1])
    print("++++++++++++++++++++++++")
    if number_guess >= NUMBER_PLAY:
        print("\n🎃 SORRY! YOU LOST")
    print("End Game------------")
    print("number of guesses: ", number_guess)
    print("High Score is: ", highscore)

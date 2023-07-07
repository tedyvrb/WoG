import GuessGame
import MemoryGame
import CurrencyRouletteGame

def welcome(name):
    print(f'''Hello {name} and welcome to the Wold of Games (WoG).
Here you can fid many cool games to play.''')

def get_game():
    # print(type(game_choose), game_choose)
    return input('Please choose the game from 1 to 3: ')

def get_difficulty():
    return input('Please choose game difficulty from 1 to 5: ')

def is_digital(num):
    return num.isdigit()

def num_is_valid (num, max):
    if num > max or num < 1:
        return False
    else:
        return True

def play_again():
    your_choose = input('Want to play again? yes/no: ')
    if your_choose == 'yes':
        return True
    else:
        return False
def load_game():
    max_of_games = 3
    max_of_difficulty = 5
    game_num = 0
    game_difficulty = 0
    game_ok = False
    difficulty_ok = False

    print('''1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. MGuess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    # check the game number parameters
    while not game_ok:
        game_num = get_game()
        if is_digital(str(game_num)):
           if num_is_valid(int(game_num), max_of_games):
               game_ok = True

    #check the difficulty parameter is valid
    while not difficulty_ok:
        game_difficulty = get_difficulty()
        if is_digital(str(game_difficulty)):
            if num_is_valid(int(game_difficulty), max_of_difficulty):
                difficulty_ok = True

    game_num = int(game_num)
    game_difficulty = int(game_difficulty)

    # ==== check parameters ===========
    # game_num = 3
    # game_difficulty = 3
    print(f'Game = {game_num}, Difficulty = {game_difficulty}')
    # print(type (game_num))
    # print (type (game_difficulty))
    # ----------------------------------------

    # Play 3 Games
    go_to_the_game = True
    # Play game -= #1 =-
    if game_num == 1:
        while go_to_the_game:
            GuessGame.play(game_difficulty)
            go_to_the_game = play_again()

    # Play game -= #2 =-
    elif game_num == 2:
        while go_to_the_game:
            MemoryGame.play(game_difficulty)
            go_to_the_game = play_again()

    # Play game -= #3 =-
    elif game_num == 3:
        while go_to_the_game:
            CurrencyRouletteGame.play(game_difficulty)
            go_to_the_game = play_again()



    return game_num, game_difficulty



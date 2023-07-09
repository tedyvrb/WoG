import random
import time
import Score
import Utils

def game_explanation(difficulty):
    print(f'''We start the game
Programme generate {difficulty} random numbers from 1 to 100
Please type this numbers in write order if you type it correct you are win!!!''')
def generate_sequence(difficulty):
    list_of_numbers = []
    for i in range(difficulty):
        list_of_numbers.append(random.randint(1, 101))

    # print list !!!check!!!
    print(f'Secret list check: {list_of_numbers}')
    return list_of_numbers

def get_list_from_user(difficulty):
    list_of_numbers = []
    for i in range(difficulty):
        user_num = input(f'Enter number {i+1}: ')
        if user_num.isdigit():
            list_of_numbers.append(user_num)
        else:
            while not user_num.isdigit():
                user_num = input('Bad input try again: ')
            list_of_numbers.append(user_num)

    return list_of_numbers

def is_list_equal(list1, list2):
        if list1 == list2:
            return True
        else:
            return False

def play(difficulty):
    secret_list = []
    user_list = []

    game_explanation(difficulty)
    secret_list = generate_sequence(difficulty)
    print(f'Try to remember this list and type it again: {secret_list}')
    time.sleep(1)
    Utils.screen_clean()
    user_list = get_list_from_user(difficulty)
    user_list = [int(x) for x in user_list]

    # --------------------------------------------
    # print list check
    print(f'''Computer list check: {secret_list}
Users list check: {user_list}''')
    # --------------------------------------------

    if is_list_equal(secret_list, user_list):
        print('You WIN!!!')
        Score.add_score(difficulty)
        return True
    else:
        print('Looser!!!')
        return False

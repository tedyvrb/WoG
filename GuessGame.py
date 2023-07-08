import random
import Score
def game_explanation(difficulty):
    print(f'''We start the game
Programme generate the random number from 1 to {difficulty}
Tape the number, if you choose the same number as a computer you are win!!!''')


def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user():
    # my_num = input('Type your number: ')
    user_num = input(f'Enter number : ')
    while not user_num.isdigit():
        user_num = input('Bad input try again: ')
    return user_num

def compare_result(secret, get_guess_from_user):
    if secret != get_guess_from_user:
        return False
    else:
        return True

def play(difficulty):
    game_explanation(difficulty)
    secret = generate_number(difficulty)

    # check the secret
    print(f'My secret num CHECK: {secret}')

    user_number = get_guess_from_user()
    if compare_result(secret, int(user_number)):
        print('Your are WIN!!!')
        Score.add_score(difficulty)
        return True
    else:
        print('Looser try again )))')
        return False





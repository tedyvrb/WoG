import random

def game_explanation(difficulty):
    print(f'''We start the game
Programme generate the random number from 1 to {difficulty}
Choose the random number if you choose the same number you are win!!!''')


def generate_number(difficulty):
    start = 1
    return random.randint(start, difficulty)


def get_guess_from_user():
     return input('Type your number: ')

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

    user_number=get_guess_from_user()
    if compare_result(secret,int(user_number)):
        print('Your are WIN!!!')
    else:
        print('Looser try again )))')





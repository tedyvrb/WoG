import requests
import random

def game_explanation(difficulty):
    delta = 5 - int(difficulty)
    print(f'''We start the game
Programme generate random numbers from 1 to 100 for USD amount
Computer will convert this amount to ILS due to today gate
Try to guess how much it is in ILS..... 
if you type value +- {delta}  you are win!!!''')

def get_money_interval(amount_usd):
    base_currency = "USD"
    target_currency = "ILS"
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][target_currency]
    amount_nis = amount_usd * exchange_rate
    return amount_nis

def get_guess_from_user():
    amount_nis=input('Enter number amount in ILS : ')
    if amount_nis.isdigit():
        amount_nis = int(amount_nis)
    else:
        while not amount_nis.isdigit():
            amount_nis = input('Bad input try again: ')
    return int(amount_nis)


def play(difficulty):
    game_explanation(difficulty)
    amount_usd = random.randint(1, 101)
    print(f'Try to guess how much does {amount_usd} USD in ILS...')
    amount_nis = get_money_interval(amount_usd)

    print(f'Computer amount_nis CHECK: {amount_nis}')

    users_nis = get_guess_from_user()

    # --------------------------------------------
    # parameters check
    print(f'Computer amount_nis: {amount_nis}')
    print(f'Users users_nis: {users_nis}')
    # --------------------------------------------

    delta_nis = 5 - difficulty
    if abs(amount_nis - users_nis) < delta_nis:
        print('Yor are win!!!')
    else:
        print('Looser!!!!')


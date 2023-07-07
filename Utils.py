import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 500

def screen_clean():
    os.system('cls' if os.name == 'nt' else 'clear')

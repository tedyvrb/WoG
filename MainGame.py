from Live import load_game, welcome
import Score

# print(welcome('Helena'))
# return 2 parameters game_number and game_difficulty
# game_num, game_difficulty = load_game()
score_file = 'Scores.txt'
score = open(score_file, 'w').write('0')
Score.add_score(5)


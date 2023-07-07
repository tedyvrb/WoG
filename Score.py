import os

def add_score(difficulty):
    # score_file_path = r'C:\Users\user\OneDrive - Qmasters\DevOps\Python\Python Project\WOG'
    score_file = 'Scores.txt'

    # If file not exist or removed created file Scores
    if not os.path.exists(score_file):
        with open(score_file,'w') as file:
            file.write('0')

    # Check Scores_file content
    score = open(score_file, 'r').read()
    print(f'Score check is: {score}')
    if score.isdigit():
        score = int(score)
    else:
        score = 0

    points_of_wings = (difficulty * 3) + 5
    new_score = score + points_of_wings
    open(score_file, 'w').write(str(new_score))

    # check score file after adding new_value
    new_value = open(score_file, 'r').read()
    print(f'New value in score file is: {new_value}')
    # ------------------------------------------------

    open(score_file).close()







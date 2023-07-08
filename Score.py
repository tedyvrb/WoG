import os
import Utils

def add_score(difficulty):
    # score_file_path = r'C:\Users\user\OneDrive - Qmasters\DevOps\Python\Python Project\WOG'
    score_file = Utils.SCORES_FILE_NAME

    # If file not exist or removed created new file Scores
    if (not os.path.exists(score_file)) or difficulty == 0:
        with open(score_file, 'w') as file:
            file.write('Start the Game CHECK')
            file.close()

    # Check Scores_file content
    score = open(score_file, 'r').read()
    print(f'Score check from the file is: {score}, difficulty is: {difficulty}')
    if score.isdigit() and score != 0:
        score = int(score)
        points_of_winnigs = (difficulty * 3) + 5
        new_score = score + points_of_winnigs
    else:
        new_score = 0


    # check new_score
    print(f'New score check is: {new_score}')
    open(score_file, 'w').write(str(new_score))

    # check score file after adding new_value
    # new_value = open(score_file, 'r').read()
    # print(f'New value in score file is: {new_value}')
    # ------------------------------------------------

    open(score_file).close()







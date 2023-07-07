def add_score(difficulty):
    # score_file_path = r'C:\Users\user\OneDrive - Qmasters\DevOps\Python\Python Project\WOG'
    score_file = 'Scores.txt'
    score = open(score_file, 'r').read()
    print(f'score check - {score}')
    if score.isdigit():
        score = int(score)
    else:
        score = 0



    points_of_wings = (difficulty * 3) + 5
    new_score = score + points_of_wings
    open(score_file, 'w').write(str(new_score))

    # check score file new value
    new_value = open(score_file, 'r').read()
    print(f'new value in score file is - {new_value}')
    # ------------------------------------------------

    open(score_file).close()







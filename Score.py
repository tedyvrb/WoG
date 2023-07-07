def add_score(difficulty):
    # score_file_path = r'C:\Users\user\OneDrive - Qmasters\DevOps\Python\Python Project\WOG'
    score_file = 'Scores.txt'
    score = open(score_file, 'r').read()

    print(f'score check - {score}')


    points_of_wings = (difficulty * 3) + 5
    new_score = int(score) + points_of_wings
    open(score_file, 'w').write(new_score)

    open(score_file).close()







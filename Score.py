def add_score(difficulty):
    score_file_path = r'C:\Users\user\OneDrive - Qmasters\DevOps\Python\Python Project\WOG'
    score_file = open(score_file_path, 'r')
    score = score_file.read()
    print(f'score check - {score}')


    points_of_wings = (difficulty * 3) + 5
    new_score = int(score) + points_of_wings
    score_file = open(score_file_path, 'w')
    score_file.write(new_score)

    score_file.close()







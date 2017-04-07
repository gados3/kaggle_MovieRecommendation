import csv
from os import path
from core.data_load import Data_Holder
from learning_algorithms.naive_bayes import Naive_Bayes


def parse_file(file_path):
    d = {}
    with open(file_path, 'r', encoding="latin-1") as file:
        next(file)
        for item_string in file.readlines():
            elements = item_string.replace("\n", "").split(',')
            d[elements[2]] = elements[1]
    return d


def test_solution(answers_file_path, solution_file_path):
    solution = parse_file(solution_file_path)
    answers = parse_file(answers_file_path)
    item_count = 0
    right_answer_count = 0
    for rating_id, rating in solution.items():
        item_count += 1
        if abs(int(rating) - int(answers[rating_id])) < 2:
            right_answer_count += 1
    return (right_answer_count / item_count) * 100


if __name__ == "__main__":

    # PATHS
    RELATIVE_PATH = path.dirname(__file__)
    USERS_PATH = path.join(RELATIVE_PATH, 'resources/users.dat')
    MOVIES_PATH = path.join(RELATIVE_PATH, 'resources/movies.dat')
    # SAMPLE_PATH = path.join(RELATIVE_PATH, 'resources/sample_submission.csv')
    # SAMPLE_PATH = path.join(RELATIVE_PATH, 'testing/sample_sub1.csv')
    SAMPLE_PATH = path.join(RELATIVE_PATH, 'testing/sample_sub2.csv')
    RESULT_PATH = path.join(RELATIVE_PATH, 'testing/result.csv')
    # TRAINING_PATH = path.join(
    # RELATIVE_PATH, 'resources/training_ratings_for_kaggle_comp.csv')
    TRAINING_PATH = path.join(
        RELATIVE_PATH, 'testing/training_data1.csv')
    # TRAINING_PATH = path.join(
    #     RELATIVE_PATH, 'testing/training_data2.csv')

    # FETCHING DATA FROM FILES
    data = Data_Holder(USERS_PATH, MOVIES_PATH, TRAINING_PATH, SAMPLE_PATH)

    # INITIATING BAYES CLASSIFIER
    nbc = Naive_Bayes(data.get_training_data(), "rating")

    with open(RESULT_PATH, 'w') as result_file:
        wr = csv.writer(result_file, delimiter=',', quoting=csv.QUOTE_NONE)
        wr.writerow(["user", "rating", "id"])
        for user_id, movie_id in data.movies_to_rate:
            result = nbc.classify(data.itemize_association(user_id, movie_id))
            wr.writerow([user_id, result.value, str(
                user_id) + "_" + str(movie_id)])

    print(test_solution(SAMPLE_PATH, RESULT_PATH))

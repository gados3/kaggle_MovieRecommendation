import csv
from os import path
from core.data_load import Data_Holder
from learning_algorithms.naive_bayes import Naive_Bayes

if __name__ == "__main__":

    # PATHS
    RELATIVE_PATH = path.dirname(__file__)
    USERS_PATH = path.join(RELATIVE_PATH, 'resources/users.dat')
    MOVIES_PATH = path.join(RELATIVE_PATH, 'resources/movies.dat')
    SAMPLE_PATH = path.join(RELATIVE_PATH, 'resources/sample_submission.csv')
    RESULT_PATH = path.join(RELATIVE_PATH, 'result.csv')
    TRAINING_PATH = path.join(
        RELATIVE_PATH, 'resources/training_ratings_for_kaggle_comp.csv')

    # FETCHING DATA FROM FILES
    data = Data_Holder(USERS_PATH, MOVIES_PATH, TRAINING_PATH, SAMPLE_PATH)

    # INITIATING BAYES CLASSIFIER
    nbc = Naive_Bayes(data.get_training_data(), "rating")

    with open(RESULT_PATH, 'w') as result_file:
        wr = csv.writer(result_file, delimiter=',', quoting=csv.QUOTE_NONE)
        wr.writerow(["user", "rating", "id"])
        for user_id, movie_id in data.movies_to_rate:
            rating = nbc.classify(data.itemize_association(user_id, movie_id))
            wr.writerow([user_id, rating.value, str(
                user_id) + "_" + str(movie_id)])

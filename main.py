from os import path
from core.data_load import load_movies_data, load_ratings_data, load_users_data

if __name__ == "__main__":

    # DATA LOAD
    script_path = path.dirname(__file__)
    users = load_users_data(path.join(script_path, '../resources/users.dat'))
    movies = load_movies_data(
        path.join(script_path, '../resources/movies.dat'))
    ratings = load_ratings_data(
        path.join(script_path, '../resources/training_ratings_for_kaggle_comp.csv'))

from functools import partial
from operator import is_not
from os import path

from data_type import Occupation, Sex, Age, Zipcode
from user import User
from movie import Movie
from rating import Rating


def load_users_data(filename: str):
    with open(filename, 'r', encoding="latin-1") as file:
        users_string = file.readlines()
    return parse_users(users_string)


def load_movies_data(filename: str):
    with open(filename, 'r', encoding="latin-1") as file:
        movies = file.readlines()
    return list(map(parse_movie, movies))


def load_ratings_data(filename: str):
    with open(filename, 'r', encoding="latin-1") as file:
        next(file)
        ratings = file.readlines()
    return list(map(parse_rating, ratings))


def parse_user(user_string: str):
    user_string = user_string.replace("\n", "")
    user_elements = user_string.split('::')

    try:
        return User(user_id=int(user_elements[0]),
                    sex=Sex(user_elements[1]),
                    age=Age(int(user_elements[2])),
                    occupation=Occupation(int(user_elements[3])),
                    zipcode=Zipcode(user_elements[4]))
    except ValueError:
        return None


def parse_users(users_string):
    return list(filter(partial(is_not, None), map(parse_user, users_string)))


def parse_movie(movie_string: str):
    movie_elements = movie_string.replace("\n", "").split('::')
    return Movie(
        movie_id=int(movie_elements[0]),
        title=movie_elements[1],
        genres=movie_elements[2]
    )


def parse_rating(rating_string: str):
    rating_elements = rating_string.replace("\n", "").split(',')
    return Rating(
        user_id=int(rating_elements[0]),
        movie_id=int(rating_elements[1]),
        rating=int(rating_elements[2]),
        rating_id=rating_elements[3]
    )


if __name__ == "__main__":
    script_path = path.dirname(__file__)

    users = load_users_data(path.join(script_path, '../resources/users.dat'))
    movies = load_movies_data(
        path.join(script_path, '../resources/movies.dat'))
    ratings = load_ratings_data(
        path.join(script_path, '../resources/training_ratings_for_kaggle_comp.csv'))

    # for user in users:
    #     print(user)
    # for movie in movies:
    #     print(movie)
    for rating in ratings:
        print(rating)

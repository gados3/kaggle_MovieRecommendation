from core.data_types import Occupation, Gender, Age, Zipcode
from core.user import User
from core.movie import Movie
from core.rating import Rating


class Data_Holder:

    def __init__(self,
                 path_to_users_file,
                 path_to_movies_file,
                 path_to_training_file,
                 path_to_sample_submission):
        self.users = self.__load_users_data(path_to_users_file)
        self.movies = self.__load_movies_data(path_to_movies_file)
        self.ratings = self.__load_training_data(path_to_training_file)
        self.movies_to_rate = self.__load_sample_data(
            path_to_sample_submission)

    def __load_users_data(self, filename: str):
        with open(filename, 'r', encoding="latin-1") as file:
            users_string = file.readlines()
        users_dict = {}
        for user_string in users_string:
            user = self.__parse_user(user_string)
            users_dict[user.id] = user
        return users_dict

    def __load_movies_data(self, filename: str):
        with open(filename, 'r', encoding="latin-1") as file:
            movies_string = file.readlines()
        movies_dict = {}
        for movie_string in movies_string:
            movie = self.__parse_movie(movie_string)
            movies_dict[movie.id] = movie
        return movies_dict

    def __load_training_data(self, filename: str):
        with open(filename, 'r', encoding="latin-1") as file:
            next(file)
            ratings = file.readlines()
        return list(map(self.__parse_rating, ratings))

    def __load_sample_data(self, filename: str):
        with open(filename, 'r', encoding="latin-1") as file:
            next(file)
            items_string = file.readlines()
        return list(map(self.__parse_sample, items_string))

    def __parse_sample(self, item_string: str):
        sample_elements = item_string.replace("\n", "").split(',')
        return tuple(map(int, sample_elements[2].split('_')))

    def __parse_user(self, user_string: str):
        user_elements = user_string.replace("\n", "").split('::')
        return User(
            user_id=int(user_elements[0]),
            gender=Gender(user_elements[1]),
            age=Age(int(user_elements[2])),
            occupation=Occupation(int(user_elements[3])),
            zipcode=Zipcode(user_elements[4])
        )

    def __parse_movie(self, movie_string: str):
        movie_elements = movie_string.replace("\n", "").split('::')
        return Movie(
            movie_id=int(movie_elements[0]),
            title=movie_elements[1],
            genres=movie_elements[2]
        )

    def __parse_rating(self, rating_string: str):
        rating_elements = rating_string.replace("\n", "").split(',')
        return Rating(
            user_id=int(rating_elements[0]),
            movie_id=int(rating_elements[1]),
            rating=int(rating_elements[2]),
            rating_id=rating_elements[3]
        )

    def get_training_data(self):
        training_data = []
        for rating in self.ratings:
            item = []
            item.extend(rating.itemize())
            item.extend(self.users[rating.user_id].itemize())
            item.extend(self.movies[rating.movie_id].itemize())
            training_data.append(item)
        return training_data

    def itemize_association(self, user_id, movie_id):
        item = []
        item.extend(self.users[user_id].itemize())
        item.extend(self.movies[movie_id].itemize())
        return item
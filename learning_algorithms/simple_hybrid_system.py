from collections import defaultdict
from core.data_types import Star_Rating


class SimpleHybridSystem:

    def __init__(self, users, movies: dict, ratings):
        self.movie_rating_dict = self.__build_movie_rating_dict(ratings)
        self.user_rating_dict = self.__build_user_rating_dict(ratings)
        self.user_similarity = self.__build_user_similarity_dict(users)
        self.movie_similarity = self.__build_movie_similarity_dict(movies)

    def classify(self, user_id, movie_id):
        rating_based_on_users = self.__classify_using_users(user_id, movie_id)
        rating_based_on_movies = self.__classify_using_movies(
            user_id, movie_id)
        if rating_based_on_users is None and rating_based_on_movies is None:
            return Star_Rating(3)
        elif rating_based_on_movies is None:
            return Star_Rating(int(rating_based_on_users))
        elif rating_based_on_users is None:
            return Star_Rating(int(rating_based_on_movies))
        else:
            return Star_Rating(int((rating_based_on_movies +
                                    rating_based_on_users) / 2.))

    def __build_user_rating_dict(self, ratings):
        user_rating_dict = defaultdict(list)
        for rating in ratings:
            user_rating_dict[rating.user_id].append(rating)
        return user_rating_dict

    def __build_movie_rating_dict(self, ratings):
        movie_rating_dict = defaultdict(list)
        for rating in ratings:
            movie_rating_dict[rating.movie_id].append(rating)
        return movie_rating_dict

    def __build_user_similarity_dict(self, users):
        similarity_dict = {}
        users_list = list(users.items())
        for user1_id, user1 in users.items():
            for user2_id, user2 in users_list:
                if user1_id == user2_id:
                    similarity_dict[(user1_id, user2_id)] = 1
                else:
                    similarity = user1.compare(user2)
                    similarity_dict[(user1_id, user2_id)] = similarity
                    similarity_dict[(user2_id, user1_id)] = similarity
            users_list.remove((user1_id, user1))
        return similarity_dict

    def __build_movie_similarity_dict(self, movies):
        similarity_dict = {}
        movies_list = list(movies.items())
        for movie1_id, movie1 in movies.items():
            for movie2_id, movie2 in movies_list:
                if movie1_id == movie2_id:
                    similarity_dict[(movie1_id, movie2_id)] = 1
                else:
                    similarity = movie1.compare(movie2)
                    similarity_dict[(movie1_id, movie2_id)] = similarity
                    similarity_dict[(movie2_id, movie1_id)] = similarity
            movies_list.remove((movie1_id, movie1))
        return similarity_dict

    def __classify_using_movies(self, user_id, movie_id):
        numerator = 0
        denominator = 0
        for rating in self.user_rating_dict[user_id]:
            try:
                similarity = self.movie_similarity[(movie_id, rating.movie_id)]
                numerator += rating.rating.value * similarity
                denominator += similarity
            except KeyError:
                return None
        if denominator == 0:
            return None
        else:
            return float(numerator) / denominator

    def __classify_using_users(self, user_id, movie_id):
        numerator = 0
        denominator = 0
        for rating in self.movie_rating_dict[movie_id]:
            try:
                similarity = self.user_similarity[(user_id, rating.user_id)]
                numerator += rating.rating.value * similarity
                denominator += similarity
            except KeyError:
                return None
        if denominator == 0:
            return None
        else:
            return float(numerator) / denominator

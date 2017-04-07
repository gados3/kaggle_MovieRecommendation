from core.data_types import Star_Rating


class Rating:

    def __init__(self, user_id: int, movie_id: int, rating: int, rating_id: str):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = Star_Rating(rating)
        self.id = rating_id

    def __str__(self):
        return "user_id: {}, " \
            "movie_id: {}, " \
            "rating: {}, " \
            "rating id: {}".format(self.user_id,
                                   self.movie_id,
                                   self.rating,
                                   self.id)

    def itemize(self):
        return [("rating", self.rating)]

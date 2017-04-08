import re
from core.utils import global_similarity, euclidian_distance, list_similarity, min_max_normalization
from core.data_types import Genre


class Movie:

    def __init__(self, movie_id: int, title: str, genres: str):
        self.id = movie_id
        self.title = re.sub(r"\(\d{4}\)", '', title)
        self.genres = self.__parse_genres(genres)
        self.year = re.search(r"\(\d{4}\)", title).group(
            0).strip('(').strip(')')

    def __parse_genres(self, genres_string: str):
        return list(map(lambda genre: Genre(genre), genres_string.split('|')))

    def __str__(self):
        return "id: {}, " \
            "title: {}, " \
            "genres: {}".format(self.id,
                                self.title,
                                ' / '.join(map(lambda genre: str(genre), self.genres)))

    def itemize(self):
        movie_attributes = [("movie_title", self.title),
                            ("movie_year", self.year)]
        attr_genres = [("movie_genre", g) for g in self.genres]
        movie_attributes.extend(attr_genres)
        return movie_attributes

    def compare(self, other_movie: Movie):
        return global_similarity([
            euclidian_distance(min_max_normalization(1920, 2017, self.year), min_max_normalization(1920, 2017, other_movie.year)),
            1 - list_similarity(self.genres, other_movie.genres)
        ])

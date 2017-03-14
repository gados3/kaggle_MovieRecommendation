from data_type import Genre


class Movie:

    def __init__(self, movie_id: int, title: str, genres: str):
        self.id = movie_id
        self.title = title
        self.genres = self.parse_genres(genres)

    def parse_genres(self, genres_string: str):
        return list(map(lambda genre: Genre(genre), genres_string.split('|')))

    def __str__(self):
        return "id: {}, " \
            "title: {}, " \
            "genres: {}".format(self.id,
                                self.title,
                                ' / '.join(map(lambda genre: str(genre), self.genres)))

from core.data_types import Occupation, Gender, Age, Zipcode
from core.utils import global_similarity, nominal_disimilarity, min_max_normalization, euclidian_distance


class User:

    def __init__(self, user_id: int, gender: Gender, age: Age, occupation: Occupation,
                 zipcode: Zipcode):
        self.id = user_id
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.zipcode = zipcode

    def __str__(self):
        return 'id: {}, ' \
               'sex: {}, ' \
               'age: {}, ' \
               'occupation: {}, ' \
               'zipcode: {}'.format(self.id,
                                    self.gender,
                                    self.age,
                                    self.occupation,
                                    self.zipcode)

    def itemize(self):
        return [("gender", self.gender),
                ("age", self.age),
                ("occupation", self.occupation)]

    def compare(self, other_user):
        return global_similarity([
            nominal_disimilarity(self.gender, other_user.gender),
            euclidian_distance(min_max_normalization(
                1, 56, self.age.value), min_max_normalization(1, 56, other_user.age.value)),
            nominal_disimilarity(self.occupation, other_user.occupation)
        ])
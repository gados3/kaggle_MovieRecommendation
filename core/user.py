from core.data_types import Occupation, Gender, Age, Zipcode


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
                ("occupation", self.occupation),
                ("zipcode", self.zipcode)]

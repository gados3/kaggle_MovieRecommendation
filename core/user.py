from data_type import Occupation, Sex


class User:

    def __init__(self, user_id: int, sex: Sex, age, occupation: Occupation,
                 zipcode):
        self.id = user_id
        self.sex = sex
        self.age = age
        self.occupation = occupation
        self.zipcode = zipcode

    def __str__(self):
        return 'id: {}, ' \
               'sex: {}, ' \
               'age: {}, ' \
               'occupation: {}, ' \
               'zipcode: {}'.format(self.id,
                                    self.sex,
                                    self.age,
                                    self.occupation,
                                    self.zipcode)

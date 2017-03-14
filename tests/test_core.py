import unittest

from core import parse_user
from data_type import Occupation, Sex, Age


class TestCore(unittest.TestCase):
    ID = 8
    SEX = Sex.FEMALE
    AGE = Age.LATE_FORTY
    OCCUPATION = Occupation.CLERICAL_ADMIN
    ZIPCODE = '12392'

    INVALID_ID = 'we2'
    INVALID_SEX = 'W'
    INVALID_AGE = '21'
    INVALID_OCCUPATION = '21'

    def test_parse_user(self):
        user_string = '{}::{}::{}::{}::{}\n'.format(
            self.ID,
            self.SEX,
            self.AGE,
            self.OCCUPATION,
            self.ZIPCODE,
        )

        user = parse_user(user_string)

        self.assertEqual(user.id, self.ID)
        self.assertEqual(user.sex, self.SEX)
        self.assertEqual(user.age, self.AGE)
        self.assertEqual(user.occupation, self.OCCUPATION)
        self.assertEqual(user.zipcode, self.ZIPCODE)

    def test_invalid_occupation(self):
        user_string = '{}::{}::{}::{}::{}\n'.format(
            self.ID,
            self.SEX,
            self.AGE,
            self.INVALID_OCCUPATION,
            self.ZIPCODE,
        )

        with self.assertRaises(ValueError):
            parse_user(user_string)

    def test_invalid_user_id(self):
        user_string = '{}::{}::{}::{}::{}\n'.format(
            self.INVALID_ID,
            self.SEX,
            self.AGE,
            self.OCCUPATION,
            self.ZIPCODE,
        )

        with self.assertRaises(ValueError):
            parse_user(user_string)

    def test_invalid_sex(self):
        user_string = '{}::{}::{}::{}::{}\n'.format(
            self.ID,
            self.INVALID_SEX,
            self.AGE,
            self.OCCUPATION,
            self.ZIPCODE,
        )

        with self.assertRaises(ValueError):
            parse_user(user_string)

    def test_invalid_age(self):
        user_string = '{}::{}::{}::{}::{}\n'.format(
            self.ID,
            self.SEX,
            self.INVALID_AGE,
            self.OCCUPATION,
            self.ZIPCODE,
        )

        with self.assertRaises(ValueError):
            parse_user(user_string)

from enum import Enum


class MyEnum(Enum):

    def __str__(self):
        return self.name


class Occupation(MyEnum):
    OTHER = 0
    ACADEMIC_EDUCATOR = 1
    ARTIST = 2
    CLERICAL_ADMIN = 3
    STUDENT = 4
    CUSTOMER_SERVICE = 5
    DOCTOR_HEALTH_CARE = 6
    EXECUTIVE_MANAGERIAL = 7
    FARMER = 8
    HOMEMAKER = 9
    K_12_STUDENT = 10
    LAWYER = 11
    PROGRAMMER = 12
    RETIRED = 13
    SALES_MARKETING = 14
    SCIENTIST = 15
    SELF_EMPLOYED = 16
    TECHNICIAN_ENGINEER = 17
    TRADESMAN_CRAFTSMAN = 18
    UNEMPLOYED = 19
    WRITER = 20


class Gender(MyEnum):
    MALE = 'M'
    FEMALE = 'F'


class Age(MyEnum):
    MINOR = 1
    EARLY_TWENTY = 18
    THIRTY = 25
    FORTY = 35
    LATE_FORTY = 45
    EARLY_FIFTY = 50
    GOLDEN = 56


class Zipcode(str):
    pass


class Genre(MyEnum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"
    CHILDREN = "Children's"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FANTASY = "Fantasy"
    FILM_NOIR = "Film-Noir"
    HORROR = "Horror"
    MUSICAL = "Musical"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    SCI_FI = "Sci-Fi"
    THRILLER = "Thriller"
    WAR = "War"
    WESTERN = "Western"


class Star_Rating(MyEnum):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

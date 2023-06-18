import datetime


class Person:
    def __init__(
            self,
            first_name,
            middle_name,
            last_name,
            birthdate,
            birthmonth,
            birthyear,
            hobbies
    ):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.birthmonth = birthmonth
        self.birthyear = birthyear
        self.hobbies = hobbies
        self.age = int(datetime.date.today().year) - birthyear

    def update_age(self):
        if int(datetime.date.today().month) > self.birthmonth:
            pass

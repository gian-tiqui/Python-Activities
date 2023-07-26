class Student:
    def __init__(self, student_id, last_name, first_name, middle_name):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name


class Building:
    def __init__(self, building_num, name):
        self.building_num = building_num
        self.name = name
        self.floor_amount = 4

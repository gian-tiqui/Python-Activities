class Subject:
    def __init__(self, s_name, s_desc):
        self.s_name = s_name
        self.s_desc = s_desc
        self.grade = 0

    def set_grade(self, final_grade):
        self.grade = final_grade


class Student:
    def __init__(self,
                 f_name,
                 l_name,
                 m_name,
                 birthyear,
                 birthdate,
                 birthmonth,
                 sex):
        self.f_name = f_name
        self.l_name = l_name
        self.m_name = m_name
        self.birthyear = birthyear
        self.birthdate = birthdate
        self.birthmonth = birthmonth
        self.sex = sex
        self.status = "regular"
        self.subject = []

    def change_status(self):
        self.status = input("Enter status: ")

    def add_subject(self, subject, max_subject=9):
        if len(self.subject) == max_subject or subject in self.subject:
            return False

        self.subject.append(subject)

        return True

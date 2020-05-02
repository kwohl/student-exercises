from student import Student
from cohort import Cohort
from exercise import Exercise

class Instructor:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.slack_handle = ""
        self.cohort = 0
        self.specialty = ""
        
    def assign(self, exercise, cohort):
        for student in cohort.students:
            student.exercises.append(exercise)
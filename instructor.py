from student import Student
from cohort import Cohort
from exercise import Exercise
from nss_person import NSSPerson

class Instructor(NSSPerson):

    def __init__(self):
        super().__init__()
        self.specialty = ""
        
    def assign(self, exercise, cohort):
        for student in cohort.students:
            student.exercises.append(exercise)
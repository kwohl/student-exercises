from student import Student
from cohort import Cohort
from exercise import Exercise
from nss_person import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.specialty = ""
        
    def assign(self, exercise, cohort):
        for student in cohort.students:
            student.exercises.append(exercise)

    def assign_cohort(self, cohort):
        self.cohort = cohort
        cohort.instructors.append(self)
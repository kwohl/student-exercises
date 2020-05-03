from nss_person import NSSPerson
from cohort import Cohort

class Student(NSSPerson):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.exercises = []

    def assign_cohort(self, cohort):
        self.cohort = cohort
        cohort.students.append(self)

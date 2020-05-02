from nss_person import NSSPerson

class Student(NSSPerson):

    def __init__(self):
        super().__init__()
        self.exercises = []

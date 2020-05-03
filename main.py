from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

fizz_buzz = Exercise("Fizz Buzz", "javaScript")
daily_journal = Exercise("Daily Journal", "javascript")
flexbox = Exercise("flexbox", "CSS")
sensitive_information = Exercise("sensitive_information", "python")

day38 = Cohort("Day Cohort 38")
day39 = Cohort("Day Cohort 39")
day40 = Cohort("Day Cohort 40")
evening11 = Cohort("Evening Cohort 11")

ivan = Student("Ivan", "Smith")
katie = Student("Katie", "Wohl")
cooper = Student("Cooper", "Nichols")
roxanne = Student("Roxanne", "Nasraty")

andy = Instructor("Andy", "Collins")
kristen = Instructor("Kristen", "Norris")
bryan = Instructor("Bryan", "Nilsen")
jisie = Instructor("Jisie", "David")

ivan.assign_cohort(evening11)
katie.assign_cohort(day38)
cooper.assign_cohort(day38)
roxanne.assign_cohort(day40)

andy.assign_cohort(day38)
kristen.assign_cohort(day38)
bryan.assign_cohort(day38)
jisie.assign_cohort(day38)

for instructor in day38.instructors:
    print(instructor.first_name)

andy.assign(fizz_buzz, day38)
jisie.assign(sensitive_information, day38)

for exercise in katie.exercises:
    print(exercise.name)
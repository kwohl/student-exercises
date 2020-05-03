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
bryan.assign_cohort(day40)
jisie.assign_cohort(day38)


# for instructor in day38.instructors:
#     print(instructor.first_name)

andy.assign(fizz_buzz, day38)
jisie.assign(sensitive_information, day38)
bryan.assign(flexbox, day40)
andy.assign(flexbox, evening11)
andy.assign(fizz_buzz, evening11)
andy.assign(sensitive_information, evening11)
andy.assign(daily_journal, evening11)

# for exercise in katie.exercises:
#     print(exercise.name)


students = list()
exercises = list()

students.append(ivan)
students.append(katie)
students.append(cooper)
students.append(roxanne)
# for student in students:
#     print(student.first_name)
exercises.append(fizz_buzz)
exercises.append(flexbox)
exercises.append(daily_journal)
exercises.append(sensitive_information)

for student in students:
    current_exercises = []
    for exercise in exercises:
        for student_exercise in student.exercises:
            if exercise.name == student_exercise.name:
                current_exercises.append(exercise.name)
    if len(current_exercises) == 2:
        print(f"{student.first_name} is working on {' and '.join(current_exercises)}.")
    if len(current_exercises) == 1:
        print(f"{student.first_name} is working on {' '.join(current_exercises)}.")
    if len(current_exercises) > 2:
        print(f"{student.first_name} is working on {', '.join(current_exercises[:-1])}, and {current_exercises[-1]}.")

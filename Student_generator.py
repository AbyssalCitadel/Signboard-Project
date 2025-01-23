from random import randrange
from datetime import timedelta
import numpy as np
# Imports the random number gen
# do all calculations in seconds from midnight,
# output as hh:mm:ss in military time

# arrival_time = when the student arrives on campus, expose_time = how long the student sees the sign, times_per_week = how often the student arrives on campus
class Student:
    def __init__ (self, arrival_time, expose_time, times_per_week):
        self.arrival_time = arrival_time
        self.expose_time = expose_time
        self.times_per_week = times_per_week
    def hms(self):
        return str(timedelta(seconds=self.arrival_time))

class QueueOfStudents:
    def __init__(self):
        self.students = []
        self.next_student_index = 0
    def add_student(self, student):
        self.students.append(student)
    def take_student(self):
        return self.students.pop(0)

queue_of_students = QueueOfStudents()

# Generates the students.  
for x in range(300):
    example_student = Student(randrange(8 * 3600, 18 * 3600), round(np.random.normal(60,5)), randrange(1, 6))
    queue_of_students.add_student(example_student)

# print the student information
for x in queue_of_students.students:
    print (x.hms())
    print (x.expose_time)
    print (x.times_per_week)
    print ("______________")

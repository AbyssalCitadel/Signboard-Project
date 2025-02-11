from random import randrange
from datetime import timedelta
import numpy as np
# Imports the random number gen
# output as hh:mm:ss in military time

# arrival_time = when the student arrives on campus, expose_time = how long the student sees the sign, times_per_week = how often the student arrives on campus
class Student:
    def __init__ (self, arrival_time, expose_time, times_per_week):
        self.arrival_time = arrival_time
        self.expose_time = expose_time
        self.times_per_week = times_per_week
    def hms(self):
        return str(timedelta(seconds=self.arrival_time))

# Class for student generation
class QueueOfStudents:
    def __init__(self):
        self.students = []
        self.next_student_index = 0
    def add_student(self, student):
        self.students.append(student)
    def take_student(self):
        return self.students.pop(0)

queue_of_students = QueueOfStudents()
def generate_students(student_amount):
# Generates the students.  
#Putting the student generator in it's own function in order to let the user change the student amount
    for x in range(student_amount):
        # Since real life students arive in waves, this let's the program choose if a certain student arrives in a wave or at a random time
        arrival_times = [28800, 34560, 36720, 39240, 42120, 45000, 50040, 57600, 62640, randrange(21600, 79200)]
                 
        example_student = Student(round(np.random.normal(choice(arrival_times),200)), round(np.random.normal(60,5)), randrange(1, 6))
        queue_of_students.add_student(example_student)

# I also have to put the student sorting into here or else the student amount wouldn't work
    sorted_list = []

    for x in queue_of_students.students: 

    # upper found checks if the algorithm found a another entry with a arrival_time higher than the selected entry's
        upper_found = False

        selected_position = 0
        while upper_found == False:
            # If the selected position reaches the end of the list, just put the current student at the end of the list (Prevents crash)
            if selected_position == len(sorted_list):
                sorted_list.insert(selected_position, x)
            else:
                if x.arrival_time > sorted_list[selected_position].arrival_time:
                    selected_position = selected_position + 1
                else:
                    sorted_list.insert(selected_position, x)
                    upper_found = True

    queue_of_students.students = sorted_list
    return queue_of_students



from random import randrange
# Imports the random number gen

# arrival_time = when the student arrives on campus, expose_time = how long the student sees the sign, times_per_week = how often the student arrives on campus
class student:
    def __init__ (self, arrival_time, expose_time, times_per_week):
        self.arrival_time = arrival_time
        self.expose_time = expose_time
        self.times_per_week = times_per_week


list_of_students = []

# Generates the students. 
# NOTE: Arrival time is in military time. 
for x in range(300):
    example_student = student( (randrange(8, 18) * 100) + randrange(00, 60), (randrange(1, 3) * 100) + randrange(00, 59), randrange(1, 6))
    list_of_students.append(example_student)

# print the student information
for x in list_of_students:
    print (x.arrival_time)
    print (x.expose_time)
    print (x.times_per_week)
    print ("______________")
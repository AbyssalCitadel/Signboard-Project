from random import randrange
import numpy as np
import matplotlib.pyplot as plt
# Imports the random number gen
# do all calculations in seconds from midnight,
# output as hh:mm:ss in military time

# arrival_time = when the student arrives on campus, expose_time = how long the student sees the sign, times_per_week = how often the student arrives on campus\

number_of_students = 120
number_of_slides = 21
seconds_per_slide = 20
number_of_weeks = 16
days_per_week = 4
# 8AM
slide_zero_time = 8 * 3600

seconds_per_loop = number_of_slides * seconds_per_slide
number_of_days = number_of_weeks * days_per_week
# this does not work
# students_seen_slides_counters = [[0] * number_of_slides] * number_of_students
# this works
students_seen_slides_counters = [(lambda: [0] * number_of_slides)() for _ in range(number_of_students)]

average_slides_per_student_progress = []
for d in range(number_of_days):
    for s in range(number_of_students):
        # seconds since midnight (8AM-6PM)
        arrival_time = randrange(8 * 3600, 18 * 3600)
        seconds_viewing = round(np.random.normal(60,5))
        arrival_seconds_into_loop = (arrival_time - slide_zero_time) % seconds_per_loop
        arrival_slide_number = int(arrival_seconds_into_loop // seconds_per_slide)
        departure_time = arrival_time + seconds_viewing
        departure_seconds_into_loop = (departure_time - slide_zero_time) % seconds_per_loop
        departure_slide_number = int(departure_seconds_into_loop // seconds_per_slide)
        if departure_slide_number >= arrival_slide_number:
            for n in range(arrival_slide_number, departure_slide_number + 1):
                students_seen_slides_counters[s][n] += 1
        else:
            for n in range(arrival_slide_number, number_of_slides):
                students_seen_slides_counters[s][n] += 1
            for n in range(0, departure_slide_number + 1):
                students_seen_slides_counters[s][n] += 1
    slides_per_student = list(map(lambda slides_for_student: len(slides_for_student) - slides_for_student.count(0), students_seen_slides_counters))
    average_slides_per_student = sum(slides_per_student) / len(slides_per_student)
    print(d, average_slides_per_student)
    average_slides_per_student_progress.append(average_slides_per_student)

plt.bar(range(number_of_days), average_slides_per_student_progress)
plt.show()
# print(students_seen_slides_counters)
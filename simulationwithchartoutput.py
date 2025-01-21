from random import randrange
import numpy as np
import matplotlib.pyplot as plt
# Imports the random number gen
# do all calculations in seconds from midnight,
# output as hh:mm:ss in military time

# arrival_time = when the student arrives on campus, expose_time = how long the student sees the sign, times_per_week = how often the student arrives on campus\


number_of_students = 120
number_of_slides = 20
seconds_per_slide = 20
number_of_weeks = 16
days_per_week = 4
# 8AM
slide_zero_time = 8 * 3600

# seconds per full cycle of the slides, how long it takes all twenty slides to show
seconds_per_loop = number_of_slides * seconds_per_slide
# number of days the student goes to school
number_of_days = number_of_weeks * days_per_week
# this does not work
# students_seen_slides_counters = [[0] * number_of_slides] * number_of_students
# this crates a list of a list of all students and each student has a list of what slides they have seen
students_seen_slides_counters = [(lambda: [0] * number_of_slides)() for _ in range(number_of_students)]

# make an empty list for later
average_slides_per_student_progress = []
# number of days the student went total
for d in range(number_of_days):
    # the student
    for s in range(number_of_students):
        # seconds since midnight (8AM-6PM)
        arrival_time = randrange(8 * 3600, 18 * 3600)
        # standard deviation of 5 from 60 seconds so amount of time student is going up the driveway varies
        seconds_viewing = round(np.random.normal(60,5))
        # how many seconds into the current loop of 20 slides 
        arrival_seconds_into_loop = (arrival_time - slide_zero_time) % seconds_per_loop
        # find which slide was up when the student first came up the driveway
        arrival_slide_number = int(arrival_seconds_into_loop // seconds_per_slide)
        # when the student is out of the driveway
        departure_time = arrival_time + seconds_viewing
        # how far into the loop the student is when the student is out of the driveway
        departure_seconds_into_loop = (departure_time - slide_zero_time) % seconds_per_loop
        # which slide was the last on ethe student saw
        departure_slide_number = int(departure_seconds_into_loop // seconds_per_slide)
        # if the loop did not reach the final slides and reset back to zero
        if departure_slide_number >= arrival_slide_number:
            # from the first slide seen to the last slide seen
            for n in range(arrival_slide_number, departure_slide_number + 1):
                # add one to the index of each slide seen by that student
                students_seen_slides_counters[s][n] += 1
        # if the loop reached the end and the slides reset
        else:
            # add one to the index of each slide seen by that student
            for n in range(arrival_slide_number, number_of_slides):
                students_seen_slides_counters[s][n] += 1
            for n in range(0, departure_slide_number + 1):
                students_seen_slides_counters[s][n] += 1
    # creates a list of the slides the student have seen
    slides_per_student = list(map(lambda slides_for_student: len(slides_for_student) - slides_for_student.count(0), students_seen_slides_counters))
    # get the average of the slides seen per student
    average_slides_per_student = sum(slides_per_student) / len(slides_per_student)
    # prints the day and the average percentage of slides by student
    print(d, average_slides_per_student)
    # used for the bar graph
    average_slides_per_student_progress.append(average_slides_per_student)

# creates a bar graph of the data gathered
plt.bar(range(number_of_days), average_slides_per_student_progress)
plt.show()
# print(students_seen_slides_counters)
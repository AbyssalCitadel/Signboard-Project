"""Gui module"""
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os 
from full_simulator import full_simulation

#Creating the GUI window 
window = tk.Tk()

window.title('')
window.geometry('1000x753')

window.title('Signboard Project')  # Adding a title

def search():
   #create a search button
    if int(seconds_box.get()) == 0 or int(search_box.get()) == 0 or int(slides_box.get()) == 0:
        result_box.config(text=(f"Please have all your inputs above 0"))
    else:
        times_slides_were_seen = full_simulation(int(seconds_box.get()), int(search_box.get()), int(slides_box.get()))
    # math for finding the average amount slides were seen
        slide_count = 0
        for x in times_slides_were_seen:
            slide_count = slide_count + x
            slide_count = slide_count // len(times_slides_were_seen)
        # I tried to split the output text, but it hates me D:
        result_box.config(text=(f"The most times a slide was seen was {min(times_slides_were_seen)}, at slide {times_slides_were_seen.index(min(times_slides_were_seen))} \n The least times a slide was seen was {max(times_slides_were_seen)}, at slide {times_slides_were_seen.index(max(times_slides_were_seen))} \n On average, a given slide was seen {slide_count} times"))

# adding a background image
'''creating a path to the image'''
DIRECTORY_PATH = os.path.dirname(__file__)
# importing the image
FILE_PATH = os.path.join(DIRECTORY_PATH, "sign.png")

# placing the image in the GUI
sd_image = tk.PhotoImage(file=FILE_PATH)
image_label = tk.Label(window, image=sd_image)
image_label.place(relx=.5, rely=.5, anchor='center')

# make the label look better
title_font = tkFont.Font(family="Georgia", size = 16, weight = "bold")

# creating a label
label = tk.Label(text="Exposure To Signboard", font = title_font)

# placing the label
label.place(relx=.5, rely=.3, anchor='center')

# change the font for the smaller labels
labels_font = tkFont.Font(family="Poor Richard", size = 12, weight=tkFont.NORMAL)

# search option
search_label = tk.Label(window, text="Number of Students", font = labels_font)

# placing the label
search_label.place(relx=.25, rely=.35, anchor='w')

# text box
search_box = tk.Entry(window, width = 20)
# placing the text box
search_box.place(relx=.45, rely=.35, anchor='center')
search_box.insert(-1, "0")

# number of slides label
slides_label = tk.Label(window, text="Number of Slides", font = labels_font)
slides_label.place(relx=.25, rely=.40, anchor='w')

# text box
slides_box = tk.Entry(window, width = 20)
# placing the text box
slides_box.place(relx=.45, rely=.40, anchor='center')
slides_box.insert(-1, "0")
# seconds persilde
seconds_label = tk.Label(window, text="Seconds Perslide", font = labels_font)
seconds_label.place(relx=.25, rely=.45, anchor='w')
# text box
seconds_box = tk.Entry(window, width = 20)
seconds_box.insert(-1, "0")
# placing the text box
seconds_box.place(relx=.45, rely=.45, anchor='center')

# Creating a styled frame for the signboard effect
signboard_frame = tk.Frame(window, bg="#F0EDE5", bd=5, relief="ridge")  
signboard_frame.grid(column=0, row=0, columnspan=3, padx=10, pady=10, sticky="ew")

#Result box in GUI
result_box = tk.Label(window, text="")

# search button
search_button= tk.Button(window, text='Submit', command = search, font = labels_font,)
# placing the button
search_button.place(relx=.5, rely=.5, anchor='center')

result_box.place(relx = 0.5,  rely = 0.57, anchor = 'center')


#Styling the existing labels
label_style = {"font": ("Arial", 11), "bg": "#d9d9d9", "padx": 5, "pady": 2}

#Adding a border and styling for the result box
result_box.config(font=("Arial", 11), fg="black", bg="white", width=50, height=3, bd=2, relief="sunken")

#Styling the search button
search_button.config(bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), bd=3, relief="raised")

#Display the GUI window
window.mainloop()

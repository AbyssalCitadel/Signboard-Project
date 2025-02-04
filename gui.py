"""Gui module"""

import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os


#Creating the GUI window 
window = tk.Tk()

window.title('')
window.geometry('1000x753')

window.title('Signboard Project')  # Adding a title
window.geometry('600x600')
window.configure(bg="#9E4244")  #MakeitPINK-This is the color of watermelon


def search():
   #create a search button
    search_entry = search_box.get()
    slides_entry = slides_box.get()
    seconds_entry = seconds_box.get()

    if search_box:
        display_text = ""
        display_text += f'{search_entry},\n'
        display_text += f'{slides_entry},\n'
        display_text += f'{seconds_entry}.'
        result_box.config(text=(display_text))


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

# number of slides label
slides_label = tk.Label(window, text="Number of Slides", font = labels_font)
slides_label.place(relx=.25, rely=.40, anchor='w')

# text box
slides_box = tk.Entry(window, width = 20)
# placing the text box
slides_box.place(relx=.45, rely=.40, anchor='center')

# seconds persilde
seconds_label = tk.Label(window, text="Seconds Perslide", font = labels_font)
seconds_label.place(relx=.25, rely=.45, anchor='w')

# text box
seconds_box = tk.Entry(window, width = 20)
# placing the text box
seconds_box.place(relx=.45, rely=.45, anchor='center')

# Creating a styled frame for the signboard effect
signboard_frame = tk.Frame(window, bg="#F0EDE5", bd=5, relief="ridge")  
signboard_frame.grid(column=0, row=0, columnspan=3, padx=10, pady=10, sticky="ew")

#label inside the signboard frame
signboard_label = tk.Label(signboard_frame, text="<3", 
                           font=("Arial", 14, "bold"), bg="#8b7d6b", fg="white")
signboard_label.pack(pady=5)

#label itself
label = tk.Label(text="EXPOSE THE PEOPLE TO THE GLOWING SIGN")
# Placing the label
label.grid(column=0, row=0)

#Search
search_label = tk.Label(window, text="Search")
search_label.grid(column=0, row=3)

#Text
search_box = tk.Entry(window, width=20)
search_box.grid(column=1, row=3)

#Number of slide lable
slides_label = tk.Label(window, text="Number of slides")
slides_label.grid(column=0, row=4)

#Text box
slides_box = tk.Entry(window, width=20)
slides_box.grid(column=1, row=4)

#Seconds per slide
seconds_label = tk.Label(window, text="Seconds Per Slide")
seconds_label.grid(column=0, row=5)

#Text box
seconds_box = tk.Entry(window, width=20)
seconds_box.grid(column=1, row=5)


#Result box in GUI
result_box = tk.Label(window, text="")

# placing result area
result_box.place(relx=.55, rely=.4, anchor='center')

# search button
search_button= tk.Button(window, text='Submit', command = submit, font = labels_font,)
# placing the button
search_button.place(relx=.5, rely=.5, anchor='center')

result_box.grid(column=7, row=5)

#Search button
search_button = tk.Button(window, text='Search', command=search)
search_button.grid(column=5, row=5)

#Styling the existing labels
label_style = {"font": ("Arial", 11), "bg": "#d9d9d9", "padx": 5, "pady": 2}

search_label.config(**label_style)
slides_label.config(**label_style)
seconds_label.config(**label_style)

#Adding a border and styling for the result box
result_box.config(font=("Arial", 11), fg="black", bg="white", width=30, height=2, bd=2, relief="sunken")

#Adding a border and some padding for the text entry boxes
search_box.config(bg="white", fg="black", font=("Arial", 10), bd=2, relief="solid")
slides_box.config(bg="white", fg="black", font=("Arial", 10), bd=2, relief="solid")
seconds_box.config(bg="white", fg="black", font=("Arial", 10), bd=2, relief="solid")

#Styling the search button
search_button.config(bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), bd=3, relief="raised")

#Display the GUI window
window.mainloop()

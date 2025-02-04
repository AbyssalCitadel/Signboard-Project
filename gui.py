"""Gui module"""


import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os


# creating the GUI window 
window = tk.Tk()
window.title('')
window.geometry('1000x753')

def submit():
    '''create a search button'''
    search_entry = search_box.get()
    slides_entry = slides_box.get()
    seconds_entry = seconds_box.get()

    if search_box:
        display_text = ""
        display_text += f'{search_entry},\n'
        # print(display_text)
        display_text += f'{slides_entry},\n'
        # print(display_text)
        display_text += f'{seconds_entry}.'
        print(display_text)

        # result_box.config(text=(search_entry))
        # result_box.config(text=(slides_entry))
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

# result box in gui
result_box = tk.Label(window, text="")
# placing result area
result_box.place(relx=.55, rely=.4, anchor='center')

# search button
search_button= tk.Button(window, text='Submit', command = submit, font = labels_font,)
# placing the button
search_button.place(relx=.5, rely=.5, anchor='center')

# display the GUI window
window.mainloop()
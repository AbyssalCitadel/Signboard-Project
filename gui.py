import tkinter as tk

# creating the GUI window 
window = tk.Tk()
window.title('')
window.geometry('600x300')

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


# creating a label
label = tk.Label(text="Exposure To Signboard")
# placing the label
label.grid(column = 0, row = 0)

# search option
search_label = tk.Label(window, text="Number of Students")
# placing the label
search_label.grid(column = 0, row = 3)

# text box
search_box = tk.Entry(window, width = 20)
# placing the text box
search_box.grid(column = 1, row = 3)

# number of slides label
slides_label = tk.Label(window, text="Number of Slides")
slides_label.grid(column = 0, row = 4)

# text box
slides_box = tk.Entry(window, width = 20)
# placing the text box
slides_box.grid(column = 1, row = 4)

# seconds persilde
seconds_label = tk.Label(window, text="Seconds Perslide")
seconds_label.grid(column = 0, row = 5)

# text box
seconds_box = tk.Entry(window, width = 20)
# placing the text box
seconds_box.grid(column = 1, row = 5)

# result box in gui
result_box = tk.Label(window, text="")
# placing result area
result_box.grid(column = 7, row = 5)

# search button
search_button= tk.Button(window, text='Submit', command = submit)
# placing the button
search_button.grid(column = 5, row =5)

# display the GUI window
window.mainloop()
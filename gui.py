import tkinter as tk

# creating the GUI window 
window = tk.Tk()
window.title('')
window.geometry('600x300')

def search():
    '''create a search button'''
    search_entry = search_box.get()
    if search_box:
        display_text = f'The content of the entry box are: {search_entry}.\nThe type of the content is {type(search_entry)}.'
        print(display_text)

        result_box.config(text=(search_entry))


# creating a label
label = tk.Label(text="Exposure To Signboard")
# placing the label
label.grid(column = 0, row = 0)

# search option
search_label = tk.Label(window, text="Search")
# placign the label
search_label.grid(column = 0, row = 3)

# text box
search_box = tk.Entry(window, width = 20)
# placing the text box
search_box.grid(column = 1, row = 3)

# result box in gui
result_box = tk.Label(window, text="")
# placing result area
result_box.grid(column = 7, row = 5)

# search button
search_button= tk.Button(window, text='Search', command = search)
# placing the button
search_button.grid(column = 5, row =5)

# display the GUI window
window.mainloop()
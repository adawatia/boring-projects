import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles = user_input.get()
    kilometers = str(round(miles * 1.61,2))
    output_str.set(kilometers + "Km")
    
# window = tk.Tk()
window = ttk.Window(themename="minty")
window.title("MtK")
window.geometry("320x150")

# Title
title_label = ttk.Label(master = window, text = "Miles to Kilomters", font = "Calibri 24 bold")
title_label.pack()

# User input field
input_frame = ttk.Frame(master = window)

user_input  = tk.IntVar()
input_field = ttk.Entry(master = input_frame,textvariable = user_input)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
input_field.pack(side = 'left', padx = 12)
button.pack(side = 'left')
input_frame.pack(padx = 15)

# Output
output_str = tk.StringVar()
output_label  = ttk.Label(master = window, font = "Calibri 24", textvariable = output_str)
output_label.pack(pady = 10)

# Run
window.mainloop()
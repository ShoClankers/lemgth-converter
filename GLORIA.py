import tkinter as tk
from tkinter import messagebox


def convert_length():
    try:
        inches = float(entry_inches.get())
        centimetres = inches * 2.54
        result_label.config(text=f"{inches} inches = {centimetres:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


window = tk.Tk()
window.title("Inches to Centimetres Converter")
window.geometry("350x200")

title_label = tk.Label(window, text="Length Converter", font=("Arial", 16))
title_label.pack(pady=10)

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

label_inches = tk.Label(input_frame, text="Enter length in inches:")
label_inches.pack(side=tk.LEFT)

entry_inches = tk.Entry(input_frame)
entry_inches.pack(side=tk.LEFT)

convert_button = tk.Button(window, text="Convert", command=convert_length)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
#Author: Alana Joshua
# This program expect Zero or two command-line argument and then prompt the users for a string of text and then output that text in the desired font
# If Zero, output text in a random font
# elif two,  output text in a specific font


import sys
import random
import tkinter as tk
from tkinter import font

def get_available_fonts():
    root = tk.Tk()
    fonts = list(font.families())
    root.destroy()
    return fonts

if len(sys.argv) == 1:
    fonts = get_available_fonts()
    font_name = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font_name = sys.argv[2]
else:
    sys.exit("Usage: python program.py [-f FONT]")

root = tk.Tk()
root.withdraw()

text = input("Enter your text: ")

try:
    font_obj = font.Font(family=font_name)
except tk.TclError:
    sys.exit(f"Font {font_name} not found")

label = tk.Label(root, text=text, font=font_obj)
label.pack()

root.mainloop()
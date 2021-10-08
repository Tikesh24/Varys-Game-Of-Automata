from service.FileHandler import initial_setup

initial_setup()
import tkinter as tk
from service.EventRunner import *

global root
root = tk.Tk()

root.title('Varys - Automata')
# root.iconbitmap('favicon.ico')
# ------------------------- Code to add widgets will go here-----------------
# Create a canvas with defined width and height and bg color.
canvas = tk.Canvas(root, height=80, width=280, bg="#003399")
canvas.pack()

# Create a frame inside with defined width and height and bg color.
frame = tk.Frame(root, bg="#0099cc")
frame.place(relwidth="0.8", relheight="0.8", relx=0.1, rely=0.1)

# Create button
record = tk.Button(frame, text="Record", padx=10, pady=5, fg="white", bg="#263042", command=get_events)
record.pack(side=tk.LEFT)

validate = tk.Button(frame, text="Validate", padx=10, pady=5, fg="white", bg="#263042", command=get_validation)
validate.pack(side=tk.LEFT)

play = tk.Button(frame, text="Play", padx=10, pady=5, fg="white", bg="#263042", command=play_events)
play.pack(side=tk.LEFT)

record.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
validate.place(relx=0.55, rely=0.5, anchor=tk.CENTER)
play.place(relx=0.86, rely=0.5, anchor=tk.CENTER)

# ---------------------------------------------------------------------------
# Run GUI
root.mainloop()

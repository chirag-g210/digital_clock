import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")
root.configure(bg="black")

def time():
    current_time = strftime('%I:%M:%S')
    current_ampm = strftime('%p')
    current_date = strftime('%d/%m/%Y')

    time_label.config(text=current_time)
    ampm_label.config(text=current_ampm)
    date_label.config(text=current_date)

    root.after(1000, time)

# frame for time
time_frame = tk.Frame(root, bg="black")
time_frame.pack()

time_label = tk.Label(time_frame, font=('Digital-7 Mono', 50), bg='black', fg='#00FFFF')
time_label.pack(side="left")

ampm_label = tk.Label(time_frame, font=('Digital-7 Mono', 25), bg='black', fg='#00FFFF')
ampm_label.pack(side="left", padx=5, anchor="n")

date_label = tk.Label(root, font=('Digital-7 Mono', 30), bg='black', fg='#00FFFF')
date_label.pack()

time()

root.mainloop()
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")
root.configure(bg="black")

def time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%d/%m/%Y')
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    time_label.after(1000, time)

time_label = tk.Label(root, font=('calibri', 60, 'bold'), background='black', foreground='red')
time_label.pack(anchor='center')

date_label = tk.Label(root, font=('calibri', 35, 'bold'), background='black', foreground='red')
date_label.pack(anchor='center')

time()

root.mainloop()
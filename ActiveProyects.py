import tkinter as tk
from tkinter import ttk
import os

ls_toAvoid = ['__','.i','00']
work = 'C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work'
proyect = 'C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Proyects'

work = ['work'+f for f in os.listdir(work) if f[:2] not in ls_toAvoid]
proyect = ['proy'+f for f in os.listdir(proyect) if f[:2] not in ls_toAvoid]

ls = work+proyect

txt = ''
for i in ls:
    txt = txt + i + '\n'

# Create the application window
window = tk.Tk()
 
# Create the user interface
my_label = ttk.Label(window, text=txt)
my_label.grid(row=1, column=2)

# Start the GUI event loop
window.mainloop()

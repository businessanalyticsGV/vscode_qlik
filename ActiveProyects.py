import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import os
import time

def Ventanita():
    ls_toAvoid = ['__','.i','00']
    work = 'C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Work'
    proyect = 'C:/Users/alexisalvarez/OneDrive - Grupo Vidanta/UPDATE/Proyects'

    work = ['WORK-'+f for f in os.listdir(work) if f[:2] not in ls_toAvoid]
    proyect = ['PROY-'+f for f in os.listdir(proyect) if f[:2] not in ls_toAvoid]

    ls = work+proyect

    txt = []
    for i in ls:
        comp = 'COMPLETED'
        proc = 'INPROCESS'
        if i[-len(comp):] == comp:
            txt.append((i[:len(i)-len(comp)-3],comp,0))
        elif i[-len(proc):] == proc:
            txt.append((i[:len(i)-len(proc)-3],proc,2))
        else:
            txt.append((i,'PENDING      ',1))

    df = pd.DataFrame(txt,columns = ['name','status','order'])
    df = df.sort_values(by = 'order', ascending = False)

    txt = ''
    for i in range(df.shape[0]):
        name = df.iloc[i][0]
        stat = df.iloc[i][1]
        txt = txt + stat + ' ' + name + '\n'

    # Create the application window
    window = tk.Tk(className=' My Activities')

    # Create the user interface
    my_label = ttk.Label(window, text=txt)
    my_label.grid(row=1, column=2)
    my_label.pack()
    
    # Start the GUI event loop
    window.mainloop()
    
Ventanita()
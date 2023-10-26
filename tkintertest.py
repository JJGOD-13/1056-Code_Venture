import tkinter as tk
from tkinter import ttk
from login import Login
from interface import Interface



# Make an interface class that inherits from the Tk class

interface = Interface("CodeVenture")

# Pass the interface object to the login frame

login = Login(interface)
login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

interface.mainloop()













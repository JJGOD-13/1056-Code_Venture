"""
The definition for the main interface of the application is below.
"""

# Import statements 
import tkinter as tk




class Interface(tk.Tk):

    # This line has instantiated the Tk class from the tkinter module
    # THe interface class is a subclass of the Tk class

    def __init__(self, title, width=960, height=540):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
"""
Definition for the homepage class
"""

# Import statements
from user import User
from learner import Learner
from parentEducator import ParentEducator
from progressTracker import ProgressTracker
import sqlite3 as sql
import tkinter as tk


class Homepage(tk.Frame):

    def __init__(self,master,user):
        """
        Initialize the homepage.
        
        INPUTS:
        self: The Homepage object.
        master: The tk root object.
        user: The user object.

        OUTPUTS:
        None
        
        """

        super().__init__(master=master)
        self.master = master

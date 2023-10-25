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
from update_db import update_db


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

        # Update the DB before starting
        update_db()

        super().__init__(master=master)
        self.master = master
        self.user = user

        # Check what the user type is

        if self.user.get_type() == "student":
            self.student_homepage()
        elif self.user.get_type() == "parent":  
            self.parent_homepage()
        elif self.user.get_type() == "educator":
            self.educator_homepage()
        else:
            self.admin_homepage()

    def student_homepage(self):
        pass

    def parent_homepage(self):
        pass

    def educator_homepage(self):
        pass

    def admin_homepage(self):
        pass

if __name__ == "__main__":
    # Test cases





        




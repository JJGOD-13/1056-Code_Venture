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

    def __init__(self,master,user=User):
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

        if self.user.user_type == "student":
            self.student_homepage(self.user)
        elif self.user.user_type() == "parent":  
            self.parent_homepage()
        elif self.user.user_type() == "educator":
            self.educator_homepage()
        else:
            self.admin_homepage()

    def student_homepage(self, user):
        """
        Definition for the main student page.
        """
        # Remove homepage from display
        self.place_forget()

        # Create and display the Learner(Student Homepage) frame
        learner_frame = Learner(self.master,user)
        learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def parent_homepage(self):
        pass

    def educator_homepage(self):
        pass

    def admin_homepage(self):
        pass

if __name__ == "__main__":
    # Test cases
    pass




        




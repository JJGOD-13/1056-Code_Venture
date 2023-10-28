"""
Definition for the homepage class
"""

# Import statements
from user import User
from learner import Learner
from parentEducator import ParentEducator
from admin import Admin
# from progressTracker import ProgressTracker
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
        elif self.user.user_type == "parent/educator":  
            self.parent_educator_homepage(self.user)
        # elif self.user.user_type() == "admin":
        #     self.admin_homepage()
        else:
            self.admin_homepage(self.user)

    def student_homepage(self, user):
        """
        Definition for the main student page.
        """
        # Remove homepage from display
        self.place_forget()

        # Create and display the Learner(Student Homepage) frame
        learner_frame = Learner(self.master,user)
        learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def parent_educator_homepage(self,user):
        """
        Definition for the main parent educator homepage.
        """
        self.place_forget()

        #create and display the parent educator frame
        parent_educator_frame = ParentEducator(self.master,user)
        parent_educator_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def admin_homepage(self,user):
        """
        Definition for the main admin homepage.
        """
        self.place_forget()

        #create and display the parent educator frame
        admin_frame = Admin(self.master,user)
        admin_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    # Test cases
    pass




        




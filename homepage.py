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
            self.student_homepage()
        elif self.user.user_type() == "parent":  
            self.parent_homepage()
        elif self.user.user_type() == "educator":
            self.educator_homepage()
        else:
            self.admin_homepage()

    def student_homepage(self):
        """
        Definition for the main student page.
        """
        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to the Student Page!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #button to start tutorials
        tutorial_button = tk.Button(self, text = "Start Tutorials") #add command to direct to tutorials page
        tutorial_button.grid(row=1, column=0, padx=10, pady=10)

        #button to start challenges 
        challenges_button = tk.Button(self, text = "Start Challenges") #add command to direct to challenges page
        challenges_button.grid(row=2, column=0, padx=10, pady=10)

        #button to view progress
        challenges_button = tk.Button(self, text = "View Progress so far") #add command to direct to progress report page
        challenges_button.grid(row=3, column=0, padx=10, pady=10)



    def parent_homepage(self):
        pass

    def educator_homepage(self):
        pass

    def admin_homepage(self):
        pass

if __name__ == "__main__":
    # Test cases
    pass




        




'''
The definition for the Admin class is below.
'''
# Import statements
from user import User
import tkinter as tk
from tkinter import Toplevel
import csv
import sqlite3 as sql


#Admin class definition
class Admin(tk.Frame):
    """
    Definition for the Learner class.
    This class accepts the following arguments:
    - User: a User object
    - admin_name: a string, which will be pulled from the User object
    - admin_id: an inr
    """

    def __init__(self,master, User):
        super().__init__(master=master)
        self.master = master
        self.User = User

        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to the Admin Page!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #button to user stats
        stats_button = tk.Button(self, text = "View User Stats", command=self.view_stats)
        stats_button.grid(row=1, column=0, padx=10, pady=10)
        
        #button for reviewing feedback
        review_button = tk.Button(self, text = "Review feedback received", command=self.read_feedback) 
        review_button.grid(row=2, column=0, padx=10, pady=10)

    #method to review all feedback
    def read_feedback(self):
        """
        Read and review all the feedback received.
        """
        file_feedback = "feedback.csv"
        all_feedback = []
        with open(file_feedback, "r") as review_file:
            for line in review_file:
                all_feedback.append(line)
        
        review_feedback_window = Toplevel(self)
        review_feedback_window.title("Feedback from users")
        review_feedback_window.geometry("600x400")
        
        #heading label
        heading_label = tk.Label(review_feedback_window,text = "All feedback \n (in the format username : feedback)", font=("Arial",10) )
        heading_label.grid(row=0, column=0, padx=10, pady=10)
        
        #all feedback label
        feedback_label = tk.Label(review_feedback_window,text = "\n".join(all_feedback) )
        feedback_label.grid(row=1, column=0, padx=10, pady=10)

    #method to view number of users registered
    def view_stats(self):
        """
        This methods runs a SQL query to get the total number of registered
        users 
        """
        #establish connection to the codeventure database
        stats_db = sql.connect('codeventure.db')
        
        #create a cursor object
        stats_c = stats_db.cursor()

        #execute the query
        stats_c.execute('SELECT COUNT(*) FROM users')

        #fetch the result
        total_users = stats_c.fetchone()[0]

        #display stats in a new toplevel window
        stats_window = Toplevel(self)
        stats_window.title("User Stats")
        stats_window.geometry("600x400")
        
        #heading label
        heading_label = tk.Label(stats_window,text = "User Stats", font=("Arial",14) )
        heading_label.grid(row=0, column=0, padx=10, pady=10)
        
        #all feedback label
        stats_label = tk.Label(stats_window,text = f"Total number of registered users : {total_users} ") 
        stats_label.grid(row=1, column=0, padx=10, pady=10)

        #close the connection to the databse
        stats_db.close()




if __name__ == "__main__":
    pass
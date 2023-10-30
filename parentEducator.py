'''
The definition for the ParentEducator class is below.
'''
# Import statements
from user import User
import tkinter as tk
from learner import Learner
import sqlite3 as sql
import csv

# ParentEducator class definition
class ParentEducator(tk.Frame):
    """
    - parentEducatorName: string
    - student: Learner
    - learnerProgress: ProgressTracker

    """

    def __init__(self, master, User):
        """
        Constructor of ParentEducator self
        """
        super().__init__(master=master)
        self.master = master
        self.User = User
        # self.Learner = Learner

        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to the Parent/Educator Page!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #button to view progress
        progress_button = tk.Button(self, text = "View Progress of child",font=("Calibri", 12), command=self.view_childs_progress) #add command to direct to progress report page
        progress_button.grid(row=1, column=0, padx=10, pady=10)
        
        #label for feedback
        feedback_label = tk.Label(self, text = "Your feedback is most welcome! \nType below, if you wish to give feedback.",font=("Calibri", 12))
        feedback_label.grid(row=2, column=0, padx=10, pady=10)

        #text widget for feedback 
        self.feedback_box = tk.Text(self,width=40, height=10)
        self.feedback_box.grid(row=3, column=0, padx=10, pady=10)

        #button to submit feedback
        submit_feedback_button = tk.Button(self, text = "Submit feedback",font=("Calibri", 10),command=self.store_feedback_csv) #add command to submit feedback
        submit_feedback_button.grid(row=4, column=0, padx=10, pady=10)

        #label for thank you
        self.thanks_label = tk.Label(self, text = "",font=("Calibri", 12))
        self.thanks_label.grid(row=5, column=0, padx=10, pady=10)

    
    def store_feedback_db(self):
        #retrieve user feedback from the text widget
        #from start to the end of the box
        user_feedback = self.feedback_box.get("1.0", tk.END)
        
        #establish connection to the codeventure database
        feedback_db = sql.connect('codeventure.db')
        
        #create a cursor object
        feedback_c = feedback_db.cursor()

        #insert the feedback into db feedback table
        feedback_c.execute("INSERT INTO feedback (giver_username, feedback_text) VALUES (?,?)", (self.User.get_username(), user_feedback))

        print("Feedback received")

        #commit the changes to the databse
        feedback_db.commit()

        #close the connection to the databse
        feedback_db.close()
    
    def store_feedback_csv(self):
        """
        This method stores the feedback given in a csv file.
        """
        #retrieve user feedback from the text widget
        #from start to the end of the box
        user_feedback = self.feedback_box.get("1.0", tk.END)
        
        username = self.User.get_username()
        #file path and name
        feedback_file = "feedback.csv"

        #open csv in append mode to prevent overwrite
        with open(feedback_file, "a") as feedback_storage_file:
            feedback_storage_file.write(f"{username} : {user_feedback}")
        
        #clear the text widget
        self.feedback_box.delete("1.0", tk.END)

        #dispaly thank you message
        self.thanks_label.config(text="Thank you for your feedback!")

    def view_childs_progress(self):

        # Ask the parent to input their child's first name and lastname

        firstname_label = tk.Label(self, text="Enter your child's first name:")
        firstname_label.grid(row=1, column=1, padx=10, pady=10)

        self.firstname_entry = tk.Entry(self)
        self.firstname_entry.grid(row=1, column=2, padx=10, pady=10)

        lastname_label = tk.Label(self, text="Enter your child's last name:")
        lastname_label.grid(row=2, column=1, padx=10, pady=10)

        self.lastname_entry = tk.Entry(self)
        self.lastname_entry.grid(row=2, column=2, padx=10, pady=10)

        # Make a button to submit the child's name
        submit_button = tk.Button(self, text="Submit", command=self.get_childs_progress)
        submit_button.grid(row=3, column=2, padx=10, pady=10)

    def get_childs_progress(self):

        # Open a connection to the database

        db = sql.connect("codeventure.db")
        c = db.cursor()

        # Get the child's first name and last name from the entry boxes

        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()

        # Get the child's username from the users table

        c.execute("SELECT username FROM users WHERE first_name = ? AND last_name = ?", (firstname, lastname))
        username = c.fetchone()[0]

        # Get the child's progress from the students table
        
        c.execute("SELECT level FROM students WHERE username = ?", (username,))
        progress = c.fetchone()[0]

        # Display the child's progress

        progress_label = tk.Label(self, text=f"{firstname} {lastname}'s progress so far: {progress} out of 5 lessons completed.")
        progress_label.grid(row=4, column=0, padx=10, pady=10)

        # Close the connection to the database

        db.close()

        


if __name__ == "__main__":
    # Test cases
    # Create a User object
    user1 = User("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1)
    learner1 = Learner(user1, 14, 1)
    user2 = User("Kate", "Simpson", "someemail@gmail.com", "password1", "kateSi", "parent", 1)
    parent1 = ParentEducator(user2, learner1)
    feedback = parent1.give_feedback()
    

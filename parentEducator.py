'''
The definition for the ParentEducator class is below.
'''
# Import statements
from user import User
import tkinter as tk
from learner import Learner
import sqlite3 as sql

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
        progress_button = tk.Button(self, text = "View Progress of child",font=("Calibri", 12)) #add command to direct to progress report page
        progress_button.grid(row=1, column=0, padx=10, pady=10)
        
        #label for feedback
        feedback_label = tk.Label(self, text = "Your feedback is most welcome! \nType below, if you wish to give feedback.",font=("Calibri", 12))
        feedback_label.grid(row=2, column=0, padx=10, pady=10)

        #text widget for feedback 
        self.feedback_box = tk.Text(self,width=40, height=10)
        self.feedback_box.grid(row=3, column=0, padx=10, pady=10)

        #button to submit feedback
        submit_feedback_button = tk.Button(self, text = "Submit feedback",font=("Calibri", 10),command=self.store_feedback_db) #add command to submit feedback
        submit_feedback_button.grid(row=4, column=0, padx=10, pady=10)

    # def get_learner_progress(self):
    #     return self.learner_progress
    # def get_learner(self):
    #     return self.learner


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


        #commit the changes to the databse
        feedback_db.commit()

        #close the connection to the databse
        feedback_db.close()

        #clear the text box
        self.feedback_box.delete("1.0", tk.END)

        # #display a message to the user
        feedback_submitted_label = tk.Label(self, text="Feedback submitted!", fg="green")
        feedback_submitted_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)
        



if __name__ == "__main__":
    # Test cases
    # Create a User object
    user1 = User("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1)
    learner1 = Learner(user1, 14, 1)
    user2 = User("Kate", "Simpson", "someemail@gmail.com", "password1", "kateSi", "parent", 1)
    parent1 = ParentEducator(user2, learner1)
    feedback = parent1.give_feedback()
    

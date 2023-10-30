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
    

    def __init__(self, master, User):
        """
         
        Definition for the Learner class.
        attributes
        INPUTS:
        self: The Learner object.
        master: The tk root object.
        User: The User object

        OUTPUTS:
        None
    
        """
        super().__init__(master=master)
        self.master = master
        self.User = User

        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to the Parent/Educator Page!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)
        
        #username entry label
        username_label = tk.Label(self,text = "Enter your child's username to view report")
        username_label.grid(row=1, column=0, padx=10, pady=10)

        #button to view progress
        progress_button = tk.Button(self, text = "View Progress of child",font=("Calibri", 12), command=self.view_child_report) #add command to direct to progress report page
        progress_button.grid(row=2, columnspan=2, padx=10, pady=10)

        #Entry field for entering child username
        self.child_username = tk.StringVar()
        self.child = tk.Entry(self, textvariable=self.child_username)
        self.child.grid(row=1, column=1, padx=10, pady=10)
        
        #label for feedback
        feedback_label = tk.Label(self, text = "Your feedback is most welcome! \nType below, if you wish to give feedback.",font=("Calibri", 12))
        feedback_label.grid(row=3, columnspan=2, padx=10, pady=10)

        #text widget for feedback 
        self.feedback_box = tk.Text(self,width=40, height=10)
        self.feedback_box.grid(row=4, columnspan=2, padx=10, pady=10)

        #button to submit feedback
        submit_feedback_button = tk.Button(self, text = "Submit feedback",font=("Calibri", 10),command=self.store_feedback_csv) #add command to submit feedback
        submit_feedback_button.grid(row=5, columnspan=2, padx=10, pady=10)

        #label for thank you
        self.thanks_label = tk.Label(self, text = "",font=("Calibri", 12))
        self.thanks_label.grid(row=6, columnspan=2, padx=10, pady=10)
    
    def view_child_report(self):
        """
        Event handler for viewing child's progress report
        """
        learner_child_username = self.child_username.get()

        progress_window = tk.Toplevel(self.master)
        progress_window.title(f"Progress Report of {learner_child_username}")
        progress_window.geometry("600x450")

        try:
            with open(f'{learner_child_username}_progress.csv', "r") as progress_file:
                lines = progress_file.readlines()
                if len(lines) > 1: #check if the file has content
                    level, index = lines[1].strip().split(',')
                    completed_tut = int(index)
                else:
                    completed_tut = 0

            with open(f'{learner_child_username}_chall_progress.csv', "r") as challenge_file:
                lines_challenge = challenge_file.readlines()
                if len(lines_challenge) > 1: #check if the file has content
                    ques_index = lines_challenge[1].strip()
                    completed_chall = int(ques_index)
                else:
                    completed_chall= 0

            title_label = tk.Label(progress_window, text=f"Progress Report", font=("Arial", 15))
            title_label.pack(padx=10, pady=10)


            progress_label = tk.Label(progress_window, text=f"Tutorials completed: {completed_tut}")
            progress_label.pack( padx=10, pady=10)

            progress_chall_label = tk.Label(progress_window, text=f"Challenges completed: {completed_chall}")
            progress_chall_label.pack( padx=10, pady=10)

        except FileNotFoundError:
            completed_tut = 0
            completed_chall= 0

            title_label = tk.Label(progress_window, text=f"Progress Report", font=("Arial", 15))
            title_label.pack(padx=10, pady=10)

            info_label = tk.Label(progress_window, text="No progress file found for the username you entered.")
            info_label.pack( padx=10, pady=10)
            #error handling if the user has not done anything yet 
            #and hence file does not exist
            
       
        
    
    def store_feedback_db(self):
        """
        Method to store user feedback in the codeventure.db
        """
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


    

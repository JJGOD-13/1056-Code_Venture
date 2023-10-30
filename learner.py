'''
The definition for the Learner class is below.
'''
# Import statements
from user import User
import tkinter as tk
from tutorial import Tutorials
from challenges import Challenges
import sqlite3 as sql
#from progressTracker import ProgressTracker

# Learner class definition
class Learner(tk.Frame):

    def __init__(self,
                 master, 
                 User=User
                ):
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
        
        # Initialise the parent class
        super().__init__(master=master)
        self.master = master
        self.User = User
        self.username_learner = User.get_username()
    
        
        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to the Student Page!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #button to start tutorials
        tutorial_button = tk.Button(self, text = "Start Tutorials", command=self.start_tutorial) 
        tutorial_button.grid(row=1, column=0, padx=10, pady=10)

        #button to start challenges 
        challenges_button = tk.Button(self, text = "Start Challenges",command=self.start_challenge) 
        challenges_button.grid(row=2, column=0, padx=10, pady=10)

        #button to view progress
        progress_button = tk.Button(self, text = "View Progress so far", command=self.view_user_progress) 
        progress_button.grid(row=3, column=0, padx=10, pady=10)
        
    
    def go_back_to_home(self):
        """
        Event handler to go back to the welcome login page
        """
        self.place_forget()
        # self.home_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def start_tutorial(self):
        """
        Event handler to show tutorial page.
        """
        self.place_forget()
        tutorial_frame = Tutorials(self.master, self, self.username_learner)
        tutorial_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def start_challenge(self):
        """
        Event handler to show tutorial page.
        """
        self.place_forget()
        challenge_frame = Challenges(self.master,self,self.username_learner)
        challenge_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    
    #csv method

    def view_user_progress(self):
        """
        Event handler to view user progress
        """
        progress_window = tk.Toplevel(self.master)
        progress_window.title("Progress Report")
        progress_window.geometry("600x450")

        completed_tut = 0
        completed_adv = 0

        try:
            with open(f'{self.username_learner}_progress.csv', "r") as progress_file:
                # lines = progress_file.readlines()
                # if len(lines) > 1: #check if the file has content
                    for line in progress_file:
                        level, index = line.strip().split(',')
                        if level == "basic":
                            completed_tut = int(index)
                        if level == "advanced":
                            completed_adv = int(index)

                # else:
                #     completed_tut = 0
                #     completed_adv = 0

            with open(f'{self.username_learner}_chall_progress.csv', "r") as challenge_file:
                lines_challenge = challenge_file.readlines()
                if len(lines_challenge) > 1: #check if the file has content
                    ques_index = lines_challenge[1].strip()
                    completed_chall = int(ques_index)
                else:
                    completed_chall= 0
        except FileNotFoundError:
            completed_tut = 0
            completed_chall= 0
            completed_adv = 0
            #error handling if the user has not done anything yet 
            #and hence file does not exist
            pass 
       
        title_label = tk.Label(progress_window, text=f"Progress Report", font=("Arial", 15))
        title_label.pack(padx=10, pady=10)


        progress_label = tk.Label(progress_window, text=f"Basic Tutorials completed: {completed_tut}")
        progress_label.pack( padx=10, pady=10)

        progress_adv_label = tk.Label(progress_window, text=f"Advanced Tutorials completed: {completed_adv}")
        progress_adv_label.pack( padx=10, pady=10)

        progress_chall_label = tk.Label(progress_window, text=f"Challenges completed: {completed_chall}")
        progress_chall_label.pack( padx=10, pady=10)

    
    #database method

    def view_progress(self):
        """
        Event handler to view progress.
        """

        # Get the progress from the database
        db = sql.connect('codeventure.db')
        c = db.cursor()
        c.execute("SELECT experience FROM students WHERE username = ?", (self.User.get_username(),))
        result = c.fetchall()
        db.close()

         # Create a label to display the progress
        progress_label = tk.Label(self, text=f"Your progress so far: {result} out of 5 lessons completed.")
        progress_label.grid(row=4, column=0, padx=10, pady=10)


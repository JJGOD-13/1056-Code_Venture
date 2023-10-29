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
    """
    Definition for the Learner class.
    This class accepts the following arguments:
    - User: a User object
    - display_name: a string, which will be pulled from the User object
    - age: an integer, which will be pulled from the User object
    - progressLevel: and integer whose initial value will be 0 and whose setting i have to figure out. (set to zero initially?)
    """

    def __init__(self,
                 master, 
                 User=User
                ):
        
        # Initialise the parent class
        super().__init__(master=master)
        self.master = master
        self.User = User

        # self.display_name = User.get_username()
        # self.age = age
        # self.progressLevel = progressLevel

        
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
        
        # #button to go back to the login page
        # go_to_home_page = tk.Button(self, text = "Go Back",command=self.go_back_to_home) 
        # go_to_home_page.grid(row=4, columnspan=3, padx=10, pady=10)

        #initialising a progress tracker for each student
        #self.progress_tracker = ProgressTracker(self)
    
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
        tutorial_frame = Tutorials(self.master, self)
        tutorial_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def start_challenge(self):
        """
        Event handler to show tutorial page.
        """
        self.place_forget()
        challenge_frame = Challenges(self.master,self)
        challenge_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    
    #csv method
    
    def view_user_progress(self):
        progress_window = tk.Toplevel(self.master)
        progress_window.title("Progress Report")
        progress_window.geometry("600x450")

        try:
            with open('progress.csv', "r") as progress_file:
                lines = progress_file.readlines()
                if len(lines) > 1: #check if the file has content
                    level, index = lines[1].strip().split(',')
                    completed_tut = int(index)
                else:
                    completed_tut = 0

            with open('challenge_progress.csv', "r") as challenge_file:
                lines_challenge = challenge_file.readlines()
                if len(lines_challenge) > 1: #check if the file has content
                    ques_index = lines_challenge[1].strip()
                    completed_chall = int(ques_index)
                else:
                    completed_chall= 0
        except FileNotFoundError:
            completed_chall= 0
            #error handling if the user has not done anything yet 
            #and hence file does not exist
            pass 
       
        title_label = tk.Label(progress_window, text=f"Progress Report", font=("Arial", 15))
        title_label.pack(padx=10, pady=10)


        progress_label = tk.Label(progress_window, text=f"Tutorials completed: {completed_tut}")
        progress_label.pack( padx=10, pady=10)

        progress_chall_label = tk.Label(progress_window, text=f"Challenges completed: {completed_chall}")
        progress_chall_label.pack( padx=10, pady=10)


    def get_age(self):
        return self.age

    def setAge(self, age):
        self.age = age
    
    def addProgressLevel(self):
        self.progressLevel += 1
    
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





    


if __name__ == "__main__":
    # Test cases
    
    # Create a User object
    user1 = User("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1)

    print( user1.getUsername())

    check = user1.__str__()
    # Create a Learner object
    learner1 = Learner(user1, 25, 0)
    print(learner1.age)
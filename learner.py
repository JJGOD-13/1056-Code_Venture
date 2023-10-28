'''
The definition for the Learner class is below.
'''
# Import statements
from user import User
import tkinter as tk
from tutorial import Tutorials
from challenges import Challenges
from progressTracker import ProgressTracker

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
                 User
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
        tutorial_button = tk.Button(self, text = "Start Tutorials", command=self.start_tutorial) #add command to direct to tutorials page
        tutorial_button.grid(row=1, column=0, padx=10, pady=10)

        #button to start challenges 
        challenges_button = tk.Button(self, text = "Start Challenges",command=self.start_challenge) #add command to direct to challenges page
        challenges_button.grid(row=2, column=0, padx=10, pady=10)

        #button to view progress
        challenges_button = tk.Button(self, text = "View Progress so far", command=self.view_report) #add command to direct to progress report page
        challenges_button.grid(row=3, column=0, padx=10, pady=10)
        
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
    
    def view_report(self):
        """
        Event handler to show progress report.
        """
        self.place_forget()
        report_frame = ProgressTracker(self.master)
        report_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def get_age(self):
        return self.age

    def setAge(self, age):
        self.age = age
    
    def addProgressLevel(self):
        self.progressLevel += 1

    #updating the progress of the learner in the progress tracker
    # def tutorial_progress(self):
    #     self.progress_tracker.set_tutorial()
    
    # def challenge_progress(self):
    #     self.progress_tracker.set_challenge()

    # def score_progress(self,new_score):
    #     self.progress_tracker.set_score(new_score)



    


if __name__ == "__main__":
    # Test cases
    
    # Create a User object
    user1 = User("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1)

    print( user1.getUsername())

    check = user1.__str__()
    # Create a Learner object
    learner1 = Learner(user1, 25, 0)
    print(learner1.age)
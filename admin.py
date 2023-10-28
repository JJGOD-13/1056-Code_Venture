'''
The definition for the Admin class is below.
'''
# Import statements
from user import User
import tkinter as tk


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
        challenges_button = tk.Button(self, text = "View User Stats") #add command to direct to progress report page
        challenges_button.grid(row=1, column=0, padx=10, pady=10)
        
        #button for reviewing feedback
        challenges_button = tk.Button(self, text = "Review feedback received") #add command to direct to challenges page
        challenges_button.grid(row=2, column=0, padx=10, pady=10)


if __name__ == "__main__":
    pass
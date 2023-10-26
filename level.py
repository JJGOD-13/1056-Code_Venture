'''
Class definition for Level Class
'''
import tkinter as tk
from challenges import Challenges
from tutorial import Tutorials
class Levels(tk.Frame):
    def __init__(self, master,level_number, Challenges, Tutorials):
        """
        Constructor for the Level Class
        """
        # Initialise the parent class
        super().__init__(master=master)
        self.master = master

        self.level_number = 1 #initialised to 1 
        self.challenges = [] # list of Challenges related to the level (to be appended as per the level)
        self.tutorials = [] #list of Tutorials related to the level (to be appended as per the level)

        #Label for message to choose the level

        #Column 1 Label saying "Just starting? Choose Basics"
        #Buttons for basic level 

        #Column 2 Label saying "Wanna improve your existing skills? Choose Advanced"
        #Button for advanced level

        #accessor methods
        def get_level_challenges(self):
            return self.challenges
        def get_level_tutorials(self):
            return self.tutorials
        def get_level_number(self):
            return self.level_number
        
        #setter methods
        def add_level_number(self):
            self.level_number += 1

        def set_tutorials (self, new_tutorials):
            self.tutorials =  new_tutorials
        
        def set_challenges(self, new_challenges):
            self.challenges = new_challenges

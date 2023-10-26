'''
The definintion for challenges class
'''
#import statements
import random
import tkinter as tk

class Challenges(tk.Frame):
    """
    Definition for the challenges class.
    attributes
    - challenge_title 
    - challenge_content
    """

    def __init__(self, 
                 master
                 ):
        # self.challenge_title = challenge_title
        # self.challenge_content = challenge_content

        # Initialise the parent class
        super().__init__(master=master)
        self.master = master

        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to Challenges!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #welcome message 2 label
        welcome_label2 = tk.Label(self,text = "Let's be the masters", font=("Arial",12) )
        welcome_label2.grid(row=1, columnspan=2, padx=10, pady=10)

        #button to tutorial 1
        tutorial_button1 = tk.Button(self, text = "Challenge 1: Intro") #add command to direct to tutorials page
        tutorial_button1.grid(row=2, column=0, padx=10, pady=10)

        #button to tutorial 2
        tutorial_button2 = tk.Button(self, text = "Challenge 2: Basics") #add command to direct to tutorials page
        tutorial_button2.grid(row=3, column=0, padx=10, pady=10)
        
    #accessor methods
    def get_challenge_title(self):
        return self.challenge_title

    def get_challenge_content(self):
        return self.challenge_content
    
    #setter methods
    def set_challenge_title(self, new_challenge_title):
        self.challenge_title = new_challenge_title

    def set_challenge_content(self, new_challenge_content):
        self.challenge_content = new_challenge_content
    
    #function for displaying motivational messages
    def disp_motivational_message(self):
        messages_list = ["Keep up the good work!", "You can do it!", "Keep going!"]
        message = random.choice(messages_list)
        print(message)


if __name__ == "__main__":
    challenge1 = Challenges("New Challenge", "Random content")
    challenge1.disp_motivational_message()
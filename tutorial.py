'''
The definintion for tutorial class
'''
#import statements
import random
import tkinter as tk

class Tutorials(tk.Frame):
    """
    Definition for the Tutorial class.
    attributes
    - tutorial_title 
    - tutorial_content
    """

    def __init__(self, 
                 master
                 ):
        
        # Initialise the parent class
        super().__init__(master=master)
        self.master = master

        #label to show tutorial content
        #declared as an attribute so that tutorial contents fucntions can
        #access it
        self.tutorial_content = tk.Label(self, text ="",font=("Arial",12), wraplength=700)
        self.tutorial_content.grid(row=3, columnspan=4, padx=10, pady=10)

        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to Tutorials!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #welcome message 2 label
        welcome_label2 = tk.Label(self,text = "Your programming journey begins", font=("Arial",12) )
        welcome_label2.grid(row=1, columnspan=2, padx=10, pady=10)

        

        #button to tutorial 1
        tutorial_button1 = tk.Button(self, text = "Tutorial 1: Intro to Coding",command=self.tutorial_one) #add command to direct to tutorials page
        tutorial_button1.grid(row=2, column=0, padx=10, pady=10)

        #button to tutorial 2
        tutorial_button2 = tk.Button(self, text = "Tutorial 2: Basics",command=self.tutorial_two) #add command to direct to tutorials page
        tutorial_button2.grid(row=2, column=1, padx=10, pady=10)

        #button to tutorial 3
        tutorial_button2 = tk.Button(self, text = "Tutorial 3: Conditionals",command=self.tutorial_three) #add command to direct to tutorials page
        tutorial_button2.grid(row=2, column=2, padx=10, pady=10)

        
    #method for tutorial 1 content
    def tutorial_one(self):
        """
        Method for tutorial one content
        """
        tutorial_material = """
        Tutorial 1: Intro to Coding
        In this tutorial, we will have am introduction to what exactly 
        coding means. And of course, how fun is it!
        """
        self.tutorial_content.config(text=tutorial_material)

    #method for tutorial 2 content
    def tutorial_two(self):
        """
        Method for tutorial two content
        """
        tutorial_material = """
        Tutorial 2: Basics
        In this tutorial, we will start to learn the basics of Python. 
        We will start with arithmetic operations.
        """
        self.tutorial_content.config(text=tutorial_material)
    
    #method for tutorial 3 content
    def tutorial_three(self):
        """
        Method for tutorial three content
        """
        tutorial_material = """
        Tutorial 3: Conditionals
        In this tutorial, we will learn about conditionals in Python- 
        if-else structures.
        """
        self.tutorial_content.config(text=tutorial_material)

    #accessor methods
    def get_tutorial_title(self):
        return self.tutorial_title

    def get_tutorial_content(self):
        return self.tutorial_content
    
    #setter methods
    def set_tutorial_title(self, new_tutorial_title):
        self.tutorial_title = new_tutorial_title

    def set_tutorial_content(self, new_tutorial_content):
        self.tutorial_content = new_tutorial_content
    
    #function for displaying motivational messages
    def disp_motivational_message(self):
        messages_list = ["Keep up the good work!", "You can do it!", "Keep going!"]
        message = random.choice(messages_list)
        print(message)



if __name__ == "__main__":
    tutorial1 = Tutorials("New Tutorial", "Random content")
    tutorial1.disp_motivational_message()
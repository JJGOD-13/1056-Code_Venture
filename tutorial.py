'''
The definition for tutorial class
'''
#import statements
import random
import tkinter as tk
import csv

class Tutorials(tk.Frame):

    def __init__(self, 
                 master,
                 learner_page,
                 learner_username
                 ):
        """
        Definition for the Tutorial class.
        INPUTS:
        self: The Tutorial object.
        master: The tk root object.
        learner_page: The Learner Object
        learner_username: Username of the learner

        OUTPUTS:
        None
        """
        
        # Initialise the parent class
        super().__init__(master=master)
        self.master = master
        
        #username of the student
        self.username_student = learner_username

        #progress variables
        
        self.progress_tutorial = {"basic":0, "advanced":0}
        self.learner_page = learner_page

        self.done_tutorials = {"basic": False, "advanced":True}

        #load the progress
        self.load_progress()

        #label to show tutorial content
        #declared as an attribute so that tutorial contents fucntions can
        #access it
        self.tutorial_content = tk.Label(self, text ="",font=("Arial",12), wraplength=700, height=10, width=50)
        self.tutorial_content.grid(row=3, columnspan=4, padx=10, pady=10)

        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to Tutorials!", font=("Arial",18),width=20 )
        welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #welcome message 2 label
        welcome_label2 = tk.Label(self,text = "Your programming journey begins", font=("Arial",12), width=40)
        welcome_label2.grid(row=1, columnspan=2, padx=10, pady=10)

        #motivational message label
        self.message_label = tk.Label(self,text = "", width=25)
        self.message_label.grid(row=5, columnspan=2, padx=10, pady=10)


        #button to show "Basics" tutorial 
        self.tutorial_button1 = tk.Button(self, text = "Tutorial: Basics",command=self.show_basic_tutorial) 
        self.tutorial_button1.grid(row=2, column=0, padx=10, pady=10)

        #button to show "Advanced" tutorial 
        self.tutorial_button2 = tk.Button(self, text = "Tutorial: Advanced",command=self.show_advanced_tutorial) 
        self.tutorial_button2.grid(row=2, column=1,sticky=tk.E, padx=10, pady=10)

        #button for next tutorial
        tutorial_next = tk.Button(self, text = "Next Tutorial",command=self.tutorial_next) 
        tutorial_next.grid(row=4, column=1,sticky=tk.E, padx=10, pady=10)
        
        #button for previous tutorial
        tutorial_prev = tk.Button(self, text = "Previous Tutorial",command=self.tutorial_prev) 
        tutorial_prev.grid(row=4, column=0, padx=10, pady=10)

        #button to go back to the student page
        go_back_student_page = tk.Button(self, text = "Go Back",command=self.go_back_to_learner) 
        go_back_student_page.grid(row=6, columnspan=2, padx=10, pady=10)

    
        self.basic_tutorials = [
            """Tutorial 1: Intro to Coding
        In this tutorial, we will have am introduction to what exactly 
        coding means. And of course, how fun is it! 
            """, """
        Tutorial 2: Basics
        In this tutorial, we will start to learn the basics of Python. 
        We will start with arithmetic operations.
        ""","""
        Tutorial 3: Conditionals
        In this tutorial, we will learn about conditionals in Python- 
        if-else structures.
        ""","""
        Tutorial 4: Loops (For)
        In this tutorial, we will start to learn about loops. 
        We will start with "for" loops.
        ""","""
        Tutorial 5: Loops(While)
        In this tutorial, we will learn about while loops in Python
        and how they are different to for loops.
        """
        ]
        self.advanced_tutorials = [
            """Tutorial 1: Intro to OOP
        In this tutorial, we will have am introduction to what exactly 
        Object Oriented Programming is. 
            """, """
        Tutorial 2: Classes in OOP
        In this tutorial, we will start to learn how to write and use classes
        in OOP.
        ""","""
        Tutorial 3: Methods in OOP
        In this tutorial, we will learn about different types of 
        methods in OOP.
        """
        ]
        
        #set current tutorial level
        self.level_current = None
        self.tutorial_index = None

    #method to go back to the learner(student) page
    def go_back_to_learner(self):
        """
        Event handler to go back to the student page
        """
        self.place_forget()
        self.learner_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #method for basic tutorial 
    def show_basic_tutorial(self):
        """
        Event handler to show the basic tutorial
        """
        self.level_current = "basic"
        self.tutorial_index = 0
        self.show_current_tutorial()

    #method for advanced tutorial 
    def show_advanced_tutorial(self):
        """
        Event handler to show the advanced tutorial
        """
        self.level_current = "advanced"
        self.tutorial_index = 0
        self.show_current_tutorial()

    def show_current_tutorial(self):
        """
        Event handler to show current tutorial
        """
        if self.level_current == "basic":
            tutorial = self.basic_tutorials
        elif self.level_current == "advanced":
            tutorial = self.advanced_tutorials

        if self.tutorial_index < len(tutorial):
            self.tutorial_content.config(text=tutorial[self.tutorial_index])

            if self.level_current == "basic":
                self.progress_tutorial["basic"] = self.tutorial_index
            elif self.level_current == "advanced":
                self.progress_tutorial["advanced"] = self.tutorial_index
            #save progress for each tutorial
            self.save_progress()
        else:
            self.tutorial_content.config(text= "Yay! You completed all the tutorials.")
            if self.level_current == "basic":
                self.tutorial_button1.config(text = "Tutorial: Basics ✅")
            elif self.level_current == "advanced":
                self.tutorial_button2.config(text = "Tutorial: Advanced ✅")

        return self.level_current, self.tutorial_index


    def tutorial_next(self):
        """
        Event handler to show next tutorial
        """
        if self.level_current and self.tutorial_index is not None:
            self.tutorial_index += 1
            self.show_current_tutorial()
            if self.tutorial_index < len(self.basic_tutorials):
                self.disp_motivational_message()


    def tutorial_prev(self):
        """
        Event handler to show previous tutorial
        """
        if self.level_current and self.tutorial_index is not None:
            if self.tutorial_index > 0:
                self.tutorial_index -= 1
                self.show_current_tutorial()

    #function for displaying motivational messages
    def disp_motivational_message(self):
        """
        Event handler to show display motivational messages
        """
        messages_list = ["Keep up the good work!", "You can do it!", "Keep going!"]
        message = random.choice(messages_list)
        self.message_label.config(text=message)

    #method to save progress in a csv file
    def save_progress(self):
        """
        Method to save user progress
        """
        with open(f'{self.username_student}_progress.csv', "w") as progress_file:
            col_names = ['level', 'index']
            progress_file.write(",".join(col_names) + '\n')

            #progress_file.write(f'{self.level_current}, {self.tutorial_index + 1}\n')
            progress_file.write(f'basic, {self.progress_tutorial["basic"]}\n')
            progress_file.write(f'advanced, {self.progress_tutorial["advanced"]}\n')

    #method to load progress
    def load_progress(self):
        """
        Method to load user progress when the program is restarted
        """
        try:
            with open(f'{self.username_student}_progress.csv', "r") as progress_file:
                lines = progress_file.readlines()
                if len(lines) > 1: #check if the file has content
                    level, index = lines[1].strip().split(',')
                    self.progress_tutorial[level] = int(index)

                    #return level, int(index)
                    return self.progress_tutorial["basic"], self.progress_tutorial["advanced"]
        except FileNotFoundError:
            #error handling if the user has not done anything yet 
            #and hence file does not exist
            pass 
        return None, None
    

    
    
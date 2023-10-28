'''
The definition for the ProgressTracker class is below.
'''
# Import statements
from user import User
# from learner import Learner
import tkinter as tk


class ProgressTracker(tk.Frame):
    """
    - userProgress: Learner
    - totalScores: int
    - totalTutorialCompleted: int
    - totalChallengesCompleted: int

    """

    def __init__(self,
                 master,  
                 ):
        
        # Initialise the parent class
        super().__init__(master=master)
        self.master = master

        # TODO CONNECT THE LEARNER TO THE PROGRESS REPORT
        #self.Learner = Learner

        #for now create just a template 

        #heading label
        heading_label = tk.Label(self,text = "Progress Report", font=("Arial",18) )
        heading_label.grid(row=0, columnspan=2, padx=10, pady=10)

        #tutorials completed label
        tutorial_label = tk.Label(self,text = "Tutorials completed: " )
        tutorial_label.grid(row=1, column=0, padx=10, pady=10)

        #challenges completed label
        challenges_label = tk.Label(self,text = "Challenges completed: " )
        challenges_label.grid(row=2, column=0, padx=10, pady=10)

        #fetch data from db to show the actual numbers
        # 

       
        

    # #accessor methods 
    # def get_total_scores(self):
    #     return self.total_scores
    
    # def get_total_tutorial_completed(self):
    #     return self.total_tutorial_completed
    
    # def get_total_challenges_completed(self):
    #     return self.total_challenges_completed
    
    # #setter methods
    # def set_score(self, new_score):
    #     #ensuring no negative score is added
    #     if new_score > 0:
    #         self.total_scores += new_score

    # def set_tutorial(self):
    #     self.total_challenges_completed += 1

    # def set_challenge(self):
    #     self.total_challenges_completed +=1 

    def report(self):
        print(f"The report for {self.Learner.display_name}")
        print(f"Total score = {self.total_scores}")
        print(f"Total Tutorials Completed = {self.total_tutorial_completed}")
        print(f"Total challenges completed = {self.total_challenges_completed}")
        


if __name__ == "__main__":
    pass
    # Test cases
    #feature view learner progress report 
    # user1 = User("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1)
    # learner1 = Learner(user1, 14, 1)
    # pg = ProgressTracker(learner1,10, 2, 1)
    # pg.report()
'''
The definition for the ProgressTracker class is below.
'''
# Import statements
from user import User
from learner import Learner


class ProgressTracker():
    """
    - userProgress: Learner
    - totalScores: int
    - totalTutorialCompleted: int
    - totalChallengesCompleted: int

    """

    def __init__(self,  
                 Learner,
                 total_scores = 0, 
                 total_tutorial_completed = 0,
                 total_challenges_completed = 0,
                 ):
        self.Learner = Learner
        self.total_scores = total_scores
        self.total_tutorial_completed = total_tutorial_completed
        self.total_challenges_completed = total_challenges_completed
        

    #accessor methods 
    def get_total_scores(self):
        return self.total_scores
    
    def get_total_tutorial_completed(self):
        return self.total_tutorial_completed
    
    def get_total_challenges_completed(self):
        return self.total_challenges_completed
    
    #setter methods
    def set_score(self, new_score):
        #ensuring no negative score is added
        if new_score > 0:
            self.total_scores += new_score

    def set_tutorial(self):
        self.total_tutorial_completed += 1

    def set_challenge(self):
        self.total_challenges_completed +=1 

    def report(self):
        print(f"The report for {self.Learner.first_name}")
        print(f"Total score = {self.total_scores}")
        print(f"Total Tutorials Completed = {self.total_tutorial_completed}")
        print(f"Total challenges completed = {self.total_challenges_completed}")
        


if __name__ == "__main__":
    # Test cases
    #feature view learner progress report 
    
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    pg = ProgressTracker(learner1,10, 2, 1)
    pg.report()
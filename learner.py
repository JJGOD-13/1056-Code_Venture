'''
The definition for the Learner class is below.
'''
# Import statements
from user import User
#from progressTracker import ProgressTracker

# Learner class definition
class Learner():
    """
    Definition for the Learner class.
    This class accepts the following arguments:
    - User: a User object
    - display_name: a string, which will be pulled from the User object
    - age: an integer, which will be pulled from the User object
    - progressLevel: and integer whose initial value will be 0 and whose setting i have to figure out. (set to zero initially?)
    """

    def __init__(self, 
                 User, 
                 age,
                 progressLevel):
        self.User = User
        self.display_name = User.get_username()
        self.age = age
        self.progressLevel = progressLevel

        #initialising a progress tracker for each student
        #self.progress_tracker = ProgressTracker(self)

    def getAge(self):
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
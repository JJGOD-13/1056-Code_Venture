'''
The definition for the Learner class is below.
'''
# Import statements
from user import User
#from progressTracker import ProgressTracker

# Learner class definition
class Learner(User):
    """
    Definition for the Learner class.
    This class accepts the following arguments:
    - User: a User object
    - display_name: a string, which will be pulled from the User object
    - age: an integer, which will be pulled from the User object
    - progressLevel: and integer whose initial value will be 0 and whose setting i have to figure out. (set to zero initially?)
    """

    def __init__(self, 
                 first_name,
                 last_name,
                 email, 
                 password, 
                 username,
                 user_type, # type is either "student" or "educator"
                 user_id, 
                 age,
                 progress_level):
        
        super().__init__(first_name,
                 last_name,
                 email, 
                 password, 
                 username,
                 user_type, # type is either "student" or "educator"
                 user_id)
        self.age = age
        self.progress_level = progress_level

        #initialising a progress tracker for each student
        #self.progress_tracker = ProgressTracker(self)

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0:
            self.age = age
    
    def add_progress_level(self):
        self.progress_level += 1
    

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
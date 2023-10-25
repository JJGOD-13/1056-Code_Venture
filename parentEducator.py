'''
The definition for the ParentEducator class is below.
'''
# Import statements
from user import User
from learner import Learner

# ParentEducator class definition
class ParentEducator():
    """
    - parentEducatorName: string
    - student: Learner
    - learnerProgress: ProgressTracker

    """

    def __init__(self, User, Learner):
        """
        Constructor of ParentEducator self
        """
        self.User = User
        self.parentEducatorName = User.get_username()
        self.Learner = Learner

    def get_learner_progress(self):
        return self.learner_progress
    def get_learner(self):
        return self.learner

    def give_feedback(self):
        feedback_input = input("Please give your feedback about CodeVenture: ")
        print("Thank you very much for your feedback.")
        return feedback_input

if __name__ == "__main__":
    # Test cases
    # Create a User object
    user1 = User("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1)
    learner1 = Learner(user1, 14, 1)
    user2 = User("Kate", "Simpson", "someemail@gmail.com", "password1", "kateSi", "parent", 1)
    parent1 = ParentEducator(user2, learner1)
    feedback = parent1.give_feedback()
    

'''
The definition for the ParentEducator class is below.
'''
# Import statements
from user import User
from learner import Learner

# ParentEducator class definition
class ParentEducator(User):
    """
    - parentEducatorName: string
    - student: Learner
    - learnerProgress: ProgressTracker

    """

    def __init__(self,first_name,
                 last_name,
                 email, 
                 password, 
                 username,
                 user_type, 
                 user_id,
                 learner):
        """
        Constructor of ParentEducator self
        """
        super().__init__(first_name,
                 last_name,
                 email, 
                 password, 
                 username,
                 user_type, 
                 user_id)
        
        self.learner = learner

    def get_learner_progress(self):
        return self.learner.get_progress_report()
    
    def get_learner(self):
        return self.learner

    def give_feedback(self):
        print("Welcome the parent/guardian for "+ self.learner.first_name)
        feedback_input = input("Please give your feedback about CodeVenture: ")
        print("Thank you very much for your feedback.")
        return feedback_input

if __name__ == "__main__":
    # Test cases
    # Create a User object
   
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    
    parent1 = ParentEducator("Kate", "Simpson", "someemail@gmail.com", "password1", "kateSi", "parent", 1, learner1)

    feedback = parent1.give_feedback()
    

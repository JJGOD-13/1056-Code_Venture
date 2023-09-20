'''
The definition for the Admin class is below.
'''
# Import statements
from user import User


#Admin class definition
class Admin():
    """
    Definition for the Learner class.
    This class accepts the following arguments:
    - User: a User object
    - admin_name: a string, which will be pulled from the User object
    - admin_id: an inr
    """

    def __init__(self, User):
        self.admin_username = User.get_username()
        self.admin_id = User.get_user_id()


if __name__ == "__main__":
    pass
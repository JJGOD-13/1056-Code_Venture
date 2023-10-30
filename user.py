"""
Definition for the User class.
"""

# Import statements

# User class definition

class User():
    """
    Definition for the User class.

    This class accepts the following arguments:

    - first_name: a string
    - last_name: a string
    - email: a string
    - password: a string
    - username: a string
    - user_type: a string, either "student" or "educator"
    - user_id: an integer

    """

    def __init__(self,
                 first_name,
                 last_name,
                 email, 
                 username,
                 password,
                 user_type, # type is either "student" or "educator"
                 ):
    
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username
        self.user_type = user_type

    #accessor methods
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_email(self):
        return self.email

    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_login_status(self):
        return self.login_status
    
    def get_user_type(self):
        return self.user_type
    
    #mutator methods
    def set_username(self, username):
        self.username = username
    def set_password(self, password):
        self.password = password
    
    #verification 
    def verify_login(self, username, password):

    # Might need to change the definition of this function to get the info 
    # from a database
    #setting the login status 
        if self.username == username and self.password == password:
            self.login_status = True
        else:
            self.login_status = False

    def logOut(self):
        self.login_status = False

   
    
    # Debugging str

    def __str__(self):
        return "User: " + self.first_name + " " + self.last_name + " " + self.email + " " + self.password + " " + self.username + " " + self.user_type + " " + str(self.user_id)
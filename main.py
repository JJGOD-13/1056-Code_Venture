
from user import User
from learner import Learner
from parentEducator import ParentEducator
import sqlite3 as sql
from constructors import construct_user


#to be modified
user_database = []

# setup the db connection
db = sql.connect("codeventure.db")

#feature = signing up and login 
def main():
    """
    main function with menu
    signing up of a new user and logging in of the user

    """
    print("Welcome to CodeVenture.")
    while True:
        try:
            user_input = int(input("Choose one option: \n1. Sign up! (for new users)\n2. Log In (For existing users): \n3. Exit\n"))

            if user_input == 1:
                #create a new user object with inputs from the user
                name_first = input("Enter your first name: ")
                name_last = input("Enter your last name: ")
                while True:
                    user_email = input("Enter your email: ")
                    if "@" in user_email:
                        break
                    else: 
                        print("Please enter a valid email.")

                user_type = input("Enter your type: Student, Parent or Educator:")
                user_type = user_type.lower()
                while True:
                    if user_type == "student" or  user_type == "parent" or  user_type == "educator":
                        break
                    else:
                        print("Please enter a valid user type")
                        user_type = input("Enter your type: Student, Parent or Educator:")
                        user_type = user_type.lower()

                user_username = input("Enter a username: ")
                while True: 
                    if user_username in user_database:
                        print("This username already exists in the database, choose a new one")
                    else:
                        break
                user_password = input("Enter a password for your account: ")

                #to be modified

                default_id = 1

                new_user = User(name_first, name_last, user_email, user_password, user_username, user_type, default_id)

                #store the information for log in of user afterwords
                user_database.append(new_user)

                print("You are now part of the CodeVenture Family! Welcome!")


            elif user_input == 2:
                old_username = input("Enter your username: ")
                old_password = input("Enter your password: ")
                
                #check if user exists
                for user in user_database:
                    new_user.verify_login(old_username,old_password)

                    if new_user.get_login_status():
                        print(f"Welcome back, {new_user.get_first_name()}!")

                        if new_user.get_user_type() == "student":
                            print("Welcome to the Learner Student Menu. Choose one option to continue")
                            print("1. Start Tutorials")
                            print("2. Start Challenges")
                            print("3. View Progress Report")
                            learner_input = input("Select one option: ")

                        if new_user.get_user_type() == "parent":
                            print("Welcome to the Parent  Menu. Choose one option to continue")
                            print("1. View Progress Report of your child")
                            print("2. Provide feedback")
                            parent_input = input("Select one option: ")
                            while True:
                                if input == "1":
                                    pass
                                elif input == "2":
                                    ParentEducator.give_feedback()

                                else: 
                                    print("Please provide valid input")

                            

                        #break out of the loop once user is found in the database
                        
                

                    else:
                        print("Invalid username or password. Unable to log in. ")



            if user_input == 3:
                print("Goodbye. See you next time")
                break
            
            else: 
                print("Invalid selection for the main menu.")
        except ValueError:
            print("Invalid selection for the main menu.")

        

if __name__ == "__main__":
    main()

from user import User
from learner import Learner
from parentEducator import ParentEducator
import sqlite3 as sql


user_database = []

# setup the db connection
db = sql.connect("codeventure.db")

#feature = signing up and login 
def main():
    """main function with menu
    signing up of a new user and logging in of the user
    """
    print("Welcome to CodeVenture.")
    while True:
        user_input = int(input("Choose one option: \n1. Sign up! (for new users)\n2. Log In (For existing users): \n3. Exit\n"))

        if user_input == 1:
            #create a new user object with inputs from the user
            name_first = input("Enter your first name: ")
            name_last = input("Enter your last name: ")
            user_email = input("Enter your email: ")
            user_type = input("Enter your type: Student, Parent or Educator:")
            user_username = input("Enter a username: ")
            user_password = input("Enter a password for your account: ")

            #to be modified

            

            new_user = User(name_first, name_last, user_email, user_password, user_username,user_type)

            db.execute("INSERT INTO users (first_name, last_name, email, password, username, type) VALUES (?,?,?,?,?,?)", (name_first, name_last, user_email, user_password, user_username, user_type))
            db.commit()

            #store the information for log in of user afterwords
            user_database.append(new_user)

            print("You are now part of the CodeVenture Family! Welcome!")


        elif user_input == 2:
            old_username = input("Enter your username: ")
            old_password = input("Enter your password: ")
            
            #check if user exists
            for user in user_database:
                user.VerifyLogin(old_username,old_password)

                if user.getLoginStatus():
                    print(f"Welcome back, {user.get_first_name()}!")

                    #break out of the loop once user is found in the database
                    break
            

            else:
                print("Invalid username or password. Unable to log in. ")

            break
        elif user_input == 3:
            print("Goodbye. See you next time")
            break
        
        else: 
            print("Invalid selection for the main menu.")

if __name__ == "__main__":
    main()
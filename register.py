"""
This file contains the class that will allow the user to register for the service.

Dependencies:
tkinter
interface.py
sqlite3


"""

# Import statements

import tkinter as tk

import time
import sqlite3 as sql
from homepage import Homepage
from user import User


# Make a class for the registration page that take the root from the main file

class Register(tk.Frame):

    def __init__(self,master):

        """
        Initialize the registration page.

        INPUTS:
        self: The Register object.
        master: The tk root object.

        OUTPUTS:
        None
        """
        # Initialise the parent class
        super().__init__(master=master)
        self.master = master

        # Make a canvas to make displaying easier
        canvas = tk.Canvas(master=self, width=960, height=540)
        canvas.grid(row=0, column=0, sticky=tk.S, padx=0, pady=0)

        # Make a frame to put the widgets in
        frame = tk.Frame(master=canvas)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Make a label for the title
        title = tk.Label(master=frame, text="Register", font=("Calibri", 30))
        title.grid(row=0, column=0, columnspan=2, sticky=tk.N, padx=10, pady=10)

        # Make a label for the first name
        first_name_label = tk.Label(master=frame, text="First name:")
        first_name_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

        # Make an entry box for the first name
        self.first_name_entry = tk.Entry(master=frame)
        self.first_name_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

        # Error label for first name
        self.first_name_error_label = tk.Label(master=frame, text="First Name cannot be empty", fg="red")


        # Make a label for the last name
        last_name_label = tk.Label(master=frame, text="Last name:")
        last_name_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

        # Make an entry box for the last name
        self.last_name_entry = tk.Entry(master=frame)
        self.last_name_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a label for the username
        username_label = tk.Label(master=frame, text="Username:")
        username_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

        # Make an entry box for the username
        self.username_entry = tk.Entry(master=frame)
        self.username_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a label for the password
        password_label = tk.Label(master=frame, text="Password:")
        password_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)


        # Make an entry box for the password
        self.password_entry = tk.Entry(master=frame, show="*")
        self.password_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a label for the confirm password
        confirm_password_label = tk.Label(master=frame, text="Confirm password:")
        confirm_password_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)

        # Make an entry box for the confirm password
        self.confirm_password_entry = tk.Entry(master=frame, show="*")
        self.confirm_password_entry.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a label for the email
        email_label = tk.Label(master=frame, text="Email:")
        email_label.grid(row=6, column=0, sticky=tk.W, padx=10, pady=10)

        # Make an entry box for the email
        self.email_entry = tk.Entry(master=frame)
        self.email_entry.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a label for the type of user that this will be
        user_type_label = tk.Label(master=frame, text="User type:")
        user_type_label.grid(row=7, column=0, sticky=tk.W, padx=10, pady=10)

        # Make a drop down menu for the user type
        self.user_type = tk.StringVar()
        self.user_type.set("student")
        user_type_dropdown = tk.OptionMenu(frame, self.user_type, "student", "parent", "educator")
        user_type_dropdown.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a button to register
        register_button = tk.Button(master=frame, text="Register", command=self.register)
        register_button.grid(row=8, column=0, sticky=tk.W, padx=10, pady=10)

        self.frame = frame



    def register(self):

        
        """
        Register the user.

        INPUTS:
        self: The Register object.

        OUTPUTS:
        None
        """

        # Get the values from the entry boxes
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        email = self.email_entry.get()
        user_type = self.user_type.get()

        # Validate Data

        # Check if First Name is empty
        if first_name == "":
            self.first_name_error_label.grid(row=1, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.first_name_error_label.grid_forget()
        
        self.last_name_error_label = tk.Label(master=self.frame, text="Last Name cannot be empty", fg="red")
        if last_name == "":
            self.last_name_error_label.grid(row=2, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.last_name_error_label.grid_forget()

        # Check if the first name is only letters

        if not first_name.isalpha():
            self.first_name_error_label = tk.Label(master=self.frame, text="First Name can only contain letters", fg="red")
            self.first_name_error_label.grid(row=1, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.first_name_error_label.grid_forget()

        # Check if the last name is only letters

        if not last_name.isalpha():
            self.last_name_error_label = tk.Label(master=self.frame, text="Last Name can only contain letters", fg="red")
            self.last_name_error_label.grid(row=2, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.last_name_error_label.grid_forget()

        # Check if the username is empty

        self.username_error_label = tk.Label(master=self.frame, text="Username cannot be empty", fg="red")
        if username == "":
            self.username_error_label.grid(row=3, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.username_error_label.grid_forget()

        # Check if the password is empty

        self.password_error_label = tk.Label(master=self.frame, text="Password cannot be empty", fg="red")
        if password == "":
            self.password_error_label.grid(row=4, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.password_error_label.grid_forget()

        # Check if the confirm password is empty

        self.confirm_password_error_label = tk.Label(master=self.frame, text="Confirm Password cannot be empty", fg="red")
        if confirm_password == "":
            self.confirm_password_error_label.grid(row=5, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.confirm_password_error_label.grid_forget()

        # Check if the password and confirm password match

        self.password_error_label = tk.Label(master=self.frame, text="Passwords do not match", fg="red")
        self.confirm_password_error_label = tk.Label(master=self.frame, text="Passwords do not match", fg="red")
        if password != confirm_password:
            self.password_error_label.grid(row=4, column=2, sticky=tk.W, padx=10, pady=10)
            self.confirm_password_error_label.grid(row=5, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.password_error_label.grid_forget()
        self.confirm_password_error_label.grid_forget()

        # Check if the email is empty

        self.email_error_label = tk.Label(master=self.frame, text="Email cannot be empty", fg="red")
        if email == "":
            self.email_error_label.grid(row=6, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.email_error_label.grid_forget()

        # Check if the email is valid

        self.email_error_label = tk.Label(master=self.frame, text="Email is invalid", fg="red")
        if not email.count("@") == 1 or not email.count(".") >= 1:
            self.email_error_label.grid(row=6, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.email_error_label.grid_forget()


        # Check if the username is already taken

        db = sql.connect('codeventure.db')
        c = db.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))    
        self.result = c.fetchall()

        self.username_error_label = tk.Label(master=self.frame, text="Username is already taken", fg="red")
        if  len(self.result) != 0:
            self.username_error_label.grid(row=3, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.username_error_label.grid_forget()

        # Check if the email is already taken

        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        self.result = c.fetchall()

        self.email_error_label = tk.Label(master=self.frame, text="Email is already taken", fg="red")
        if len(self.result) != 0:
            self.email_error_label.grid(row=6, column=2, sticky=tk.W, padx=10, pady=10)
            return
        self.email_error_label.grid_forget()

        # =====================
        # Adding user to DB
        # =====================

        # Add the user to the database

        c.execute("INSERT INTO users (first_name, last_name, username, password, email, type) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, username, password, email, user_type))

        # Commit the changes to the database
        db.commit()

        # Close the connection to the database
        db.close()

        # Create a user object 

        user = User(first_name, last_name, email, password, username, user_type)

        # ======================
        # Redirect to homepage
        # ======================

        # Erase the register page
        self.place_forget()

        homepage = Homepage(self.master, user)
        homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



        

if __name__ == "__main__":

    # Make a root object
    root = tk.Tk()

    # Make a register object
    register = Register(root)
    register.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()

        

        



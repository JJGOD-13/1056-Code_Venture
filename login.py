''' 
This file is used to login to the service. 

Dependencies: 

tkinter
user.py
learner.py
educator.py

'''

# Import statements

import tkinter as tk

from user import User
from register import Register
import  sqlite3 as sql
from homepage import Homepage
import time




# Make a class for the login page that take the root from the main file

class Login(tk.Frame):

    """
    This class is used to login to the service.

    INPUTS:
    root: The root of the tkinter window.

    
    """
    

    def __init__(self, master):
         
        """
        Initialize the login page.

        INPUTS:
        self: The Login object.
        root: The tk root object.

        OUTPUTS:
        None
        """

        super().__init__(master=master)
        self.master = master

        # Make a canvas to make displaying easier
        canvas = tk.Canvas(master=self, width=960, height=540)
        canvas.grid(row=0, column=0, sticky=tk.S, padx=0, pady=0)

        # Make a frame to put the widgets in
        frame = tk.Frame(master=canvas, width=960, height=540)
        frame.pack()

        # Make a label for the username
        username_label = tk.Label(master=frame, text="Username:")
        username_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        # Make an entry for the username
        self.username_entry = tk.Entry(master=frame)
        self.username_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a label for the password
        password_label = tk.Label(master=frame, text="Password:")
        password_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

        # Make an entry for the password
        self.password_entry = tk.Entry(master=frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)

        # Make a button to login
        login_button = tk.Button(master=frame, text="Login", command=self.login)
        login_button.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

        # Make a button to register
        register_button = tk.Button(master=frame, text="Register", command=self.register)
        register_button.grid(row=2, column=1, sticky=tk.E, padx=10, pady=10)


    def register(self):
        # Erase the login page
        self.place_forget()

        # Initialize the registration page

        # Make a register object
        register = Register(self.master)
        register.place(relx=0.5, rely=0.5, anchor=tk.CENTER)








    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()
        conn = sql.connect('codeventure.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = c.fetchall()
        if len(result) == 0:
            
            
            # Make a label to display to the screen
            login_failed_label = tk.Label(master=self, text="Login failed.", fg="red")
            login_failed_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

            

        else:
            print("Login successful")
            print(result)

            # Make a label to display to the screen
            login_successful_label = tk.Label(master=self, text="Login successful.", fg="green")
            login_successful_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

            time.sleep(1)

            # Construct a User object

            user = User(result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6])

            # Erase the login page
            self.destroy()

            # Initialize the homepage
            return Homepage(self.master, user)
            
        conn.commit()
        conn.close()

    
    
# Testing

if __name__ == "__main__":
    root = tk.Tk()

    # Initialize the login page
    login_page = Login(root)

    root.mainloop()
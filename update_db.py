"""
Contains a function to update the database with the latest data from the login and register pages
"""


import sqlite3 as sql


def update_db():

    # Connect to the db
    db = sql.connect("codeventure.db")

    # Make a cursor

    c = db.cursor()

    # Make a list of all usernames from the user table where the type is "student"

    c.execute("SELECT username FROM users WHERE type = 'student'")

    user_student_usernames = c.fetchall()

    # Make a list of all usernames from the user table where the type is "parent" or "educator"

    c.execute("SELECT username FROM users WHERE type = 'parent' OR type = 'educator'")

    user_parent_educator_usernames = c.fetchall()

    # Make a list of all usernames from the students table 

    c.execute("SELECT username FROM students")

    students_usernames = c.fetchall()

    # Find all the usernames that are in the user_student_usernames list but not in the students_usernames list

    usernames_to_add = []

    for username in user_student_usernames:
        if username not in students_usernames:
            usernames_to_add.append(username)

    # Add the usernames to the students table

    # for username in usernames_to_add:
    #     c.execute("INSERT INTO students VALUES (?)", (username[0],))


    # Select all the usernames from the educators table

    c.execute("SELECT username FROM educators")
    parentteacher_usernames = c.fetchall()



    # Find all the usernames that are in the user_parent_educator_usernames list but not in the parentteacher_usernames list

    usernames_to_add = []

    for username in user_parent_educator_usernames:
        if username not in parentteacher_usernames:
            usernames_to_add.append(username)
    
    # Add the usernames to the educators table

    for username in usernames_to_add:
        c.execute("INSERT INTO educators VALUES (?)", (username[0],))

        

    
# Jayant Godse
"""
This file will contain the functions to construct the objects used in the program by pulling their data from 
db and then deconstruct to save them into the db
"""

import sqlite3 as sql
from user import User

#setup the db connection
db = sql.connect("codeventure.db")


def construct_user(username, password):
    """
    This function will construct a user object from the db
    :param username: username of the user
    :return: user object
    """
    #get the data from the db
    user_data = db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
    #create a user object
    user = User(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[0])
    return user
'''
The definintion for challenges class
'''
#import statements
import random

class Challenges():
    """
    Definition for the challenges class.
    attributes
    - challenge_title 
    - challenge_content
    """

    def __init__(self, 
                 challenge_title, 
                 challenge_content,
                 ):
        self.challenge_title = challenge_title
        self.challenge_content = challenge_content
        
    #accessor methods
    def get_challenge_title(self):
        return self.challenge_title

    def get_challenge_content(self):
        return self.challenge_content
    
    #setter methods
    def set_challenge_title(self, new_challenge_title):
        self.challenge_title = new_challenge_title

    def set_challenge_content(self, new_challenge_content):
        self.challenge_content = new_challenge_content
    
    #function for displaying motivational messages
    def disp_motivational_message(self):
        messages_list = ["Keep up the good work!", "You can do it!", "Keep going!"]
        message = random.choice(messages_list)
        print(message)


if __name__ == "__main__":
    challenge1 = Challenges("New Challenge", "Random content")
    challenge1.disp_motivational_message()
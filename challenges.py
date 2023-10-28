'''
The definintion for challenges class
'''
#import statements
import random
import tkinter as tk

class Challenges(tk.Frame):
    """
    Definition for the challenges class.
    attributes
    - challenge_title 
    - challenge_content
    """

    def __init__(self, 
                 master,
                 learner_page
                 ):
        # self.challenge_title = challenge_title
        # self.challenge_content = challenge_content

        # Initialise the parent class
        super().__init__(master=master)
        self.master = master
        self.learner_page = learner_page

        #welcome message label
        welcome_label = tk.Label(self,text = "Welcome to Challenges!", font=("Arial",18) )
        welcome_label.grid(row=0, columnspan=3, padx=10, pady=10)

        #welcome message 2 label
        welcome_label2 = tk.Label(self,text = "Practice! Practice! Practice!", font=("Arial",12) )
        welcome_label2.grid(row=1, columnspan=3, padx=10, pady=10)

        #current question index
        self.current_question_index = 0

        #All questions and answers stored as dictionary in a list
        self.all_challenge_content =[
            {"ques": "What will be the value of (5**2 + 3*2)", "ans":"31"},
            {"ques": "What will be the value of (4//2)", "ans":"2"},
            {"ques": "What will be the value of (4/2)", "ans":"2.0"}
            ]
        
        #Label for ques display
        self.ques = tk.Label(self, text="")
        self.ques.grid(row=2,column=1,padx=10,pady=10)

        #Entry field for answers
        self.user_ans = tk.StringVar()
        self.ans = tk.Entry(self, textvariable=self.user_ans)
        self.ans.grid(row=3, column=1, padx=10, pady=10)

        #Button to submit answer
        self.submit = tk.Button(self, text="Submit",command=self.verify_ans)
        self.submit.grid(row=4, column=1, padx=10, pady=10)

        #Label to display result 
        self.result = tk.Label(self, text="")
        self.result.grid(row=5, column=1, padx=10, pady=10)

        #button for next ques
        ques_next = tk.Button(self, text = "Next", command=self.ques_next) 
        ques_next.grid(row=6, column=2, padx=10, pady=10)
        
        #button for previous ques
        ques_prev = tk.Button(self, text = "Previous", command=self.ques_prev) 
        ques_prev.grid(row=6, column=0, padx=10, pady=10)

        #button to go back to the student page
        go_to_student_page = tk.Button(self, text = "Go Back",command=self.go_back_to_learner) 
        go_to_student_page.grid(row=7, columnspan=3, padx=10, pady=10)
        
        #start with the first question
        self.display_ques()

    #method to go back to the learner(student) page
    def go_back_to_learner(self):
        """
        Event handler to go back to the student page
        """
        self.place_forget()
        self.learner_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def display_ques(self):
        """
        Method to display the question
        """
        if self.current_question_index < len(self.all_challenge_content):
            #display the ques
            self.ques.config(text=self.all_challenge_content[self.current_question_index]["ques"])

            
        else:
            self.ques.config(text= "Woah! You completed all the questions.")

        #clear the entry for previous question's answer
        self.ans.delete(0, tk.END)

        #reset the result label 
        self.result.config(text="")

    def verify_ans(self):
        """
        Method to check if the answer provided by the user is correct
        """
        try:
            answer_user = self.ans.get()
            right_answer = self.all_challenge_content[self.current_question_index]["ans"]
            if answer_user == right_answer:
                self.result.config(text="Well done! Correct Answer",fg="green")
            elif answer_user == "":
                self.result.config(text="Please enter an answer to check", fg="red")
            else:
                self.result.config(text="Oops! Try again", fg="red")
        except IndexError:
            self.result.config(text="Error. You have completed all questions", fg="blue")

    def ques_next(self):
        if self.current_question_index < len(self.all_challenge_content):
            self.current_question_index += 1
            self.display_ques()
            # if self.tutorial_index < len(self.basic_tutorials):
            #     self.disp_motivational_message()

    def ques_prev(self):
        if 0 < self.current_question_index:
            self.current_question_index -= 1
            self.display_ques()

    



    #function for displaying motivational messages
    def disp_motivational_message(self):
        messages_list = ["Keep up the good work!", "You can do it!", "Keep going!"]
        message = random.choice(messages_list)
        print(message)


        
    # #accessor methods
    # def get_challenge_title(self):
    #     return self.challenge_title

    # def get_challenge_content(self):
    #     return self.challenge_content
    
    # #setter methods
    # def set_challenge_title(self, new_challenge_title):
    #     self.challenge_title = new_challenge_title

    # def set_challenge_content(self, new_challenge_content):
    #     self.challenge_content = new_challenge_content
    
   

if __name__ == "__main__":
    challenge1 = Challenges("New Challenge", "Random content")
    challenge1.disp_motivational_message()
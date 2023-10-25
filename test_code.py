import pytest

from user import User
from learner import Learner
from parentEducator import ParentEducator
from progressTracker import ProgressTracker
from tutorial import Tutorials
from challenges import Challenges

#positive testing

def test_user_object_creation():
    sample_user = User("Tom", "Jackson","something@example.com","password","tjack", "student",1 )
    assert sample_user.first_name == "Tom"
    assert sample_user.last_name == "Jackson"
    assert sample_user.email == "something@example.com"
    assert sample_user.password == "password"
    assert sample_user.username == "tjack"
    assert sample_user.user_type == "student"
    assert sample_user.user_id == 1

def test_progress_tracker_object_creation():
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    pg = ProgressTracker(learner1,10, 2, 5)
    
    assert pg.total_scores == 10
    assert pg.total_tutorial_completed == 2
    assert pg.total_challenges_completed == 5

def test_tutorial_object_creation():
    tutorial1 = Tutorials("New Tutorial", "Random content")

    assert tutorial1.tutorial_title == "New Tutorial"
    assert tutorial1.tutorial_content == "Random content"

def test_challenge_object_creation():
    challenge1 = Challenges("New Challenge", "Random content 2")

    assert challenge1.challenge_title == "New Challenge"
    assert challenge1.challenge_content == "Random content 2"

def test_tutorial_setters():
    tutorial1 = Tutorials("New Tutorial", "Random content")
    tutorial1.set_tutorial_title("This is the Latest Tutorial Title")
    tutorial1.set_tutorial_content("This is the Latest Tutorial Content")

    assert tutorial1.tutorial_title == "This is the Latest Tutorial Title"
    assert tutorial1.tutorial_content == "This is the Latest Tutorial Content"

def test_challenge_setters():
    challenge1 = Challenges("New Challenge", "Random content 2")
    challenge1.set_challenge_title("This is the Latest Challenge Title")
    challenge1.set_challenge_content("This is the Latest Challenge Content")

    assert challenge1.challenge_title == "This is the Latest Challenge Title"
    assert challenge1.challenge_content == "This is the Latest Challenge Content"

def test_verify_login_true():
    """
    Test for the verify_login function by providing correct details
    """
    #create a sample user
    sample_user = User("Tom", "Jackson","something@example.com","password","tjack", "student",1 )
    sample_user.verify_login("tjack","password")

    sample_user2 = User("Tom", "Jackson","something@example.com","password","tjack", "student",1 )
    sample_user2.verify_login("tjack","wrongPassword")
    
     
    assert sample_user.get_login_status() == True

def test_log_out():
    sample_user = User("Tom", "Jackson","something@example.com","password","tjack", "student",1 )
    sample_user.log_out()
    
    assert sample_user.get_login_status() == False

def test_add_progress_level_learner():
    sample_learner = Learner("Tom", "Jackson","something@example.com","password","tjack", "student",1, 12, 1 )
    sample_learner.add_progress_level()
    
    assert  sample_learner.progress_level == 2

def test_set_score_progress_level_positive():
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    pg = ProgressTracker(learner1,10, 2, 1)
    pg.set_score(5)

    assert pg.total_scores == 15
    
def test_set_score_tutorial():
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    pg = ProgressTracker(learner1,10, 2, 1)
    pg.set_tutorial()

    assert pg.total_tutorial_completed == 3

def test_set_score_challenges():
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    pg = ProgressTracker(learner1,10, 2, 5)
    pg.set_challenge()

    assert pg.total_challenges_completed == 6

def test_positive_age_learner():
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    learner1.set_age(15)
    assert learner1.age == 15

def test_parent_educator_feedback(monkeypatch):
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    parent1 = ParentEducator("Kate", "Simpson", "someemail@gmail.com", "password1", "kateSi", "parent", 1, learner1)

    #using builtins input to mock user input
    monkeypatch.setattr('builtins.input', lambda _:"This is awesome!")
    feedback = parent1.give_feedback()

    assert feedback == "This is awesome!"

def test_challenge_print_output(capsys):
    challenge1 = Challenges("New Challenge", "Random content 2")
    challenge1.disp_motivational_message()
    #using capsys to check the printed output
    print_output = capsys.readouterr()
    final_output = print_output.out
    messages_list = ["Keep up the good work!\n", "You can do it!\n", "Keep going!\n"]
    assert final_output in messages_list


#negative testing
def test_verify_login_false():
    """
    Test for the verify_login function by providing wrong password
    """
    #create a sample user
    sample_user2 = User("Tom", "Jackson","something@example.com","password","tjack", "student",1 )
    sample_user2.verify_login("tjack","wrongPassword")
    
    assert sample_user2.get_login_status() == False

def test_set_score_progress_level_negative():
    """
    If negative test score is tried to be set, it will not be updated in the total scores section
    """
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    pg = ProgressTracker(learner1,10, 2, 1)
    pg.set_score(-5)

    assert pg.total_scores == 10

def test_negative_age_learner():
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    learner1.set_age(-15)
    assert learner1.age == 14

def test_parent_educator_feedback_empty(monkeypatch):
    """
    Testing the give_feedback() function for empty input provided by the user
    """
    learner1 = Learner("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1, 14, 1)
    parent1 = ParentEducator("Kate", "Simpson", "someemail@gmail.com", "password1", "kateSi", "parent", 1, learner1)

    #using builtins input to mock user input
    monkeypatch.setattr('builtins.input', lambda _:"")
    feedback = parent1.give_feedback()

    assert feedback == ""






# Name: Issa Mohamed
# Date: 9/29/21
# Class: CS 111
import random
from history import History

rubric = {("c","c","c"):( 3, 3, 3),
          ("d","c","c"):( 5, 0, 0),
          ("c","d","c"):( 0, 5, 0),
          ("c","c","d"):( 0, 0, 5),
          ("c","d","d"):(-5, 2, 2),
          ("d","c","d"):( 2,-5, 2),
          ("d","d","c"):( 2, 2,-5),
          ("d","d","d"):(-2,-2,-2)}

# Plays a three-player prisoner's dilemma game
# strat0, strat1 and strat2 are functions that return either "c" or "d"
# count is the number of plays
def play_loop(strat0, strat1, strat2, count=100):
    history0 = History()
    history1 = History()
    history2 = History()
    for i in range(count):
        action0 = strat0(history0, history1, history2)
        action1 = strat1(history1, history0, history2)
        action2 = strat2(history2, history0, history1)
        history0.add_action(action0)
        history1.add_action(action1)
        history2.add_action(action2)

    print_results(strat0, strat1, strat2, history0, history1, history2)
    return history0, history1, history2

# This fuction prints the average scores for a three-player prisoner's 
# dilemma game
def print_results(strat0, strat1, strat2, history0, history1, history2):
    assert history0.get_length() == history1.get_length() == history2.get_length(), "Histories have unequal length"
    score0 = score1 = score2 = 0
    for actions in zip(history0, history1, history2):
        score0 += rubric[actions][0]
        score1 += rubric[actions][1]
        score2 += rubric[actions][2]
    print("{} average score: {:.3f}".format(strat0.__name__, score0 / history0.get_length()))
    print("{} average score: {:.3f}".format(strat1.__name__, score1 / history1.get_length()))
    print("{} average score: {:.3f}".format(strat2.__name__, score2 / history2.get_length()))

# DEFINE STRATEGIES HERE
def betrayer3(my_history, other_history1, other_history2):
    return "d"
def friend3(my_history,other_history1, other_history2):
    return "c"
def chaos3(my_history,other_history1,other_history2):
    chaos_options = ["c", "d"] 
    random_option = random.randint(0, 1)
    return chaos_options[random_option]
def tough_mimic(my_history,other_history1,other_history2 ):
     other_user_last_play1 = other_history1.get_most_recent
     other_user_last_play2 = other_history2.get_most_recent
     if(other_user_last_play1 == "d" or other_user_last_play2 == "d"):
         return "d"
     else: 
         return "c"
def soft_mimic(my_history,other_history1,other_history2 ):
     other_user_last_play1 = other_history1.get_most_recent
     other_user_last_play2 = other_history2.get_most_recent
     if(other_user_last_play1 == "d" and other_user_last_play2 == "d"):
         return "d"
     else: 
         return "c"
         
        



# SELECT STRATEGIES HERE
strategy1 = soft_mimic
strategy2 = chaos3
strategy3 = chaos3
log = False

# no need to modify this code
if __name__ == "__main__":
    h1, h2, h3 = play_loop(strategy1, strategy2, strategy3)
    if log:
        s1_name = strategy1.__name__
        s2_name = strategy2.__name__
        s3_name = strategy3.__name__
        print("\nFULL GAME LOG\n")
        print(f"round #   \t{s1_name:>11}'s action\t{s2_name:>11}'s action\t{s3_name:>11}'s action")
        print("-"*85)
        for i, (a1, a2, a3) in enumerate(zip(h1, h2, h3)):
            print(f"{'round ' + str(i):10}\t{a1:>20}\t{a2:>20}\t{a3:>20}")
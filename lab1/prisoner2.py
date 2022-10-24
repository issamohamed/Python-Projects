# Name: Issa Mohamed
# Date: 9/29/21
# Class: CS 111
import random 
from history import History

rubric = {("c","c"):( 2, 2),
          ("c","d"):(-3, 5),
          ("d","c"):( 5,-3),
          ("d","d"):(-1,-1)}

# Plays a two-player prisoner's dilemma game
# strat0 and strat1 are functions that return either "c" or "d"
# count is the number of plays
def play_loop(strat0, strat1, count=100):
    history0 = History()
    history1 = History()
    for _ in range(count):
        action0 = strat0(history0, history1)
        action1 = strat1(history1, history0)
        history0.add_action(action0)
        history1.add_action(action1)

    print_results(strat0, strat1, history0, history1)
    return history0, history1

# This fuction prints the average scores for a two-player prisoner's
# dilemma game
def print_results(strat0, strat1, history0, history1):
    assert history0.get_length() == history1.get_length(), "Histories have unequal length"
    score0 = score1 = 0
    for actions in zip(history0, history1):
        score0 += rubric[actions][0]
        score1 += rubric[actions][1]
    print("{} average score: {:.3f}".format(strat0.__name__, score0 / history0.get_length()))
    print("{} average score: {:.3f}".format(strat1.__name__, score1 / history1.get_length()))


# DEFINE STRATEGIES HERE
def betrayer(my_history, other_history):
    return "d"
def friend(my_history,other_history):
    return "c"
def chaos(my_history,other_history):
    chaos_options = ["c", "d"] 
    random_option = random.randint(0, 1)
    return chaos_options[random_option]
def mimic(my_history,other_history):
    # solving for first round
    current_round_checker = my_history.get_length()
    if (current_round_checker == 0):
        return "c" 
    else:
        # solving for subsequent rounds   
        other_user_last_play = other_history.get_most_recent()
        return other_user_last_play


def judge(my_history, other_history):
    # solving for the first round
    current_round_checker = my_history.get_length()
    if (current_round_checker == 0):
        return "c" 
    else: 
        # solving for subsequent rounds
        other_player_total_defect = other_history.get_num_defects()
        other_player_total_coop = other_history.get_num_coops()
        # If the other player’s defections outnumber their cooperations, judge will defect
        if (other_player_total_defect > other_player_total_coop):
            return "d"
        else:
            return "c"

def careful_mimic(my_history, other_history):
    # solve the number of rounds to see if less than 2 rounds have been played 
    current_round_checker = my_history.get_length()
    if (current_round_checker < 2):
        return "c" 
    else: 
    # solving for subsequent rounds
        if (other_history.has_recent_defect(1) and other_history.has_recent_defect(2)):
            return "d"
        else:
            return "c"

# Challenge Problem 4:
def alternating(my_history,other_history):
    current_round_checker = my_history.get_length()   
    if(current_round_checker == 0):
        return mimic(my_history,other_history)
    elif( (current_round_checker % 2) == 0):
        return mimic(my_history,other_history)
    else:
        return judge(my_history,other_history)



# SELECT STRATEGIES HERE
strategy1 = alternating
strategy2 = betrayer
log = False

# no need to modify this code
if __name__ == "__main__":
    h1, h2 = play_loop(strategy1, strategy2)
    if log:
        s1_name = strategy1.__name__
        s2_name = strategy2.__name__
        print("\nFULL GAME LOG\n")
        print(f"round #   \t{s1_name:>11}'s action\t{s2_name:>11}'s action")
        print("-"*65)
        for i, (a1, a2) in enumerate(zip(h1, h2)):
            print(f"{'round ' + str(i):10}\t{a1:>20}\t{a2:>20}")
   
# Name: Issa Mohamed, Marco Caba-Acevedo
# Date: 10/14/21
# Class: CS 111
# Prof: Aaron Bauer
# Purpose: To determine signs of gerrymandering with given values of data

# Conclusion: Based on our code's analysis, out of all 3 states taken into consideration,
# the primary suspects of gerrymandering to their own blatant advantage were Maryland and Wisconsin.
# Starting with Maryland, a state consisiting of only 8 seats as of the 2020 census, we see that distrubuition of the seats are 
# in favor of the Democrats as they hold 87.5% of the seats with 65.04% of the votes whilst the Republicans only holds a mere
# 12.5% of the seats with 34.96% of the votes making the difference between the two a gaping 7:1 ratio in terms of district distribuition. 
# Wisconsin is also a solid suspect of gerrymandering seeing that it too has 8 seats like Maryland yet the Republicans hold 62.5% of the seats 
# with with 51.47% of the vote whilst the Democrats hold a petty 37.5% of seats with 48.53% of the vote making it a whopping ratio of 5:3. 

# The seat number was mainly taken into consideration as the high percentages by themselves, could be misleading if one state were to have perhaps, 4 seats
# which would make alot more sense given the lack of seats the percents are being divided by. Maryland/ Wisconsin's analysis also widley contrast the least suspecting 
# of gerrymandering of the 3 in the group: Michigan, which has 14 seats as of the 2020 census yet maintains a 50.0 50.0 percentage of even disturbuiton of seats for both the Democrats 
# and the Republicans. There are more outrageous examples of gerrymandering. For example we must take a look at the state of Arkansas.
# Holding 4 seats, Arkansas Democrats should get at least 1 seat with their 28.52% of the vote. However, Arkansas Republicans hold all 4 or 100%
# of seats.




# Using accessor functions to access fields
def get_year(line):
    return(int(line[0]))

def get_state(line):
    return(line[1])

def get_state_po(line):
    return (line[2])

def get_state_fips(line): 
    return (int(line[3]))

def get_state_cen(line):
    return (int(line[4]))

def get_state_ic(line):
    return (int(line[5]))

def get_office(line):
    return (line[6])

def get_district(line):
    return (int(line[7]))

def get_stage(line):
    return (line[8])

def get_runoff(line):
    return (line[9])

def get_special(line):
    return (line[10])

def get_candidate(line):
    return (line[11])

def get_party(line):
    return (line[12])

def get_writein(line):
    return (line[13])

def get_mode(line):
    return (line[14])

def get_canidates_votes(line):
    return (int(line[15]))

def get_totalvotes(line):
    return (int(line[16]))

def get_unofficial(line):
    return (line[17])

def get_version(line):
    return (int(line[18]))

def get_fusion_ticket(line):
    return (line[19])

def get_election(line):
    state = get_state(line)
    district = get_district(line)
    district = str(district)
    election = state + district 
    return election 


# Opening/Closing the cvs file and storing the contents of the cvs in a list 
data_file = open("district_overall_2020.csv")
data_lines = data_file.readlines()
data_file.close()
# Removing column names from the data
data_lines.pop(0)

# Splitting the list 
for index in range(len(data_lines)):
    data_lines[index] = data_lines[index].split(",")
# List of States
states = []
for line in data_lines:
    current_state = get_state(line)
    if ((current_state in states) == False):
        states.append(current_state)
# List of Elections
elections = []
for line in data_lines:
    current_election = get_election(line)
    if ((current_election in elections) == False):
        elections.append(current_election)
        # Intially opening the output file
output_file = open("gerrymandering-report.txt", "w")
# Calculating the values of each state
for state in states:
# Intializing DEM and GOP votes for each state
    gop_votes = 0
    gop_seats = 0
    dem_votes = 0
    dem_seats = 0
    for election in elections:
        if (election.startswith( state )):
            vote_party_tuples = []
            for line in data_lines:
                if (election == get_election(line)):
                    party = get_party(line)
                    votes = get_canidates_votes(line)
                    # Updating vote count for the tuple's party
                    if ( party == 'REPUBLICAN'):
                        gop_votes = gop_votes + votes
                    elif (party == 'DEMOCRAT'):
                        dem_votes = dem_votes + votes
                    # Generating tuple to add to list
                    vote_party_tuple = (votes, party)
                    vote_party_tuples.append(vote_party_tuple)
            # Determing winning party and updating their seat count 
            vote_party_tuples.sort()
            winning_party = vote_party_tuples[-1]
            if (winning_party[1] == 'REPUBLICAN'):
                gop_seats = gop_seats + 1
            elif (winning_party[1] == 'DEMOCRAT'):
                dem_seats = dem_seats + 1
    # Defining Percentages
    two_party_vote_total = dem_votes + gop_votes
    two_party_seat_total = dem_seats + gop_seats
    dem_two_party_vote_percentage = round( ((dem_votes / two_party_vote_total) * 100), 2)
    dem_two_party_seat_percentage = round( ((dem_seats / two_party_seat_total) * 100 ), 2)
    gop_two_party_vote_percentage = round( ((gop_votes / two_party_vote_total) * 100), 2)
    gop_two_party_seat_percentage = round( ((gop_seats / two_party_seat_total) * 100), 2)

    # Printing out summary stats and writing them to the output file
    print(state)
    print("Republican:", gop_two_party_vote_percentage, "% of the vote,", gop_two_party_seat_percentage,"% of the seats",'\n')
    print("Democrat:", dem_two_party_vote_percentage, "% of the vote,", dem_two_party_seat_percentage, "% of the seats", '\n')
    # Output File's actual content
    output_file.write(state + '\n')
    output_file.write("Republican:" + str(gop_two_party_vote_percentage) + "% of the vote," + str(gop_two_party_seat_percentage) + "% of the seats" + '\n')
    output_file.write("Democrat:" + str(dem_two_party_vote_percentage) + "% of the vote," + str(dem_two_party_seat_percentage) + "% of the seats" + '\n')
    output_file.write("\n")
    #closing the output file
output_file.close()
import random
from collections import Counter

'''
http://farkle.games/official-rules/
How to NOT Farkle:
a singe dice showing a 1 or a 5,
three of a kind, such as, 2 2 2
three pairs, 2 2, 4 4, 6 6 for example
a six-dice straight, 1 2 3 4 5 6 

4 of a Kind – Take the score of three of a kind and multiply it by 2.
5 of a Kind – Take the score of three of a kind and multiply it by 3.
6 of a Kind – Take the score of three of a kind and multiply it by 4.
'''

kept_die_dict = {}
i=0
default_roll = 6
FARKLE = True

def farkle(number_of_die):
    #i will need a binary flag for each point check to add up points
    one_or_five_flag = False
    three_of_a_kind_flag = False
    straight_flag = False
    three_pairs_flag = False
    four_pairs_flag = False
    five_pairs_flag = False
    six_pairs_flag = False
    farkle_flag = False
    multi_ones = False
    multi_fives = False
    two_triplets = False
    #I run the tests below then append all flags to this list and check if there is at least one pass
    flags = []
    rolls_dict = {}
    points = 0
    for roll in range(number_of_die):
        rolls_dict[roll] = random.randint(1, 6)
        print(f'Die {roll +1}: ' + str(rolls_dict[roll]))

    #sorts values of rolls_dict
    sorted_rolls = sorted(rolls_dict.values())
    #checks number of times rolled for each value
    roll_counter_list = dict(Counter(sorted_rolls))
    print(roll_counter_list)
    roll_counter_values = list(roll_counter_list.values())
    #check to see if theres a 1 or a 5
    if 1 in rolls_dict.values():
        # points += 100
        one_or_five_flag = True
    if 5 in rolls_dict.values():
        # points += 50
        one_or_five_flag = True
    #this is a straight
    elif sorted_rolls == [1,2,3,4,5,6]:
        straight_flag = True
    #check for 3 sets of doubles
    elif roll_counter_values == [2,2,2]:
        three_pairs_flag = True
    #check for 2 sets of triples
    elif roll_counter_values == [3,3]:
        two_triplets = True
    #checks for 3 of a kind
    for number_rolled in roll_counter_list:
        times_rolled = roll_counter_list[number_rolled]
        if times_rolled == 3:
            # points += 100 * number_rolled
            three_of_a_kind_flag = True
            #if there are multiple 1s or 5s then this is the point system, not the standard way
            if number_rolled == 1:
                multi_ones  = True
            if number_rolled == 5:
                multi_fives  = True

        if times_rolled == 4:
            # points += 100 * number_rolled * 2
            four_of_a_kind_flag = True
            #if there are multiple 1s or 5s then this is the point system, not the standard way
            if number_rolled == 1:
                multi_ones  = True
            if number_rolled == 5:
                multi_fives  = True

        if times_rolled == 5:
            # points += 100 * number_rolled * 3
            five_of_a_kind_flag = True
            #if there are multiple 1s or 5s then this is the point system, not the standard way
            if number_rolled == 1:
                multi_ones  = True
            if number_rolled == 5:
                multi_fives  = True

        if times_rolled == 6:
            # points += 100 * number_rolled * 4
            six_of_a_kind_flag = True
            #if there are multiple 1s or 5s then this is the point system, not the standard way
            if number_rolled == 1:
                multi_ones  = True
            if number_rolled == 5:
                multi_fives  = True


    #if you dont pass any of the tests above, you failed and you Farkled
    flags.append(one_or_five_flag)
    flags.append(three_of_a_kind_flag)
    flags.append(straight_flag)
    flags.append(three_pairs_flag)
    flags.append(four_pairs_flag)
    flags.append(five_pairs_flag)
    flags.append(six_pairs_flag)
    flags.append(multi_ones)
    flags.append(multi_fives)
    if True not in flags:
        farkle_flag = True
        print('Farkle!!!')
    return farkle_flag,rolls_dict

def keep_die(rolled_dict,rolls_this_turn):
    kept_die_list = []
    print(rolled_dict)
    #get input of kept dice
    keep_die = list(input("Which die would you like to keep?:\n "))
    while(" " in keep_die or "," in keep_die):
        try:
            keep_die.remove(" ")
        except:
             keep_die.remove(",")
    #make a list of kept dice
    keep_die = list(map(int, keep_die))
    for die in keep_die:
        kept_die_list.append(rolled_dict.pop(die-1))
    kept_die_dict[rolls_this_turn] = kept_die_list
    test = list(set([1,2,3,4,5,6]) - set(keep_die))
    print('test: ', kept_die_dict)
    #make sure we keep points

def point_tracker(kept_die_list, turn):
    pass




#add valdiation step to ensure input matches the rolls
#kept dice are numbers from 1-6 and in correct format
#kept dice are actually points

#this is my main loop
while FARKLE and (i == 0 or i == 1):
    #keep track of number of rolls
    rolls_this_turn = 1
    #first determine if FARKLED
    FARKLE, rolled_dict = farkle(default_roll)
    #second determine which die to keep
    kept_list = keep_die(rolled_dict,rolls_this_turn)
    #third determine points
    point_tracker(kept_list,rolls_this_turn)
    i+=1
    rolls_this_turn += 1

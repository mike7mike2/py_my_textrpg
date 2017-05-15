import random

def end():
    print('game over')
    import sys
    input('Press any key to continue . . . ')
    sys.exit()

# define range stats
range_hp = 6
range_def = 6
range_att = 12
range_stats = {'hp':range_hp,'def':range_def,'att':range_att}

# define mage stats
mage_hp = 3
mage_def = 3
mage_att = 21
mage_stats = {'hp':mage_hp,'def':mage_def,'att':mage_att}

# define melee stats 
melee_hp = 12
melee_def = 12
melee_att = 6
melee_stats = {'hp':melee_hp,'def':melee_def,'att':melee_att}

# ask player for class choice
player_class = input('choose your class range, mage, or melee  ')

# print player's class's stats
if player_class == "range":
    print(range_stats)
    player_stats = range_stats
elif player_class == 'mage':
    print(mage_stats)
    player_stats = mage_stats
elif player_class == 'melee':
    print(melee_stats)
    player_stats = melee_stats
else:
    end()

# ==============================================================================
# the first path
# ==============================================================================
# go to fork in the road prompt user for directions
path1 = input('you stop at a fork in the road, where do you go, right or left?  ')

# right path
if path1 == 'right':
    path1r = input('there is a cave, do you skip it or go in?  ')
    if path1r == 'go in':
        fight1 = input('in the cave you find a monster do you want to fight it or run away?  ')
    elif path1r == 'skip it':
            print('game over you are a coward')

if fight1 == 'run away':
    print('you manage to escape, youre back on the path')
elif fight1 == 'fight it':
    print("game over, you die")

# left path

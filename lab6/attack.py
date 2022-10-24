# Critter World
# Aaron Bauer, 2019

# Constants for attack
ROAR = 28
POUNCE = -10
SCRATCH = 55

def attack_to_str(attack):
    return {28: "ROAR", 
    -10: "POUNCE", 
    55: "SCRATCH"}[attack]
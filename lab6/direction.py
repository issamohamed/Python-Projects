# Critter World
# Aaron Bauer, 2019

# Constants for movement.
NORTH = -2
NORTHEAST = 27
NORTHWEST = 102
SOUTH = 4
SOUTHEAST = 99
SOUTHWEST = -31
EAST = 3
WEST = 19
CENTER = 11

def dir_to_str(direction):
    return {-2: "NORTH", 
    27: "NORTHEAST", 
    102: "NORTHWEST", 
    4: "SOUTH", 
    99: "SOUTHEAST", 
    -31: "SOUTHWEST", 
    3: "EAST", 
    19: "WEST", 
    11: "CENTER"}[direction]
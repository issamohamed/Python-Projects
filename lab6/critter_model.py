# Critter World
# Adam Eck, 2018

import critter_main
import collections
import color, attack, direction
import inspect
import random
import os
import pprint

# Just an (x, y) pair, but more readable.
Point = collections.namedtuple('Point', ['x', 'y'])

# Again, we don't really need a whole class just to store this info.
CritterInfo = collections.namedtuple('CritterInfo', ['x', 'y', 'width', 'height', 'char', 'color', 'getNeighbor'])

class CritterModel():
    """
    The main Critter simulation. Takes care of all the logic of
    Critter fights.
    """

    def __init__(self, width, height, list_lock, config):
        self.width = width
        self.height = height
        self.critters = []
        self.turn_count = 0
        # A map of critters to (x, y) positions.
        self.critter_positions = {}
        # A map of critter classes to the number alive of that class.
        self.critter_class_states = {}
        self.grid = [[None for x in range(height)] for y in range(width)]
        # Make sure nothing bad happens due to concurrent list access.
        self.list_lock = list_lock
        self.config = config
        self.verbose = config["verbose"] if "verbose" in config else False

    def add(self, critter, num):
        """
        Adds a particular critter type num times. The critter should
        be a class, not an instantiated critter.
        """
        if critter not in self.critter_class_states:
            self.critter_class_states[critter] = ClassInfo(initial_count=num)
        self.critter_class_states[critter].alive += num
        for i in range(num):
            args = CritterModel.create_parameters(critter)
            c = critter(*args)
            self.critters.append(c)
            pos = self.random_location()
            self.critter_positions[c] = pos
            self.grid[pos.x][pos.y] = c
            if self.verbose:
                print("critter_model.add: created a {} at position {} with parameters {}".format(critter.__name__, pos, args))

    def reset(self):
        '''
        Resets the model, clearing out the whole board and
        repopulating it with num_critters of the same Critter types.
        '''
        self.grid = [[None for x in range(self.height)] for y in range(self.width)]
        self.critter_positions = {}
        self.critters = []
        self.turn_count = 0
        new_states = {}
        for critter_class in self.critter_class_states.keys():
            num_critters = self.config["critter_pops"][critter_class.__name__]
            new_states[critter_class] = ClassInfo(initial_count=num_critters)
            new_states[critter_class].alive += num_critters
            for i in range(num_critters):
                args = CritterModel.create_parameters(critter_class)
                c = critter_class(*args)
                self.critters.append(c)
                pos = self.random_location()
                self.critter_positions[c] = pos
                self.grid[pos.x][pos.y] = c
                if self.verbose:
                    print("critter_model.add: created a {} at position {} with parameters {}".format(critter.__name__, pos, args))
        self.critter_class_states = new_states

    def update(self):
        """
        Takes care of updating all Critters. For each Critter, it
        firsts moves. If the position it moves to is occupied, the two
        critters fight, and the loser is destroyed while the winner
        moves into the position.
        """
        self.turn_count += 1
        if self.verbose:
            print("\n{}\ncritter_model.update: UPDATE turn {}\n{}".format("="*70, self.turn_count, "="*70))
        random.shuffle(self.critters)
        # Unclean while loop, because we'll be removing any losing critters
        # as we iterate through the list.
        i = 0
        l = len(self.critters)
        while i < l:
            critter1 = self.critters[i]
            if self.verbose:
                print("\ncritter_mode.update: updating {} (unique id={})".format(critter1.__class__.__name__, id(critter1)))
            # Move the critter
            old_position = self.critter_positions[critter1]
            move = critter1.getMove(CritterInfo(old_position.x, old_position.y,
                                                     self.width, self.height,
                                                     critter1.getChar(),
                                                     critter1.getColor(),
                                                     self.get_neighbor_func(old_position)))
            CritterModel.verify_move(move)
            position = self.move(move, old_position)
            if self.verbose:
                print("critter_mode.update: moving from {} to {}".format(old_position, position))
            # Fight, if necessary
            winner = critter1
            critter2 = self.grid[position.x][position.y]
            if critter2 and position != old_position and critter1 != critter2: # Save each stone from fighting itself
                if self.verbose:
                    print("critter_mode.update: encountered {} (unique id={})".format(critter2.__class__.__name__, id(critter2)))
                winner = self.fight(critter1, critter2)
                if self.verbose:
                    print("critter_mode.update: {} (unique id={}) won".format(winner.__class__.__name__, id(winner)))
                loser = critter1 if winner == critter2 else critter2
                self.critter_positions[winner] = position
                # Get the loser out of here
                with self.list_lock:
                    index = self.critters.index(loser)
                    if index <= i:
                        i -= 1
                    self.critter_positions.pop(loser)
                    self.critters.remove(loser)
                    l -= 1
                    # Make sure we've got an accurate kill/alive count
                    self.critter_class_states[loser.__class__].alive -= 1
                    self.critter_class_states[winner.__class__].kills += 1
            # Update positions
            self.grid[old_position.x][old_position.y] = None
            self.grid[position.x][position.y] = winner
            self.critter_positions[winner] = position
            i += 1

    def move(self, move, pos):
        """
        Returns the new position after moving in direction. This
        assumes that (0, 0) is the top-left.
        """
        if move == direction.NORTH:
            return Point(pos.x, (pos.y - 1) % self.height)
        elif move == direction.SOUTH:
            return Point(pos.x, (pos.y + 1) % self.height)
        elif move == direction.EAST:
            return Point((pos.x + 1) % self.width, pos.y)
        elif move == direction.WEST:
            return Point((pos.x - 1) % self.width, pos.y)
        elif move == direction.NORTHEAST:
            return Point((pos.x + 1) % self.width, (pos.y - 1) % self.height)
        elif move == direction.NORTHWEST:
            return Point((pos.x - 1) % self.width, (pos.y - 1) % self.height)
        elif move == direction.SOUTHWEST:
            return Point((pos.x + 1) % self.width, (pos.y + 1) % self.height)
        elif move == direction.SOUTHEAST:
            return Point((pos.x - 1) % self.width, (pos.y + 1) % self.height)
        else:
            return pos

    def fight(self, critter1, critter2):
        """
        Force poor innocent Critters to fight to the death for the
        entertainment of Carleton students. Returns the glorious
        victor.
        """
        position = self.critter_positions[critter2]
        weapon1 = critter1.fight(CritterInfo(position.x, position.y,
                                                     self.width, self.height,
                                                     critter2.getChar(),
                                                     critter2.getColor(),
                                                     self.get_neighbor_func(position)))
        if self.verbose:
            print("critter_mode.update: {} (unique id={}) selects {}".format(critter1.__class__.__name__, id(critter1), 
                                                                             attack.attack_to_str(weapon1)))
        position = self.critter_positions[critter1]
        weapon2 = critter2.fight(CritterInfo(position.x, position.y,
                                                     self.width, self.height,
                                                     critter1.getChar(),
                                                     critter1.getColor(),
                                                     self.get_neighbor_func(position)))
        if self.verbose:
            print("critter_mode.update: {} (unique id={}) selects {}".format(critter2.__class__.__name__, id(critter2), 
                                                                             attack.attack_to_str(weapon2)))
#        weapon1 = critter1.fight(critter2.getChar())
#        weapon2 = critter2.fight(critter1.getChar())
        CritterModel.verify_weapon(weapon1)
        CritterModel.verify_weapon(weapon2)
        if (weapon1 == attack.ROAR and weapon2 == attack.SCRATCH or
            weapon1 == attack.SCRATCH and weapon2 == attack.POUNCE or
            weapon1 == attack.POUNCE and weapon2 == attack.ROAR):
            critter1.fightOver(True, weapon2)
            critter2.fightOver(False, weapon1)
#            critter1.fightOver(True, weapon2, critter2.getColor())
#            critter2.fightOver(False, weapon1, critter1.getColor())
            return critter1
        elif weapon1 == weapon2:
            if random.random() > .5:
                critter1.fightOver(True, weapon2)
                critter2.fightOver(False, weapon1)
#                critter1.fightOver(True, weapon2, critter2.getColor())
#                critter2.fightOver(False, weapon1, critter1.getColor())
                return critter1
            else:
                critter1.fightOver(False, weapon2)
                critter2.fightOver(True, weapon1)
#                critter1.fightOver(False, weapon2, critter2.getColor())
#                critter2.fightOver(True, weapon1, critter1.getColor())
                return critter2
        else:
                critter1.fightOver(False, weapon2)
                critter2.fightOver(True, weapon1)
#                critter1.fightOver(False, weapon2, critter2.getColor())
#                critter2.fightOver(True, weapon1, critter1.getColor())
                return critter2

    def verify_weapon(weapon):
        """
        Make sure students are using the right weapons. If not, throws
        an exception.
        """
        if weapon not in (attack.ROAR, attack.POUNCE, attack.SCRATCH):
            raise WeaponException("Critter weapon must be ROAR, POUNCE, or SCRATCH!")

    def verify_move(move):
        "Make sure they don't move diagonally."
        if move not in (direction.NORTH, direction.SOUTH, direction.EAST, direction.WEST, direction.CENTER):
            raise LocationException("Don't move diagonally! %s" % move)

    def verify_location(location):
        """
        Make sure students are using the right locations. If not,
        throws an exception.
        """
        if location not in (direction.NORTH, direction.NORTHEAST, direction.NORTHWEST,
                            direction.SOUTH, direction.SOUTHEAST, direction.SOUTHWEST,
                            direction.EAST, direction.WEST, direction.CENTER):
            raise LocationException("That is not a real direction!")

    def random_location(self):
        """
        Calculate a random location for a Critter to be placed. This
        is not guaranteed to terminate by any means, but practically
        we (probably) don't need to be concerned.

        Returns a 2-tuple of integers.
        """
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        while self.grid[x][y] is not None:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
        return Point(x, y)

    def create_parameters(critter):
        """
        This is a bit funky. Because not all Critters take the same
        arguments in their constructor (for example, a Mouse gets a
        color while an Elephant gets an int), we need to check the
        classname and return appropriate things based on that. The
        Java version is a bit nicer because it has access to type
        information for each parameter, but c'est la vie.

        Return value is a tuple, which will be passed as *args to
        the critter's constructor.
        """
        if critter.__name__ == 'Mouse':
            return (color.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),)
        elif critter.__name__ == 'Elephant':
            return (random.randint(1, 15),)
        # No other class needs parameters
        else:
            return ()

    def get_neighbor_func(self, position):
        "Returns the getNeighbor function for a particular position."
        def get_neighbor(direction):
            neighbor_pos = self.move(direction, position)
            neighbor = self.grid[neighbor_pos.x][neighbor_pos.y]
            #print( neighbor, type(neighbor) )
            return neighbor.__class__.__name__ if neighbor else '.'
#            return neighbor.getChar() if neighbor else '.'
        return get_neighbor

    def results(self):
        """
        Returns the critters in the simulation, sorted by alive+kills.
        results()[0] is (overall winner, state of winner).
        """
        return sorted(self.critter_class_states.items(),
                      key=lambda state: -(state[1].kills + state[1].alive))


class ClassInfo():
    """
    This would be a named tuple, but they're immutable and that's
    somewhat unwieldy for this particular case.
    """
    def __init__(self, kills=0, alive=0, initial_count=0):
        self.kills = kills
        self.alive = alive
        self.count = initial_count

    def __repr__(self):
        return '%s %s %s' % (self.kills, self.alive, self.count)

# These exceptions don't really need fancy names
class WeaponException(Exception):
    pass

class LocationException(Exception):
    pass

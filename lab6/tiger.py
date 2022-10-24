import color, attack, direction, random

class Tiger():
    def __init__(self):
        self.count = 0
        self.direction = ""
        self.color = color.ORANGE

    # we can omit a __init__ method if there's nothing we need to initialize

    # @param oppInfo The critter info of the current opponent.
    # @returns Your attack: attack.ROAR, attack.POUNCE, or attack.SCRATCH
    def fight(self, oppInfo):
        return attack.ROAR

    # Give your color.
    # @returns Your current color.
    def getColor(self):
        if (self.color == color.BLACK):
            self.color = color.ORANGE
        else:
            self.color = color.BLACK
        return self.color
        # MY CODE FUCKING SUCKS ASS
        




    # Give your move this round.
    # @param info your critter info
    # @returns A cardinal direction or staying put: 
    # (direction.NORTH, direction.SOUTH, direction.EAST, direction.WEST, direction.CENTER)
    def getMove(self, info):
         tiger_directions = [direction.NORTH, direction.SOUTH, direction.EAST, direction.WEST]
         if (self.count == 0):
             self.direction = random.choice(tiger_directions)
             self.count = self.count + 1
         elif (self.count >= 2):
             self.count = 0
         else:
             self.count = self.count + 1
         return self.direction


         
         


    # Give the letter that represents you.
    # @returns Whichever character represents this critter.
    def getChar(self):
        return 'T'

    # End of fight shenanigans.
    # @param won Boolean; true if won fight, false otherwise.
    # @param oppAttack Opponent's choice of fight strategy (ROAR, etc)
    # @returns Nothing.
    def fightOver(self, won, oppAttack):
        # we don't do anything in fightOver method here, because a
        # Stone doesn't do anything with this information
        # we have to have the method because the simulation expects every critter class to have one
        # and we'll get a syntax error if we have the def line with nothing indented after it
        # so we use the pass instruction since it literally means "do nothing"
        # leave this method as just pass unless the critter needs to change its behavior based on these parameters
        pass

    def __str__(self):
        return self.__class__.__qualname__
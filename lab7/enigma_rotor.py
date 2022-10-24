# File: enigma_rotor.py

"""
This module is the starter file for the EnigmaRotor class.
"""

from pgl import GCompound
from enigma_constants import *
from utilities import *

def apply_permutation(letter, permutation, offset):
    """
    Applies the permutation to letter with the given offset.
    Returns the resulting letter.
    """
    raise NotImplementedError

def invert_permutation(permutation):
    """
    Returns the inverted version of permuation.
    """
    raise NotImplementedError

class EnigmaRotor(GCompound):
    def __init__(self, x, y, permutation):
        """
        Constructs an object representing an Enigma machine rotor.
        The center of the rotor will be at (x, y), and permutation will be stored in an instance variable.
        The rotor's offset is initialized to 0.
        """
        super().__init__()
        self.rect = create_filled_rect(x, y, ROTOR_WIDTH, ROTOR_HEIGHT, ROTOR_BGCOLOR)
        self.add(self.rect)

        self.label_x = x
        self.label_y = y
        self.label = create_centered_label("A", x, y, ROTOR_FONT)
        self.add(self.label)

        self.permutation = permutation
        self.offset = 0

    def advance(self):
        """
        Advances the rotor one turn. This increments the offset and changes the displayed letter.
        """
        raise NotImplementedError


    def click_action(self, enigma):
        """
        Clicking on a rotor advances it.
        """
        self.advance()

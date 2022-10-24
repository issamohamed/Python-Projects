# file: enigma_lamp.py
# 

"""
This module is the starter file for the EnigmaLamp class.
"""

from pgl import GCompound
from enigma_constants import *
from utilities import *


class EnigmaLamp(GCompound):
    def __init__(self, x, y, letter):
        """
        Constructs an object representing a lamp on the Enigma machine.
        The center of the lamp will be (x, y) and it will display the string letter as its text.
        """
        super().__init__()
        self.oval = create_filled_circle(x, y, LAMP_RADIUS, LAMP_BGCOLOR, LAMP_BORDER_COLOR)
        self.add(self.oval)

        self.label = create_centered_label(letter, x, y, LAMP_FONT)
        self.label.setColor(LAMP_OFF_COLOR)
        self.add(self.label)

    def turn_on(self):
        """
        Makes the lamp appear lit by changing the label color.
        """
        raise NotImplementedError

    def turn_off(self):
        """
        Makes the lamp appear unlit by changing the label color.
        """
        raise NotImplementedError
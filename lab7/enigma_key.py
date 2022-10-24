# file: enigma_key.py
# 

"""
This module is the starter file for the EnigmaKey class.
"""

from pgl import GCompound
from enigma_constants import *
from utilities import *


class EnigmaKey(GCompound):
    def __init__(self, x, y, letter):
        """
        Constructs an object representing a key on the Enigma machine keyboard
        The center of the key will be located at (x, y) and it will display the string letter
        as its text.
        """
        super().__init__()
        self.oval = create_filled_circle(x, y, KEY_RADIUS, KEY_BGCOLOR, KEY_BORDER_COLOR)
        self.oval.setLineWidth(KEY_BORDER)
        self.add(self.oval)

        self.label = create_centered_label(letter, x, y, KEY_FONT)
        self.label.setColor(KEY_UP_COLOR)
        self.add(self.label)
        
        self.letter = letter

    def mousedown_action(self, enigma):
        """
        Handles the user pressing the mouse button on this key. enigma parameter is the
        instance of the EnigmaMachine class. This method should change the label color (Milestone #2)
        and call enigma.key_pressed with self.letter (Milestone #4).
        """ 
        raise NotImplementedError

    def mouseup_action(self, enigma):
        """
        Handles the user releasing the mouse button on this key. enigma parameter is the
        instance of the EnigmaMachine class. This method should change the label color (Milestone #2)
        and call enigma.key_released with self.letter (Milestone #4).
        """
        raise NotImplementedError

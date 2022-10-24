# File: enigma_machine.py
#

"""
This module is the starter file for the EnigmaMachine class.
"""

import time
from types import LambdaType
from pgl import GImage
from enigma_key import EnigmaKey
from enigma_lamp import EnigmaLamp
from enigma_rotor import EnigmaRotor, apply_permutation, invert_permutation
from enigma_constants import *

# Class: EnigmaMachine

class EnigmaMachine():
    """
    This class is responsible for storing the data needed to simulate
    the Enigma machine.  If you need to maintain any state information
    that must be shared among different parts of this implementation,
    you should define that information as part of this class and
    provide the necessary getters, setters, and other methods needed
    to manage that information.
    """

    def __init__(self, gw):
        """
        The constructor for the EnigmaMachine class is responsible for
        initializing the graphics window along with the state variables
        that keep track of the machine's operation.
        """
        enigmaImage = GImage("enigma-top-view.png")
        gw.add(enigmaImage)
        for num_letter in range(len(KEY_LOCATIONS)):
            x = KEY_LOCATIONS[num_letter][0]
            y = KEY_LOCATIONS[num_letter][1]
            letter = ALPHABET[num_letter]
            gw.add(EnigmaKey(x, y, letter))
        self.lamps = {}
        for num_lamp in range(len(LAMP_LOCATIONS)):
            x = LAMP_LOCATIONS[num_lamp[0]]
            y = LAMP_LOCATIONS[num_lamp[1]]
            letter = ALPHABET[num_lamp]
            indivual_lamp = EnigmaLamp(x, y, letter)
            self.lamps[ALPHABET[num_lamp]] = indivual_lamp
            gw.add(indivual_lamp)


    def encrypt(self, letter):
        """
        Returns the encrypted version of letter.
        """
        raise NotImplementedError

    def key_pressed(self, letter):
        """
        Handles turning on the corresponding lamp when a key is pressed.
        This should initially be the same lamp as the key (Milestone #4), but eventually the lamp for the encrypted letter (Milestone #7+)
        """
        raise NotImplementedError

    def key_released(self, letter):
        """
        Handles turning off the corresponding lamp when a key is released.
        This should initially be the same lamp as the key (Milestone #4), but eventually the lamp for the encrypted letter (Milestone #7+)
        """
        raise NotImplementedError

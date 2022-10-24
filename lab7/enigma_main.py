# File: enigma_main.py

"""
This module is the main program for the Enigma machine.  You should
not need to change this file unless you are implementing EXTRA FUN extensions.
"""

from pgl import GWindow
from enigma_machine import EnigmaMachine
from enigma_constants import *

# Main program

if __name__ == "__main__":
    def mousedown_action(e):
        gobj = gw.getElementAt(e.getX(), e.getY())
        if gobj is not None:
            if getattr(gobj, "mousedown_action", None) is not None:
                gobj.mousedown_action(enigma)

    def mouseup_action(e):
        # has click and drag bug (won't call mouseup_action is mouse is released over different object that it was pressed down on)
        gobj = gw.getElementAt(e.getX(), e.getY())
        if gobj is not None:
            if getattr(gobj, "mouseup_action", None) is not None:
                gobj.mouseup_action(enigma)

    def click_action(e):
        gobj = gw.getElementAt(e.getX(), e.getY())
        if gobj is not None:
            if getattr(gobj, "click_action", None) is not None:
                gobj.click_action(enigma)

    gw = GWindow(ENIGMA_WIDTH, ENIGMA_HEIGHT)
    enigma = EnigmaMachine(gw)
    gw.addEventListener("mousedown", mousedown_action)
    gw.addEventListener("mouseup", mouseup_action)
    gw.addEventListener("click", click_action)

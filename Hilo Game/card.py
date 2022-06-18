import random
# CSE 210 | Programming with Classes
# Week 02
#
# @vonsouza
# 06/17/2022
#
# Hilo Game

class Card:
    """A small cube with a different number of spots on each of its six sides.

    Individual cards are represented as a number from 1 to 13.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """
    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def show_card(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
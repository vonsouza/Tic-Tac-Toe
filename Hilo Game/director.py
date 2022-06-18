from card import Card
# CSE 210 | Programming with Classes
# Week 02
#
# @vonsouza
# 06/17/2022
#
# Hilo Game

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game. The player starts the game with 300 points.
        guess (str): The player guesses if the next card will be higher or lower.
        current_card_value (int): The current card value
        previous_card_value (int): The previus card value
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.total_score = 300 

        self.card = Card()
        self.guess = ""
        self.current_card_value = 0
        self.previous_card_value = 0


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """       
        while self.is_playing:
            self.show_card()
            self.get_guess()
            self.get_next_card()
            self.do_updates()
            self.do_outputs()
            self.get_keep_playing()

    def show_card(self):
        """Get the new card (if necessary) and show the current card

        Args:
            self (Director): An instance of Director.
        """           
        print("")
        if self.current_card_value == 0:   #just for the first play
            self.card.show_card()
            self.previous_card_value = self.current_card_value 
            self.current_card_value = self.card.value
        print(f"The card is: {self.current_card_value}")

    def get_guess(self):
        """Ask the user if the next one will be higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        self.guess = input("Higher or Lower? [h/l] ")

    def get_next_card(self):
        """Get the new card and update the  previous card

        Args:
            self (Director): An instance of Director.
        """        
        self.card.show_card()
        self.previous_card_value = self.current_card_value 
        self.current_card_value = self.card.value

        print(f"Next card was: {self.current_card_value}")

    def get_keep_playing(self):      
        """Asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        plain_again = input("Plain again? [y/n] ")
        self.is_playing = (plain_again == "y")
       
    def do_updates(self):
        """Updates the player's score and checking his guess

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if (self.guess == "l") or (self.guess == "L"):
            if self.current_card_value < self.previous_card_value:
                self.total_score = self.total_score + 100
            else:
                self.total_score = self.total_score - 75
        else:
            if self.current_card_value > self.previous_card_value:
                self.total_score = self.total_score + 100
            else:
                self.total_score = self.total_score - 75
        
        if self.total_score <= 0:
            self.is_playing = False

    def do_outputs(self):
        """Displays the score. 

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is: {self.total_score}")
        
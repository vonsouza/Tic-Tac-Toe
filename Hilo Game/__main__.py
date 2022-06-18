from game.director import Director

# Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower 
# than the previous one. Points are won or lost based on whether or not the player guessed correctly.

# Upgrad necessary:
# Don't allow the player to choose a number greater than 9 or less than 1
# Don't allow the player to choose letters
# Don't allow the player to choose numbers already chosen

director = Director()
director.start_game()
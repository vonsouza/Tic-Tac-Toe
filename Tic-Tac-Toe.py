# CSE 210 | Programming with Classes
# Week 01
#
# @vonsouza
# 06/11/2022
#
# Tic-Tac-Toe
# Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, 
# or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

# Upgrad necessary:
# Don't allow the player to choose a number greater than 9 or less than 1
# Don't allow the player to choose letters
# Don't allow the player to choose numbers already chosen

spot1 = "1"
spot2 = "2"
spot3 = "3"
spot4 = "4"
spot5 = "5"
spot6 = "6"
spot7 = "7"
spot8 = "8"
spot9 = "9"
line = "-+-+-"
no_winner = True
max_plays = 9
number_play = 1

def print_menu():
    print(spot1, end=" ")
    print(spot2, end=" ")
    print(spot3)
    print(line)
    print(spot4, end=" ")
    print(spot5, end=" ")
    print(spot6)
    print(line)
    print(spot7, end=" ")
    print(spot8, end=" ")
    print(spot9)

def change_menu(choice, symbol):
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
    if choice == "1":
        spot1 = symbol
    elif choice == "2":
        spot2 = symbol
    elif choice == "3":
        spot3 = symbol
    elif choice == "4":
        spot4 = symbol
    elif choice == "5":
        spot5 = symbol
    elif choice == "6":
        spot6 = symbol
    elif choice == "7":
        spot7 = symbol
    elif choice == "8":
        spot8 = symbol
    elif choice == "9":
        spot9 = symbol

def check_winner():
    global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
    #checking horizontal winner
    if (spot1 is spot2) and (spot1 is spot3):
        return True
    elif (spot4 is spot5) and (spot4 is spot6):
        return True
    elif (spot7 is spot8) and (spot7 is spot9):
        return True
    #checking vertical winner
    elif (spot1 is spot4) and (spot1 is spot7):
        return True
    elif (spot2 is spot5) and (spot2 is spot8):
        return True
    elif (spot3 is spot6) and (spot3 is spot6):
        return True
    #checking diagonal winner
    elif (spot1 is spot5) and (spot1 is spot9):
        return True
    elif (spot3 is spot5) and (spot3 is spot7):
        return True
    #no winner
    else:
        return False

if __name__ == "__main__":
    print('Welcome to Tic-Tac-Toe!')
    print_menu()

    # The game ends when there is a winner or 9 moves are made
    while no_winner and (number_play <= max_plays):

        #'x's player turn 
        if (number_play % 2) != 0: #odd
            choice = input("'x's turn to choose a square (1-9): ")
            change_menu(choice, "X")
            number_play = number_play + 1
            print_menu()
            if check_winner():
                no_winner = False
                print("'x's player is the winner!")
        
        #'o's player turn 
        else:               #even
            choice = input("'o's turn to choose a square (1-9): ")

            change_menu(choice, "O")
            number_play = number_play + 1
            print_menu()
            if check_winner():
                no_winner = False
                print("'o's player is the winner!")
    print("==========================================END GAME=============================================================")
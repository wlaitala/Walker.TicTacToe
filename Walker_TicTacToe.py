'''
author: Walker Laitala
Created: 11/15/2022
Updated: 11/15/2022

Description: Tic Tac Toe!
Bugs: Game won't end after winner is determiend
      If you put a guy on a space where there is already a guy, it works. But if you do that twice in a row in the same move it will not work(Replaces character already in the space)
      Can't deal with improper input
      Needs documentation
'''

def main():
    '''
    Arguments:
        board: list, is the board
    Takes: 
        Input from users, is a coordinate of two numbers between 1 and 3 seperated by a comma
    Returns:   
        Nothing, sends to next function
    Description: test
        Prints the board, sends to next function. Is the main
    '''
    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]                                 #This is the board^^

    moves(board)                                            #run the moves function

def moves(board):                                           #defines the moves function
    x_input = input("Player X input(row,column): ")         #string, "2,2", where the user wants to put their guy

    rowinput = int(x_input.split(',')[0]) - 1               #rowinput = integer, 2, is the first number the user inputs
    colinput = int(x_input.split(',')[1]) - 1               #colinput = integer, 3, is the second number the user inputs

    if board[rowinput][colinput] == "-":
        board[rowinput][colinput] = "X"                     #set coordinates that the user put in as "X"
    else:
        print("this spot has already been taken")
        x_input = input("Input again (row,column): ")       #string, "2,2", where the user wants to put their guy
        rowinput = int(x_input.split(',')[0]) - 1           #rowinput = integer, 2, is the first number the user inputs
        colinput = int(x_input.split(',')[1]) - 1           #colinput = integer, 3, is the second number the user inputs

    for row in range(3):                                    #a for loop to print the board that goes through every space in the board and prints it
        col = 0                                             #set col as 0 as a baseline
        for col in range(3):                                #nested for loop to handle the column
            print(board[row][col], end = " ")               #actually printing the board
        print(' ')                                          #print a " " after eacher character to make it look pretty

    iswin = win(board)
    if iswin != False:
        print(iswin + " wins!")
        exit

    o_input = input("Player O input(row,column): ")         #string, "2,2", where the user wants to put their guy

    rowinput = int(o_input.split(',')[0]) - 1               #rowinput = integer, 2, is the first number the user inputs
    colinput = int(o_input.split(',')[1]) - 1               #colinput = integer, 3, is the second number the user inputs

    if board[rowinput][colinput] == "-":
        board[rowinput][colinput] = "O"                     #set the coordinates that the user put in as "O"
    else:
        print("this spot has already been taken")
        o_input = input("Player O input(row,column): ")     #string, "2,2", where the user wants to put their guy
        rowinput = int(o_input.split(',')[0]) - 1           #rowinput = integer, 2, is the first number the user inputs
        colinput = int(o_input.split(',')[1]) - 1           #colinput = integer, 3, is the second number the user inputs

    for row in range(3):                                    #a for loop to print the board that goes through every space in the board and prints it
        col = 0                                             #set col as 0 as a baseline
        for col in range(3):                                #nested for loop to handle the column
            print(board[row][col], end = " ")               #actually printing the board
        print(' ')                                          #print a " " after eacher character to make it look pretty

    iswin = win(board)
    if iswin != False:
        print(iswin + " wins!")
        exit

    keepgoing = False   #THIS IS WRONG
    for rows in board:
        for char in rows:
            if char == "-":
                keepgoing = True #If it finds a -, continue the program
            if char != "-":
                break            #if it doesn't find a -, it's a tie. That is how it should work, but you coded it way wrong fool
    
    if keepgoing == True:
        moves(board)
    else:
        print("it's a tie!")
        exit
def win(board):
    '''
    Arguments:
        i: Just a temporary varibale to iterate through range(3), 2
        board: The board as it is when imported into function, list
    Takes:
        the board variable from moves function
    Returns:
        Returns the string "X" or "O" (if it has determined someone has won), or False (if no one has won)
    Description:
        A funtion to determine whether or not someone has won or not, and if someone has won then determine who has won
    '''

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return(board[i][0])
        elif board[0][i] == board[1][i] == board [2][i] != "-":
            return(board[0][i])
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return(board[0][0])
    if board[0][2] == board [1][1] == board[2][0] != "-":
        return(board[0][0])

    return(False)
main()
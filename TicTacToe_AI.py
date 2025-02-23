import time

# A function used to find the best possible response to the user's play
def find_best_response(TTT_table, current_turn):
    if TTT_table[0] == TTT_table[4] and TTT_table[4] == TTT_table[8]:    # \ diagonal
        if TTT_table[0] == "O":
            return 1
        elif TTT_table[0] == "X":
                return -1           #If they are equal but carry "X", the user won

    if TTT_table[2] == TTT_table[4] and TTT_table[4] == TTT_table[6]:    # / diagonal
        if TTT_table[2] == "O":
            return 1
        elif TTT_table[2] == "X":
                return -1
    
    for i in range(0, 7, 3):        #any row
        if TTT_table[0+i] == TTT_table[1+i] and TTT_table[i+1] == TTT_table[i+2]:
            if TTT_table[0+i] == "O":
                return 1
            elif TTT_table[0+i] == "X":
                return -1

    for i in range(0, 3, 1):        #any columnm
        if TTT_table[0+i] == TTT_table[3+i] and TTT_table[3+i] == TTT_table[i+6]:
            if TTT_table[0+i] == "O":
                return 1
            elif TTT_table[0+i] == "X":
                return -1
        
    if "" not in TTT_table:     #If game is finished and no win was found by computer
        return 0

    all_possible_responses_for_X = []
    all_possible_responses_for_O = []
    
    
    for position in range(9):   #going through the tictactoe board
        if TTT_table[position] == "":
            temp_table = TTT_table.copy()
            temp_table[position] = current_turn
            
            if current_turn == "O":  #If the computer filled in an empty space just now, we need to check if that is a good place to put "O"
                outcome = find_best_response(temp_table, "X")   #This takes us down a branch were we see all possible outcomes of putting "O" in that position
                all_possible_responses_for_O.append([outcome, position])    #Keep track of all responses of O to know which one to choose finally

            elif current_turn == "X":       #If it was the user's turn, same logic is applied because we want assume X responds with best play
                outcome = find_best_response(temp_table, "O")
                all_possible_responses_for_X.append([outcome, position])

    
    if current_turn == "O":
        for i in range(len(all_possible_responses_for_O)):
           if all_possible_responses_for_O[i][0] > 0:    #If we found a win for O, return the position to play it
               return all_possible_responses_for_O[i][1]

        for i in range(len(all_possible_responses_for_O)):   #Else, try to find a draw if no win is possible
           if all_possible_responses_for_O[i][0] == 0:
               return all_possible_responses_for_O[i][1]
        
        return -1   #If it is a guaranteed losing position, return -1 so that the machine never plays it
           
           
    elif current_turn == "X":       
        for i in range(len(all_possible_responses_for_X)):
            if all_possible_responses_for_X[i][0] == -1:    #If a win is found for X, we always assume the user will play it, so directly return -1 
               return -1
        return 0    #Else, return a draw if no win was possible (We never return 1 because we assume X won't let the machine win)

# A function to display the table every time changes have been made
def print_table(list):
    for i in range(len(list)):
        if i == 8:
            print(list[i]," |")
        else:
            print(list[i]," | ", end=" ")
        if i == 2 or i == 5:
            print()

# A function to check whether the game ended, or if the machine won
def check_game_status(TTT_table):
    if TTT_table[0] == TTT_table[4] and TTT_table[4] == TTT_table[8]:    # \ diagonal
        if TTT_table[0] == "O":
            print("\nO wins! Better luck next time.\n")
            return True
    if TTT_table[2] == TTT_table[4] and TTT_table[4] == TTT_table[6]:    # / diagonal
        if TTT_table[2] == "O":
            print("\nO wins! Better luck next time.\n")
            return True
    for i in range(0, 7, 3):        #any row
        if TTT_table[0+i] == TTT_table[1+i] and TTT_table[i+1] == TTT_table[i+2]:
            if TTT_table[0+i] == "O":
                print("\nO wins! Better luck next time.\n")
                return True
            
    for i in range(0, 3, 1):        #any columnm
        if TTT_table[0+i] == TTT_table[3+i] and TTT_table[3+i] == TTT_table[i+6]:
            if TTT_table[0+i] == "O":
                print("\nO wins! Better luck next time.\n")
                return True
            
    if "" not in TTT_table:     #If game is finished and no win was found by computer
        print("\nIts a draw! I guess we're both of the same level in this game. Well played!\n")
        return True
    return False

print("\n\n--------------------------------------------------------------")
print("\nLet's play Tic Tac Toe! I bet you can't beat me ;).\n")
print("The rules are simple; We each play a turn and the first player to manage to get 3 consecutive X's or O's wins.")
print("\nPlease note that the positions in the table are numbered as follows:\n")
print("First Row:  1-2-3")
print("Second Row: 4-5-6")
print("Third Row:  7-8-9")
print("\nTherefore, when prompted to choose a position to place your letter in the table, simply type in the position number of interest.")
user_turn = input("\nTo start, please choose whether you would like to go first or second by typing 'f' for first or 's' for second: ")
while user_turn != 'f' and user_turn != 's':
    user_turn = input("\nPlease type either 'f' for first or 's' for second: ")
print("\nVery Well, let us begin! May the better player win!\n")

list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
print_table(list)

TTT_table = ['', '', '', '', '', '', '', '', '']
status = False

if user_turn == 'f':
    while status == False:
        
        while True:
            try:
                user_chosen_pos = int(input("\nPlease type the number (position) which you would like to place X in: "))
                while user_chosen_pos < 1 or user_chosen_pos > 9 or type(user_chosen_pos) != int or TTT_table[user_chosen_pos-1] != "":
                    user_chosen_pos = int(input("\nPlease type in a valid position (between 1 and 9 inclusive and still unused): "))
                break
            except ValueError:
                print("Your input should be a number...")
        
        user_chosen_pos-=1
        print()
        TTT_table[user_chosen_pos] = "X"
        list[user_chosen_pos] = "X"
        
        print_table(list)
        
        print("\nNow it's my turn. Let me think...\n")
        time.sleep(3)
        machine_chosen_pos = find_best_response(TTT_table, "O")
        TTT_table[machine_chosen_pos] = "O"
        list[machine_chosen_pos] = "O"

        print_table(list)

        status = check_game_status(TTT_table)
else:
    while status == False:
        print("\nNow it's my turn. Let me think...\n")
        time.sleep(3)
        machine_chosen_pos = find_best_response(TTT_table, "O")
        TTT_table[machine_chosen_pos] = "O"
        list[machine_chosen_pos] = "O"

        print_table(list)

        status = check_game_status(TTT_table)
        if status == True:
            break

        while True:
            try:
                user_chosen_pos = int(input("\nPlease type the number (position) which you would like to place X in: "))
                while user_chosen_pos < 1 or user_chosen_pos > 9 or type(user_chosen_pos) != int or TTT_table[user_chosen_pos-1] != "":
                    user_chosen_pos = int(input("\nPlease type in a valid position (between 1 and 9 inclusive and still unused): "))
                break
            except ValueError:
                print("Your input should be a number...")

        user_chosen_pos -=1
        print()
        TTT_table[user_chosen_pos] = "X"
        list[user_chosen_pos] = "X"
        
        print_table(list) 
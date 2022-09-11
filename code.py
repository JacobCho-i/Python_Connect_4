board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
win = False
validNums = ["1","2","3","4","5","6","7"]

#display the current game board
def display_board():
    print(" 1  2  3  4  5  6  7")
    print(" V  V  V  V  V  V  V")
    for col in range(6):
        rows = ""
        print("----------------------")
        for row in range(7):
            rows += "|"
            if board[row][col] == 0:
                rows += "  "
            elif board[row][col] == 1:
                rows += "○"
            else:
                rows += "●"
        rows += "|"
        print(rows)
        rows = ""
    print("----------------------")

#determine the player based on the number in the parameter
def changePlayer(num):
    num = num%2
    if num == 0:
        return 1
    elif num == 1:
        return 2

#returns true if there is any available spot in the column and return false otherwise.
def ValidMove(col):
    if 0 in board[col-1]:
            return True
    else:
            return False

#modifies the data in board with data given by parameter
def placeChip(col, player):
    row = 5
    newCol = col - 1
    for i in range(6):
        if board[newCol][row] == 0:
            board[newCol][row] = player
            return
        else:
            row -= 1

#iterate through board and see if there is any connection of 4 chips horizontally, vertically, or diagonally
def checkWin():
    checking = 0
    for row in range(7):
        for col in board[row]:
            if col == 0:
                checking += 1
    #checks for tie
    if checking == 0:
        return 1
    
    #horizontal
    Hstreak = 0
    for row in range(6):
        for col in range(6):
            if board[col][row] != 0:
                if board[col][row] == board[col+1][row]:
                    Hstreak += 1
                else:
                    Hstreak = 0
            if Hstreak == 3:
                if board[col][row] == 1:
                    return 2
                if board[col][row] == 2:
                    return 3
                
    #vertical          
    Vstreak1 = 0
    Vstreak2 = 0
    for col in range(7):
        index = 5
        for row in range(5):
            if board[col][index-row] != 0:
                if board[col][index-row] == board[col][index-row-1]:
                    if board[col][index-row] == 1:
                        Vstreak1 += 1
                    if board[col][index-row] == 2:
                        Vstreak2 += 1
                else:
                    Vstreak1 = 0
                    Vstreak2 = 0
            if Vstreak1 == 3:
                return 2
            if Vstreak2 == 3:
                return 3
                
    #diagonal top left to bottom right
    Dstreak1 = 0
    Dstreak2 = 0
    for row in range(4):
        for col in range(3):
            for index in range(3):
                if board[row+index][col+index] == board[row+index+1][col+index+1]:
                    #print(row+index+1, col+index+1, row+index+2, col+index+2, board[row+index][col+index] == board[row+index+1][col+index+1], Dstreak1)
                    if board[row+index][col+index] != 0:
                        if board[row+index][col+index] == 1:
                            Dstreak1 += 1
                            #print(row+index+1, col+index+1, row+index+2, col+index+2, board[row+index][col+index] == board[row+index+1][col+index+1], Dstreak1)
                        if board[row+index][col+index] == 2:
                            Dstreak2 += 1
                    elif board[row+index][col+index] == 0:
                        Dstreak1 = 0
                        Dstreak2 = 0
                if board[row+index][col+index] != board[row+index+1][col+index+1]:
                    Dstreak1 = 0
                    Dstreak2 = 0
                if Dstreak1 >= 3:
                        return 2
                if Dstreak2 >= 3:
                        return 3
                    
    #diagonal top right to bottom left
    Dstreak3 = 0
    Dstreak4 = 0
    for r in range(4):
        row = 3+r
        for c in range(3):
            col = c
            for index in range(3):
                #print(row-index+1, col-index+1, row-index+2, col-index+2, board[row-index][col-index] == board[row-index-1][col-index-1], Dstreak3)
                if board[row-index][col+index] == board[row-index-1][col+index+1]:
                    if board[row-index][col+index] != 0:
                        if board[row-index][col+index] == 1:
                            Dstreak3 += 1
                        if board[row-index][col+index] == 2:
                            Dstreak4 += 1
                    elif board[row-index][col+index] == 0:
                        Dstreak3 = 0
                        Dstreak4 = 0
                if board[row-index][col+index] != board[row-index-1][col+index+1]:
                       Dstreak3 = 0
                       Dstreak4 = 0
                if Dstreak3 >= 3:
                        return 2
                if Dstreak4 >= 3:
                        return 3
    else:
        return 0

#translate the integer receieved by parameter
def translate(code):
    if code == 1:
        print("the game tied!")
    if code == 2:
        print("P1 wins!")
    if code == 3:
        print("P2 wins!")


player = 0
while win == False:
    count = 0
    display_board()
    num = input("Which column do you want to put chip in? ")

    #check whether input is valid integer
    for i in range(7):
        if num == validNums[i]:
            count += 1
            
    #case when the input is not valid
    if count != 1:
        print("")
        print("please type a valid number")
        print("")

    #case when the input is valid
    else:
        num = int(num)
        test = ValidMove(num)
        currentPlayer = changePlayer(player)
        placeChip(num, currentPlayer)
        if test == True:
            print("")
            print("successfully placed chip")
            print("")
            player += 1
            result = checkWin()
            if result != 0:
                display_board()
                translate(result)
            if result == 1:
                break
            if result == 2:
                win = True
            if result == 3:
                win = True
                
        #case when user attempted to put a chip on the column that is full
        else:
            print("")
            print("please put a valid move!")
            print("")

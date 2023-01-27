def blank_board():
    board=[]
    for i in range(6):
        row=[]
        for x in range(7):
            row.append(".")
        board.append(row)
    return (board)

def read_board():
    x_counter=0
    o_counter=0
    board_list=[]
    b_l=[]
    with open("savegame.txt") as f:
        for line in f:
            board_list.append(line.strip())
        for i in board_list:
            b_r=[]
            for ch in i:
                b_r.append(ch)
            b_l.append(b_r)
    return(b_l)

def display_board(board):
    print("Current gameboard:")
    temp_list=[]
    for i in range(30):
        temp_list.append("-")
    temp_list="".join(temp_list)
    print(temp_list)
    for i in range(len(board)):
        line=[]
        line.append(str(i))
        for x in range(len(board[0])):
            line.append(" | "+ board[i][x])
        line="".join(line)
        print(line)
    print(temp_list)
    column="    0   1   2   3   4   5   6"
    print(column)

def make_move(column, board, player):
    if board[5][int(column)] == ".":
        board[5][int(column)]=player
    elif board[4][int(column)] == ".":
        board[4][int(column)]=player
    elif board[3][int(column)] == ".":
        board[3][int(column)]=player
    elif board[2][int(column)] == ".":
        board[2][int(column)]=player
    elif board[1][int(column)] == ".":
        board[1][int(column)]=player
    elif board[0][int(column)] == ".":
        board[0][int(column)]=player
    else:
        invalid=input("This move is invalid, please choose a new column: ")
        make_move(invalid, board, player)
    return board

def write_board(x):
    with open("savegame.txt", "w") as f:
        for i in x:
            i="".join(i)
            f.write(i+"\n")


def check_winner(board):
    positive_list_r=[5,4,3,2]
    for r in positive_list_r:
        for c in range(len(board[0])-3):
            if board[r][c]==board[r-1][c+1]==board[r-2][c+2]==board[r-3][c+3]=="X":
                return True
            elif board[r][c]==board[r-1][c+1]==board[r-2][c+2]==board[r-3][c+3]=="O":
                return True
    for r in range(len(board)-3):
        for c in range(len(board[0])):
            if board[r][c]==board[r+1][c]==board[r+2][c]==board[r+3][c]=="X":
                return True
            elif board[r][c]==board[r+1][c]==board[r+2][c]==board[r+3][c]=="O":
                return True
    for r in range(len(board)-3):
        for c in range(len(board[0])-3):
            if board[r][c]==board[r+1][c+1]==board[r+2][c+2]==board[r+3][c+3]=="X":
                return True
            elif board[r][c]==board[r+1][c+1]==board[r+2][c+2]==board[r+3][c+3]=="O":
                return True
    for r in range (len(board)):
        for c in range(len(board[0])-3):
            if board[r][c]==board[r][c+1]==board[r][c+2]==board[r][c+3]=="X":
                return True
            elif board[r][c]==board[r][c+1]==board[r][c+2]==board[r][c+3]=="O":
                return True
    return False

def play():
    type_game=input("Do you want to start a new game(N) or play a saved game(S)?")
    x_counter=0
    o_counter=0
    if type_game=="N":
        board = blank_board()
    elif type_game=="S":
        board = read_board()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="X":
                    x_counter+=1
                elif board[r][c]=="O":
                    o_counter+=1
    if o_counter<x_counter:
        count=1
    else:
        count=0
        player = "X"
    display_board(board)
    x=""
    while x!="Q" and x!="S" and check_winner(board)!=True:
        if count%2==0:
            player = "X"
        elif count%2!=0:
            player = "O"
        print("The current player is: Player", player)
        x= input("Choose the column of your piece, from 0 to 6, type Q to quit, or type S to save: ")
        if x!="Q" and x!="S":
           # y = input("Choose the row of your piece, from 0 to 5: ")
            board = make_move(int(x), board, player)
            display_board(board)
            check_winner(board)
            if check_winner(board)==True:
                print("Congratulations! The winner is: Player", player)
            elif check_winner(board)!=True:
                count+=1
        if x=="S":
            write_board(board)

play()


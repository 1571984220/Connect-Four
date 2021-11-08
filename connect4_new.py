
"""
This module is a module that can play the Connect 4 game. It is allow play with computer or play with other human player.
This game module can save and load the game.

"""

from copy import deepcopy # you may use this for copying a board
import numpy as np
import os
def newGame(player1,player2):
    """ 
    taking  two  string parameters player1 and player2 corresponding  to  the  two  players'  names.  
    The  function  returns  a game dictionary  as specified  in  Task  0. 
    
    """
    
    game = {}

    game['player1']=player1
    game['player2']=player2
    game['who']=1
    y=[]
    for _ in range(6):
        y.append(list(0 for _ in range(7)))
    game['board']=y
    # TODO: Initialize dictionary for a new game 
    return game
def printBoard(board):
    """
    taking a  list  of  lists  as  an  input  and  prints  the  7x6 Connect Four board 
    in a nicely formatted fashion. The input parameter board is of the same format as the corresponding value 
    in the game dictionary specified in Task 0. Board positions which are not occupied by any player should be printed empty. 
    Positions occupied by player 1 should be marked by an  "X",  and  positions  occupied  by  player  2  should  be  
    marked  by  an  "O". For  better  orientation,  
    the function should also print a numeration of the columns 1,2,...,7 above the board. 
    """
    s=''
    t=''
    for i in range(1,8):
        t=t+'|'+str(i)
    t=t+'|'+'\n'+7*'+-'+'+'+"\n"
    
    for c,i in enumerate(board):
        for j in i:
            if j==1:
                s=s+'|'+'X'
            if j==2:
                s=s+'|'+'O'
            if j==0:
                s=s+'|'+' '
        if c<5:
            s=s+"|""\n"
        else:
            s=s+"|"
    s=t+s
    return s
def getValidMoves(board):
    """
    Taking a  list  of  lists  as  an  input.  This  input list represents the Connect Four board and is of the 
    same format as the corresponding value in the game dictionary specified in Task 0. 
    The  function  returns  a  list  of  integers between  0 to 6  
    corresponding  to  the  indices  of  the board columns which are not completely filled. 
    Every integer should appear at most once. 
    If no valid move is possible (i.e., theboard is completely filled), the function returns an empty list.
    """
    return list(c for c,i in enumerate(board[0]) if i==0)
def makeMove(board,move,who):
    """
    The  function takes  as  input  a  list boardrepresenting  the  Connect  Four  board,  
    an  integer move between 0 to 6, and an integer who with possible values 1 or 2. 
    The parameter move corresponds to the  column  index  into  which  the  player  
    with  number who will insert  their 'disc'.  
    The  function  then returns the updated board variable. 
    """
    for i in range(5,-1,-1):
        if board[i][move]==0:
            board[i][move]=who
            break
    return board
def makeMove2(board,move,who):
    """
    no changing the board
    like deepcopy
    """
    temp=deepcopy(board)
    for i in range(5,-1,-1):
        if temp[i][move]==0:
            temp[i][move]=who
            break
    return temp
def makeMove3(board,move,who):
    """
    no changing the board
    like deepcopy
    """
    temp=deepcopy(board)
    for i in range(5,-1,-1):
        if temp[i][move]==0:
            temp[i][move]=who
            break
    return [temp,(i,move)]
def cheakrow(board,who):
    """ 
    this function is cheak the 'board' row by row wheather 'who'
    has connect 4.if there is 4 chess connect return 'True'
    otherwise False
     
    """    
    for i in board:
        c=0
        for  j in i:
            if j !=who:
                c=0
            else:
                c=c+1
                if c==4:
                    return True
    return False
def transpose(board):
    y=[]
    for _ in range(7):
        y.append(list(0 for _ in range(6)))
    temp=deepcopy(board)
    for i in range(7):
        for j in range(6):
            y[i][j]=temp[j][i]
    return y
def cheakcolumn(board,who):
    """ 
    this function is cheak the 'board' column by columnwheather 'who'
    has connect 4if there are 4 chesses connect return 'True'
    otherwise False
      
    """    
    return cheakrow(transpose(board),who)
def cheak_decreasing_diagnal(board,who):
    """ 
    this function is cheak 'who' the 'board' in decreace shape diagnal like from 
    top left to bottom right if  there are 4 chesses connect return 'True'
    otherwise False
      
    """       
    l=[(2,0),(1,0),(0,0),(0,1),(0,2),(0,3)]
    for i in l:
        c=0
        a=i[0]
        b=i[1]
        while True:
            try:
                if board[a][b]!=who:
                    c=0
                else:
                    c=c+1
                    if c==4:
                        return True
            except IndexError:
                break
            a=a+1
            b=b+1
    return False
def  cheak_increase_diagnal(board,who):
    """ 
    this function is cheak 'who' the 'board' in increase shape diagnal like from 
    top right to bottom left if  there are 4 chesses connect return 'True'
    otherwise False     
    """       
    board=list(list(reversed(i))for i in board)
    return cheak_decreasing_diagnal(board,who)
def hasWon(board,who):
    """
     taking as input a list board representing the Connect Four board and an integer who with possible values 1 or 2. 
     The function returns True or False. It returns True if the player with number who occupies four adjacent positions  
     which form a horizontal, vertical, or  diagonal line. 
     The function returns False otherwise.
    """
    if cheakrow(board,who) or cheakcolumn(board,who) or cheak_decreasing_diagnal(board,who) or cheak_increase_diagnal(board,who):
        return True
    return False
def suggestMove1(board,who):
    """
    takeing  as  input  parameters a  list board representing  the Connect  Four  board  and  an  integer 
    who with  possible  values  1  or  2.  It  returns  an  integer  between 0,1,...,6  corresponding  
    to  a  column  index  of  the  board  into  which  player  number who should  insert their "disc".
    """
    v=getValidMoves(board)
    try_board=deepcopy(board)
    
    for i in v:
        if hasWon(makeMove2(try_board,i,who),who):
            return i
        else:
            try_board=deepcopy(board)
    
    for j in v:
        if hasWon(makeMove2(try_board,j,3-who),3-who):
            return j
        else:
            try_board=deepcopy(board)
    return v[0]




def connect_3(board,position):
    """
    cheak is there any connect 3 in given location
    """
    for i in [((0,1),(0,-1)),((1,0),(-1,0)),((1,1),(-1,-1,)),((1,-1),(-1,1))]:
        c=1
        row=position[0]
        colum=position[1]
        w=board[row][colum]
        for j in i:
            a=j[0]
            b=j[1]
            while True:
                try:
                    row=row+a
                    colum=colum+b
                    if board[row][colum]==w:
                        c=c+1
                    else:
                        break
                except IndexError:
                    break
            row=position[0]
            colum=position[1]
            
        if c==3:
            return True
    return False


        
        
def suggestMove2(board,who):
    """
    takeing  as  input  parameters a  board representing  the Connect  Four  board  and  an  integer 
    who with  possible  values  1  or  2.  It  returns  an  integer  between 0 and 6  corresponding  
    to  a  column  index  of  the  board  into  which  player  number who should  insert their "disc".But the suggestMove2
    better than suggestMove1
    """
    v=getValidMoves(board)
    available=deepcopy(v)
    try_board=deepcopy(board)
    d=[]
    
    """
    cheak which move can give you win directly
    """
    
    
    for i in v:
        if hasWon(makeMove(try_board,i,who),who):
            return i
        else:
            try_board=deepcopy(board)

    """
    cheak which move can prevent your enermy win
    """       

    
    try_board=deepcopy(board)
    for j in v:
        if hasWon(makeMove(try_board,j,3-who),3-who):
            return j
        try_board=deepcopy(board)
    try_board=deepcopy(board)

    """
    cheak which place you can not place on
    
    and stop your enemy win
    
    """

    
    d=[]
    for j in v:
        try_board=makeMove(try_board,j,3-who)
        
        for n in getValidMoves(try_board):
            if n !=j and  hasWon(makeMove2(try_board,n,3-who),3-who):
                return n
            if n ==j  and cheakcolumn(makeMove2(try_board,n,3-who),3-who):
                return n
            if n ==j  and hasWon(makeMove2(try_board,n,3-who),3-who):
                d.append(j)

        try_board=deepcopy(board)


    """
    finding the only palce I am safe to place
    v
    """
        


    v= list(i for i in v if i not in d)
    """
    delete some move which after move that enemy can break my potiential connect 4
    """
    
    
    d=[]
    for j in v:
        try_board=makeMove(try_board,j,who)
        
        for n in getValidMoves(try_board):
            if n ==j  and hasWon(makeMove2(try_board,n,who),who) and (cheakcolumn(makeMove2(try_board,n,3-who),3-who)==False):
                d.append(j)

        try_board=deepcopy(board)
    v= list(i for i in v if i not in d)

    
    """
    if there is no safe move it means lost the game
    choose the first move in the list available
    """
    if v==[]:
        if d==[]:
            return available[0]
        else:
            res=4
            m=3
            for i in d:
                if abs(i-3) <= m:
                    m=abs(i-3)
                    res=i
            return res


    
    else:
        """
        if there is some move , start to attack ,choosing some move can make
        connect 3 ,if there is no such move prevent enemy sucessfully connect 3
        """
        for f in [3-who]:
            for a in v:
                temp_res=makeMove3(try_board,a,f)
                temp_board=temp_res[0]
                position=temp_res[1]
                if connect_3(temp_board,position):
                    return a
            
        """
        if there is no some better move , choose the nearest one to the column
        """
            
        res=4
        m=3
        for i in v:
            if abs(i-3) <= m:
                m=abs(i-3)
                res=i


        return res
    return available[0]
    

def remove_next_line_symbol(s):
    """ 
    input is a string ,return a string without the next line symbol
    
    """
    s=list(s)
    del s[-1]
    return "".join(s)

def correct_board(board):
    """
    to cheak the board is the connect 4 board
    0 can not between 1 or 2 in a colum
    """
    for j in range(7):
        for i in range(6):
            if board[i][j]!=0:
                while i<5:
                    i=i+1
                    if board[i][j] == 0:
                        return False
                break
    return True
def loadGame(filename="game.txt"):
    """
    Taking an  optional string argument filename
    The  function attempts to open a text file with this filenameand returns 
    its content in form of a game dictionary as specified in Task 0. 
    """
    if not os.path.exists(filename):
        print("file not found")
        raise FileNotFoundError("the file is not in the same directories")
    with open(filename,mode="rt",encoding="utf-8") as g:
        game={}
        game['player1']=remove_next_line_symbol(g.readline())
        game['player2']=remove_next_line_symbol(g.readline())        
        t=g.readline()
        game['who']=int(t)
        game['board']=[0]*6
        if game['player1']=="" or game['player2']=="" or not ((game['who']==1 or game['who']==2) and len(t)==2):
            raise ValueError("the format of the file is no correct")
        for i in range(6):
            s1=g.readline().replace('\n', '')
            s=s1.split(',')
            if s1 != "":
                game['board'][i]=list(int(k)for k in s if k!='\n' or k!='')
                for j in game['board'][i]:
                    if len(s1)!= 13 or len(game['board'][i])!=7 or any(j not in [0,1,2] for j in game['board'][i]):
                        raise ValueError("the format of the file is no correct")
        if not(correct_board(game['board'])):
            raise ValueError("the format of the file is no correct")
    return game
def saveGame(game,filename="game.txt"):
    """
    takes as input a game dictionary as specified in Task 0,and an optional filenameas a string.
    The function writes the game state into a text file with that filename in the format specified in Task 8.
    """
    with open(filename,mode="w",encoding="utf-8") as g:
        print("the game has been saved to a file.")
        g.write(game['player1']+'\n')
        g.write(game['player2']+'\n')
        g.write(str(game['who'])+'\n')
        for i in game['board']:
            s=(''.join(list(str(i)))).replace('[','').replace(']','').replace(', ', ',')
            g.write(s+'\n')

# TODO: All the other functions of Tasks 2-11 go here.
# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES!

# ------------------- Main function --------------------
def play():
    """ 
    the play function is the main function of the program allow to play 
    
    welcome message and initialize the game dictionary lines  469-501
    
    cheak the loaded file if it some winer lines 504-513
    
    print the initilized board lines 516
    
    using some simple variable lines 517-520
    
    if the player is human player lines 524-550
    
    if the player is computer player lines 552-555
    
    cheak the result win or draw and print the result informatin lines 559-574
    
    update the board if the game is not end lines 576-579
    
    
    
    
    
    
    
    
    
    
    """
    print("*"*55)
    print("***"+" "*8+"WELCOME TO JUNYI'S CONNECT FOUR!"+" "*8+"***")
    print("*"*55,"\n")
    print("player input 'S' is save ,'L' is loading")
    print("Enter the players' names, or type 'C' or 'L'. 'C' is the computer opponent")
    
    # TODO: Game flow control starts here
    #2
    game = {}
    while True:
        player1=input("Name of player 1?")
        if player1=='L':
            fn=input('what is the filename?')
            try:
                if fn=='':
                    game=loadGame("game.txt")
                    break
                else:
                    game=loadGame(fn)
                    break
            except ValueError:
                print("The format is no correct")
                return
            except FileNotFoundError:
                print("The file can not find")
                return
        else:
            player1=player1.capitalize()
            player2=input("Name of player 2?").capitalize()
            if player1 != '' and player2 != '':
                game=newGame(player1,player2)
                break
    print("Okay, let's play!")
    print("")
    chess=[' ','X','O']
    
    
    if getValidMoves(game['board'])==[]:
        return 'There was a draw and ends'
    for i in [1,2]:
        if hasWon(game['board'],i):
            if game['player'+str(i)]=='C':
                print("{} ({}) has won!".format("Computer ",chess[i]))
                return
            else:
                print( "{} ({}) has won!".format(game['player'+str(i)],chess[i]))
                return
    
    
    print(printBoard(game['board']))
    while True:
        board=game['board']
        who=game['who']
        player=game['player'+str(who)]



        if player!='C':
                while True:
                    move=input("{} ({}): which column to select?".format(player,chess[who]))
                    if move=='S':
                        try:
                            filename=input('what is the filename?')
                            if filename =='':
                                saveGame(game)
                            else:
                                saveGame(game,filename=filename)
                        except:
                            print("Could not save the file, invalid input. Try again!'")
                    else:
                        if '.' in move:
                            print('Invalid input. Try again!')
                            continue
                        try:
                            move=int(move)-1
                        except Exception:
                            print('Invalid input. Try again!')
                            continue                           
                        else:
                            if move not in getValidMoves(board):
                                print('Invalid input. Try again!')
                            else:
                                break
                board=makeMove(board,move,who)

        else:
            move_res=suggestMove2(board,who)
            print("Computer ({}) is thinking... and selected column {}.".format(chess[who],move_res+1))  
            board=makeMove(board,move_res,who)

        
        #cheak wheather some winer
        if len(getValidMoves(board))==0:
            print(printBoard(board))            
            print('there is a draw at the end')
            return
        if hasWon(board,who):
            if player=='C':
                
                print(printBoard(board))
                print("{} ({}) has won!".format("Computer ",chess[who]))
                return
               
                
            else:
                print(printBoard(board))
                print( "{} ({}) has won!".format(player,chess[who]))
                return

        game['who']=who
        game['board']=board
        print(printBoard(game['board']))
        game['who']=3-who

if __name__ == '__main__' or __name__ == 'builtins':
    play()
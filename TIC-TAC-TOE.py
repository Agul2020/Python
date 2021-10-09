# Tic-Tac-Toe

import random

def drawBoard(board):
    # This function prints out the board that it was passed. / 打印棋盘
    # "board" is a list of 10 strings representing the board (ignoreindex 0). / board 是包含了10个字符串的一个列表（忽略索引为 0 的字符串）
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Lets the player type which letter they want to be. /让玩家选择 X 或 O。
    # Returns a list with the player's letter as the first item and the computer's letter as the second. / 返回一个列表，其中玩家的字母作为第一项，计算机的字母作为第二项。
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # The first element in the list is the player's letter; the second is the computer's letter. / 列表中第一项是玩家的字母，第二项是计算机的字母
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose which player goes first. / 决定谁先走
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move): # 在游戏板上放置一个标记
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won. / 判断玩家是否获胜
    # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much. / 我们用“bo”代替“board”，用“le”代替“letter”，这样我们就不用打那么多字了。
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top 
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board): 
    # Make a copy of the board list and return it. / 复制游戏板的数据
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board. / 判断游戏上的格子是否为空
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player enter their move. / 让玩家输入他们的落子
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board. / 从落子列表中选择一个落子
    # Returns None if there is no valid move. / 如果该列表为空，返回 None
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move. / 创建计算机的 AI 
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move. / 计算机判断自己能否落子即获胜
    for i in range(1, 10):
        boardCopy = getBoardCopy(board) # 创建 board 列表的一个副本
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Check if the player could win on their next move and block them. / 计算机判断玩家是否可以落子获胜
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free. / 计算机尝试移动到一个角格子
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free. / 尝试移动到中心格子
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides. / 尝试移动到边格子
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise, return False. / 如果板上的每个空间都已被占用，则返回 True。 否则返回 False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic-Tac-Toe!')

while True:
    # Reset the board.
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True # 记录游戏是仍在进行，还是谁赢了或打成平局

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn / 运行玩家的轮次
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn / 运行计算机的轮次 
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
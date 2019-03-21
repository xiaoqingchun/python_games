# coding：utf-8
# author:xiaojia

import random

# 欢迎界面的绘制
def welcome(author,email):
    print('欢迎加入{}的井字棋游戏'.format(author))
    print('--------------------------')
    print('联系:{}'.format(email))
    print('--------------------------')


# 玩家与电脑标记的确认
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('你选的是X 还是 O(不区分大小写)?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# 玩家与电脑谁先手
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return '电脑(computer)'
    else:
        return '玩家(player)'

# 绘制棋盘
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#输赢的判断，参数为棋盘和标记
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

# 是否继续玩
def playAgain():
    print('你是否想要继续玩这个游戏? (yes or no)')
    return input().lower().startswith('y')

# 下棋
def makeMove(board, letter, move):
    board[move] = letter

# 取得棋盘的拷贝
def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

# 判断要下的位置是否是空的
def isSpaceFree(board, move):
    return board[move] == ' '

# 取得玩家要下棋的位置
def getPlayerMove(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('下一步你讲要下在哪个位置? (1-9)')
        move = input()
    return int(move)

# 随机选择移动
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# 取得点下的位置
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

# 判断棋盘是否下满了
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

if __name__ == '__main__':
    welcome('小嘉丶学长','875347754@qq.com')

    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print("由"+turn +' 先手 ！')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == '玩家(player)':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('恭喜! 你赢得了这个比赛（Good Game）!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('这是一个势均力敌的比赛!')
                        break
                    else:
                        turn = '电脑(computer)'

            else:

                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('很遗憾，电脑击败了你! 你输了.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('这是一个势均力敌的比赛!')
                        break
                    else:
                        turn = '玩家(player)'

        if not playAgain():
            break

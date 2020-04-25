board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]



def solve():
        if (checkBoard()):
                return True
        "Takes a sudoku board in array form as a parameter "
        for y in range(0, 9):
                for x in range(0, 9):
                        if (board[y][x] == 0):
                                for i in range(1, 10):
                                        if (checkValid(x, y, i)):
                                                board[y][x] = i
                                                if (solve()):
                                                        return True
                                                else:
                                                        board[y][x] = 0
                                return False
        return True

def checkBoard():
        for y in range(0, 9):
                for x in range(0, 9):
                        if (board[y][x] == 0):
                                return False
        return True

def checkValid(x, y, val):
        "Checking x axis"
        for i in range(0, len(board[y])):
                if (board[y][i] == val):
                        return False
        "Check y axis"
        for i in range(0, len(board)):
                if (board[i][x] == val):
                        return False
        "Checking surrounding square"
        if (y == 0 or y == 3 or y == 6):
                if (csx(x, y+1, val) and csx(x, y+2, val)):
                        return True
        if (y == 1 or y == 4 or y == 7):
                if (csx(x, y-1, val) and csx(x, y+1, val)):
                        return True
        else:
                if (csx(x, y-1, val) and csx(x, y-2, val)):
                        return True
        return False

def csx(x, y, val):
        if (x == 0 or x == 3 or x == 6):
                if (board[y][x+1] == val or board[y][x+2] == val):
                        return False
                return True
        if (x == 1 or x == 4 or x == 7):
                if (board[y][x-1] == val or board[y][x+1] == val):
                        return False
                return True
        else:
                if (board[y][x-1] == val or board[y][x-2] == val):
                        return False
        return True;

def printBoard():
        for i in range(0, len(board)):
                print(board[i])

if (solve()):
        printBoard()

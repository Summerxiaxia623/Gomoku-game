# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:34:26 2021

@author: 夏
"""

finish = False  # if the game is end
flagNum = 1  # the current player
flagch = '*'  # the stone of current player
x = 0  # the x axis for the current player's stone
y = 0  # the y axis for the current player's stone
row = 10
column = 10
print('\033[1;37;44m-------------simple Gomoku---------------\033[0m')
# Initialize the checkerboard
checkerboard = []
for i in range(row):
    checkerboard.append([])
    for j in range(column):
        checkerboard[i].append('-')

# print checkerboard
def print_checkerboard():
    print("\033[1;30;46m----------------------------------\033")
    print("   1 2 3 4 5 6 7 8 9 10")
    for i in range(len(checkerboard)):
        print(chr(i + ord('A')) + " ", end=' ')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j] + " ", end='')
        print()
    print("------------------------------------\033[0m")

# print finished checkerboard
def msg():
    print("\033[1;37;40m-----------------------------")
    print("   1 2 3 4 5 6 7 8 9 10")
    for i in range(len(checkerboard)):
        print(chr(i+ord('A'))+" ", end='')
        for j in range(len(checkerboard[i])):
            print(checkerboard[i][j]+' ', end=' ')
        print()
    print("-----------------------------\033[0m")
    if(flagNum == 1):
        print('\033[34m *wins! ***\033[0m')
    else:
        print('\033[34m o*wins! ***\033[0m')

# check if win
def if_win(x,y,flagch):
    global finish
# check stone's left
    print(checkerboard[9][0:5], flagch)
    if (y-4>=0):
        if checkerboard[x][y - 1] == flagch and checkerboard[x][y - 2] == flagch and checkerboard[x][y - 3] == flagch and checkerboard[x][y - 4] == flagch:
            finish = True

            msg()
# check stone's right
    if (y + 4 < column):
        if (checkerboard[x][y + 1] == flagch and checkerboard[x][y + 2] == flagch and checkerboard[x][y + 3] == flagch and checkerboard[x][y + 4] == flagch):
            finish = True
            msg()
# check stone's top
    if (x-4>=0):
        if (checkerboard[x-1][y] == flagch and checkerboard[x-2][y] == flagch and checkerboard[x-3][y] == flagch and checkerboard[x-4][y] == flagch):
            finish = True
            msg()

# check stone's below
    if (x+4<row):
        if (checkerboard[x+1][y] == flagch and checkerboard[x+2][y] == flagch and checkerboard[x+3][y] == flagch and checkerboard[x+4][y] == flagch):
            finish = True
            msg()
# check the upper right
    if (x-4>=0 and y+4<column):
        if (checkerboard[x-1][y+1] == flagch and checkerboard[x-2][y+2] == flagch and checkerboard[x-3][y+3] == flagch and checkerboard[x-4][y+4] == flagch):
            finish = True
            msg()
# check the lower right
        if (x + 4 < row and y + 4 < column):
            if (checkerboard[x +1][y + 1] == flagch and checkerboard[x + 2][y + 2] == flagch and checkerboard[x + 3][y + 3] == flagch and checkerboard[x + 4][y + 4] == flagch):
                finish = True
                msg()
# check the lower left
        if (x + 4 < row and y - 4 >= 0):
            if (checkerboard[x + 1][y - 1] == flagch and checkerboard[x + 2][y - 2] == flagch and checkerboard[x + 3][y - 3] == flagch and checkerboard[x + 4][y - 4] == flagch):
                finish = True
                msg()

# check the upper left
        if (x - 4 < row and y + 4 < column):
            if (checkerboard[x - 1][y - 1] == flagch and checkerboard[x - 2][y - 2] == flagch and checkerboard[x - 3][y - 3] == flagch and checkerboard[x - 4][y - 4] == flagch):
                finish = True
                msg()

    return finish

# check who is playing
def who(flagNum):
    if flagNum == 1:
        flagch = '*'
        print('\033[1;30;43m * please input coordinate (for example: A1) : \033[0m',end=' ')
    else:
        flagch = 'o'
        print('\033[1;30;43m o please input stone coordinate (for example A1): \033[0m',end=' ')
    return flagch

# record the stone's coordinates
def get_coordinates():
    str = input()
    ch = str[0]
    x = ord(ch)-65
    y = int(str[1:])-1
    print(x,y)
    return x,y

while not finish:
    print_checkerboard()
    flagch = who(flagNum)
    x,y = get_coordinates()
    if x < 0 or x > 9 or y < 0 or y > 9:
        print('\033[31m*** invalid input! please input again! ***\033[0m')
        continue
    if checkerboard[x][y] == '-':
        checkerboard[x][y] = flagch
    else:
        print('\033[31m******The position has already been taken, Please input again! \033[0m')
        continue
    finish = if_win(x,y,flagch)
    flagNum *= -1

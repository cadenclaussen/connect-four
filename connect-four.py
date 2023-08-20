#!bin/python3
import time
from helper import checkWin
import os

board = [[0]*7 for i in range(6)]
def printBoard(board):
    for line in board:
        print(*line)
printBoard(board)
column = 0
playerTiles = ["+", "*"]
turnPlayer = 0
while True:
    while True:
        try:
            column = int(input("What column do you want to place in: "))
            while column >= len(board[0]) or column < 0 or board[0][column] != 0:
                print("Too far")
                column = int(input())
            break
        except:
            pass
    yPos = 0
    xPos = column
    board[yPos][xPos] = playerTiles[turnPlayer]
    os.system("clear")
    printBoard(board)

    print()
    time.sleep(.4)
    while yPos + 1 < len(board) and board[yPos + 1][xPos] not in playerTiles:
        os.system("clear")
        board[yPos][xPos] = 0
        yPos += 1
        board[yPos][xPos] = playerTiles[turnPlayer]
        printBoard(board)
        print()
        time.sleep(.4)
    win = checkWin(board, playerTiles)
    if win != "":
        print(win)
        break
    turnPlayer = (turnPlayer + 1) % len(playerTiles)

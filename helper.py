def checkWin(board, playerTiles):
    isTie = True
    for row in board:
        isTie = isTie and all(row)
    if isTie:
      return "Tie"
    for p in playerTiles:
        #check horizontal wins
        for i in range(len(board)):
            streak = 0
            for j in range(len(board[i])):
                if board[i][j] == p:
                    streak += 1
                else:
                    streak = 0
                if streak == 4:
                    return str(p) + " wins!"
        #check vertical wins
        for j in range(len(board[0])):
            streak = 0
            for i in range(len(board)):
                if board[i][j] == p:
                    streak += 1
                else:
                    streak = 0
                if streak == 4:
                    return str(p) + " wins!"

        #check down and to the right diagonal wins
        for i in range(len(board[0])):
            streak = 0
            for j in range(len(board)):
                try:
                    for x in range(4):
                        if board[j+x][i+x] == p:
                            streak += 1
                            # offset += 1
                        else:
                            streak = 0
                            break
                        if streak == 4:
                            return str(p) + " wins!"
                except:
                    streak = 0
                    pass

        #check up and to the right diagonal wins
        for i in range(len(board[0])):
            streak = 0
            for j in range(len(board)):
                try:
                    for x in range(4):
                        if j-x < 0:
                            continue
                        if board[j-x][i+x] == p:
                            streak += 1
                            # offset += 1
                        else:
                            streak = 0
                            break
                        if streak == 4:
                            return str(p) + " wins!"
                except:
                    streak = 0
                    pass

    return ""

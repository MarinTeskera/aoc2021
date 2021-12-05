for i in range(5, len(drawing)):
    draw = drawing[0:i]

    for board in boards:
        if (hasBingo(board, draw) and len(boards) == 1):
            rj = board
            boards.remove(board)
            break

        elif (hasBingo(board, draw)):
            boards.remove(board)
            break

    if (len(boards) == 0):
        break
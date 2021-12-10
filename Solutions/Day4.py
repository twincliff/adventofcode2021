import numpy as np

f = open("PuzzelInputs/Day4Boards.txt", "r")
inputBoards = f.read()

g = open("PuzzelInputs/Day4Numbers.txt", "r")
inputNumbers = g.read().split(",")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def allX(cells):
    return all(cell == "X" for cell in cells)


def testRow(board, rowNr):
    return allX(board[rowNr])


def testColumn(board, columnNr):
    return allX(list(map(lambda row: row[columnNr], board)))


def testBingo(board):
    bingo = False
    for i in range(0, 4):
        bingo = bingo or testRow(board, i)
        bingo = bingo or testColumn(board, i)
    return bingo


def markWithX(board, number):
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == number:
                board[i][j] = "X"


rows = filter(lambda row: row != "", inputBoards.split("\n"))
rowsAndCells = list(map(lambda row: list(filter(None, row.split(" "))), rows))
boards = list(chunks(rowsAndCells, 5))

iNumber = -1
while not any(map(testBingo, boards)):
    iNumber += 1
    for board in boards:
        markWithX(board, inputNumbers[iNumber])


winingBoard = 0

for board in boards:
    if testBingo(board):
        winingBoard = board

testBoard = [
    ["X", "", "", "", ""],
    ["X", "", "", "", ""],
    ["X", "", "", "", ""],
    ["X", "", "", "", ""],
    ["X", "", "", "", ""],
]
print(testColumn(testBoard, 0))
print(inputNumbers[iNumber], winingBoard)

import numpy as np
import functools

from numpy.core.fromnumeric import diagonal

f = open("PuzzelInputs/Day5.txt", "r")
input = f.read()

rows = input.split("\n")


class Line:
    def __init__(self, unparsedRow):
        row = unparsedRow.split()
        self.start = Coordinate(row[0])
        self.end = Coordinate(row[2])


class Coordinate:
    def __init__(self, unparsed):

        splited = unparsed.split(",")
        self.x = int(splited[0])
        self.y = int(splited[1])


lines = list(map(Line, rows))

maxX = max(map(lambda l: max(l.start.x, l.end.x), lines))
maxY = max(map(lambda l: max(l.start.y, l.end.y), lines))

verticalLines = list(filter(lambda line: line.start.x == line.end.x, lines))
horisontalLines = list(filter(lambda line: line.start.y == line.end.y, lines))

karta = np.full((maxX + 10, maxY + 10), 0)

for line in verticalLines:
    localMaxY = max(line.start.y, line.end.y)
    localMinY = min(line.start.y, line.end.y)
    for y in range(localMinY, localMaxY + 1):
        karta[line.start.x][y] += 1

for line in horisontalLines:
    localMaxX = max(line.start.x, line.end.x)
    localMinX = min(line.start.x, line.end.x)
    for x in range(localMinX, localMaxX + 1):
        karta[x][line.start.y] += 1

dangerSpots = functools.reduce(
    lambda sum, row: sum + functools.reduce(lambda a, b: a + 1 if b > 1 else a, row),
    karta,
    0,
)

print(dangerSpots)

# Part 2

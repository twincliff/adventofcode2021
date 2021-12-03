import functools

f = open("PuzzelInputs/Day3.txt", "r")
rawInput = f.read()
inputRows = rawInput.split()

# Part 1
counter = {}
for row in inputRows:
    for i, character in enumerate(row):
        if i not in counter:
            counter[i] = {}
        counter[i][character] = counter[i].get(character, 0) + 1
print(counter)

gamma = 0
epsilon = 0

for i in range(12):
    ones = counter[11 - i]["1"]
    zeroes = counter[11 - i]["0"]
    print(ones > zeroes, 2 ** i)
    if ones > zeroes:
        gamma = gamma + 2 ** i
    else:
        epsilon = epsilon + 2 ** i

print(gamma, epsilon, gamma * epsilon)

# Part 2


def mostOnesInPosition(arr, i):
    column = map(lambda str: str[i], arr)
    ones = functools.reduce(lambda a, b: a + 1 if b == "1" else a, column, 0)
    return ones >= len(arr) / 2


mostOnesInPosition(inputRows, 0)
oxygeValues = inputRows
i = 0
while len(oxygeValues) > 1:
    mostOnes = mostOnesInPosition(oxygeValues, i)
    toKeep = "1" if mostOnes else "0"
    oxygeValues = list(filter(lambda row: row[i] == toKeep, oxygeValues))
    i += 1
print(oxygeValues)

co2Values = inputRows
i = 0
while len(co2Values) > 1:
    mostOnes = mostOnesInPosition(co2Values, i)
    toKeep = "0" if mostOnes else "1"
    co2Values = list(filter(lambda row: row[i] == toKeep, co2Values))
    i += 1
print(co2Values)

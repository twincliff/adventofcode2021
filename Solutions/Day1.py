f = open("PuzzelInputs/Day1Star1.txt", "r")
input = f.read()


def parse(t):
    return int(t)


numericalInput = list(map(parse, input.split()))

# Part 1
numberOfDecreses = 0
for i, n in enumerate(numericalInput):
    if i != 0 and n > numericalInput[i - 1]:
        numberOfDecreses = numberOfDecreses + 1

# Part 2
numberOfDecreses = 0
for i, n in enumerate(numericalInput):
    if 0 < i < len(numericalInput) - 2 and (
        n + numericalInput[i + 1] + numericalInput[i + 2]
    ) > (numericalInput[i - 1] + n + numericalInput[i + 1]):
        numberOfDecreses = numberOfDecreses + 1


print(numberOfDecreses)

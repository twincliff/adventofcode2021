f = open("PuzzelInputs/Day8.txt", "r")
input = f.read()

rows = input.split("\n")
output = map(lambda o: o.split(), map(lambda r: r.split("|")[1], rows))

outputFlat = [item for sublist in output for item in sublist]

ones = len(list(filter(lambda s: len(s) == 2, outputFlat)))
fours = len(list(filter(lambda s: len(s) == 4, outputFlat)))
sevens = len(list(filter(lambda s: len(s) == 3, outputFlat)))
eights = len(list(filter(lambda s: len(s) == 7, outputFlat)))
print(ones + fours + sevens + eights)

# Part 2


class KeyOutputSet:
    def __init__(self, unparsedRow):
        parts = unparsedRow.split("|")
        self.key = parts[0].split()
        self.displayOutput = parts[1].split()


def containsLettersInString(original, comparison):
    return set(original) >= set(comparison)


def stringSubtraction(original, toBeRemoved):
    return set(original) - set(toBeRemoved)


def findOne(key):
    return next((e for e in key if len(e) == 2), None)


def findFour(key):
    return next((e for e in key if len(e) == 4), None)


def resolveLenFive(key, test):
    if containsLettersInString(test, findOne(key)):
        return 3
    elif containsLettersInString(test, stringSubtraction(findFour(key), findOne(key))):
        return 5
    else:
        return 2


def resolveLenSix(key, test):
    if not containsLettersInString(test, findOne(key)):
        return 6
    elif containsLettersInString(test, findFour(key)):
        return 9
    else:
        return 0


def numberConversion(key, test):
    conversionTable = {
        2: 1,
        3: 7,
        4: 4,
        5: resolveLenFive(key, test),
        6: resolveLenSix(key, test),
        7: 8,
    }

    return conversionTable[len(test)]


def convertToNumber(key, displayOutput):
    return (
        1000 * numberConversion(key, displayOutput[0])
        + 100 * numberConversion(key, displayOutput[1])
        + 10 * numberConversion(key, displayOutput[2])
        + numberConversion(key, displayOutput[3])
    )


keyOutputSets = map(KeyOutputSet, rows)

outputNumbers = map(lambda x: convertToNumber(x.key, x.displayOutput), keyOutputSets)
print(sum(outputNumbers))

f = open("PuzzelInputs/Day2.txt", "r")
rawInput = f.read()


class Instruction:
    def __init__(self, unparsedRow):
        splited = list(unparsedRow.split())
        self.direction = splited[0]
        self.distance = int(splited[1])


def increceDepth(position, value):
    position["depth"] = position["depth"] + value
    return position


def decreseDepth(position, value):
    position["depth"] = position["depth"] - value
    return position


def increceDistance(position, value):

    position["distance"] = position["distance"] + value

    return position


def interpretInstruction(position, instruction):

    switcher = {
        "forward": increceDistance,
        "up": decreseDepth,
        "down": increceDepth,
    }

    func = switcher.get(instruction.direction)
    position = func(position, instruction.distance)
    return position


inputRows = list(rawInput.split("\n"))

instructions = list(map(Instruction, inputRows))

position = {}
position["depth"] = 0
position["distance"] = 0


for instruction in instructions:
    position = interpretInstruction(position, instruction)

print(position["depth"], position["distance"], position["depth"] * position["distance"])

# part2
position = {}
position["depth"] = 0
position["distance"] = 0
position["aim"] = 0


def down(position, value):
    position["aim"] = position["aim"] + value
    return position


def up(position, value):
    position["aim"] = position["aim"] - value
    return position


def forward(position, value):
    position["distance"] = position["distance"] + value
    position["depth"] = position["depth"] + position["aim"] * value
    return position


def interpretInstruction2(position, instruction):
    switcher = {
        "forward": forward,
        "up": up,
        "down": down,
    }

    func = switcher.get(instruction.direction)
    position = func(position, instruction.distance)
    return position


for instruction in instructions:
    position = interpretInstruction2(position, instruction)

print(position["depth"], position["distance"], position["depth"] * position["distance"])

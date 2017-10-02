from Parser4 import *

class Parser5:

    @staticmethod
    # Returns an heterogeneous list. The first element is the input and the second is the quintuples
    def Parse(path):
        lines = open(path, "r").read().split('\n')
        machineInput = Parser5.ParseInput(lines)
        quadruples = Parser5.parseQuintuples(lines)
        return [machineInput, quadruples]


    @staticmethod
    def ParseInput(file):
        # input is the last line of the file
        return file[file.__len__() - 1]

    @staticmethod
    def parseQuintuples(file):
        quintuples = []
        # Lines from 0 to 3 are useless
        # We want lines from 4 until the second to last
        for i in range(4, file.__len__() - 1):
            q = Parser5.ParseSingleQuintuple(file[i])
            quintuples.append(q)
        return quintuples

    @staticmethod
    def ParseSingleQuintuple(line):
        line = re.sub("[() ]", '', line) # remove parentheses and space bars with regex
        symbols = re.split("[=,]", line) # symbols are splitted between ',' or '='
        return Quintuple(symbols[0], symbols[4], symbols[1], symbols[2], symbols[3])


class Quintuple:

    def __init__(self, stateFrom, stateTo, read, write, movement):
        self.stateFrom = stateFrom
        self.stateTo = stateTo
        self.read = read
        self.write = write
        if movement == "+":
            movement = Move.RIGHT
        elif movement == "-":
            movement = Move.LEFT
        else:
            movement = Move.NOPE
        self.movement = movement
        self.print()

    def print(self):
        print("State from: " + self.stateFrom)
        print("State to: " + self.stateTo)
        print("Read: ", self.read)
        print("Write ", self.write)
        print("Movement ", self.movement)
        print("") # new line





"""
turing = Parser5.Parse("entry5.txt")
print("Tuples:")
for quintuple in turing[1]:
    quintuple.print()

t = Parser5.Parse("entry5.txt")
a = Quintuple.reverse(t[1])
for b in a:
    b.print()
"""


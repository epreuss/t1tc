import re # Regex

class Parser:

    @staticmethod
    # Returns an heterogeneous list. The first element is the input and the second is the quadruples
    def Parse(path):
        lines = open(path, "r").read().split('\n')
        machineInput = Parser.ParseInput(lines)
        quadruples = Parser.ParseQuadruples(lines)
        return [machineInput, quadruples]


    @staticmethod
    def ParseInput(file):
        # input is the last line of the file
        return  file[file.__len__() - 1]

    @staticmethod
    def ParseQuadruples(file):
        quadruples = []
        # Lines from 0 to 3 are useless
        # We want lines from 4 until the second to last
        for i in range (4, file.__len__() - 1):
            q = Parser.ParseSingleQuadruple(file[i])
            quadruples.append(q)
        return quadruples

    @staticmethod
    def ParseSingleQuadruple(line):
        line = re.sub("[() ]", '', line) # remove parentheses and space bars with regex
        tuples = line.split('=')
        firstTuple = tuples[0].split(',')
        secondTuple = tuples[1].split(',')
        return Quadruple(firstTuple[0], secondTuple[0], firstTuple[1:], secondTuple[1:])

# Using this class instead of Transition because we need to store this in a better format. We will use this later to
# create the reverse of these quadruples
class Quadruple:

    def __init__(self, stateFrom, stateTo, read, operations):
        self.stateFrom = stateFrom
        self.stateTo = stateTo
        self.read = read
        self.operations = operations

    def print (self):
        print ("State from: " + self.stateFrom)
        print("State to: " + self.stateTo)
        print("Read: ", end='')
        print(self.read)
        print("Operations: ", end='')
        print(self.operations)

'''
turing = Parser.Parse("entry.txt")
print("Input: " + turing[0] + "\n")
print("Tuples:")
for quadruple in turing[1]:
    print("") # new line
    quadruple.print()
'''
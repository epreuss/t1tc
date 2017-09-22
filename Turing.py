__author__ = 'Estevan'
from enum import Enum

class Move(Enum):
    LEFT = -1
    NOPE = 0
    RIGHT = 1

    def __str__(self):
        if self == Move.LEFT:
            return "Left"
        elif self == Move.RIGHT:
            return "Right"
        else:
            return "Nope"

class Transition:
    #read = ['', '', '']
    #execution = ['', '', '']
    #move = [Move, Move, Move]
    #useMove = [False, False, False]

    def __init__(self, read, operation, targetState):
        self.read = read
        self.operation = operation
        self.targetState = targetState

    def print(self):
        print(self.read, " -> ", self.operation)
        #print(self.read + " -> " + self.write + ", " + self.movement.__str__())

class State:
    def __init__(self, transitions, final):
        self.transitions = transitions
        self.final = final

    def process(self, tape):
        operations = []
        for t in self.transitions:
            for i in range(0, 3):
                if t.read[i] == tape.getChar(i) or t.read[i] == '/':
                    operations.append(t.operation[i])
                else:
                    operations.append(0)
        return operations

    def getTargetState(self):
        return self.transitions[0].targetState

    def isFinal(self):
        return self.final

class Tape:
    pos = [0, 0, 0]
    chars = ["", "", ""]

    def __init__(self, chars):
        self.chars = chars

    def print(self):
        print(self.chars)
        print(self.pos)

    def getChar(self, index):
        toList = list(self.chars[index])
        return toList[self.pos[index]]

    def write(self, index, char):
        toList = list(self.chars[index])
        toList[self.pos[index]] = char
        self.chars[index] = ''.join(toList)

    def move(self, index, move):
        if move == Move.LEFT._value_:
            self.pos[index] -= 1
        elif move == Move.RIGHT._value_:
            self.pos[index] += 1

    def execute(self, operations):
        i = 0
        for o in operations:
            if type(o) == str:
                self.write(i, o)
            elif type(o) == int:
                self.move(i, o)
            i += 1

class Turing:
    currState = State
    stateId = 0

    def __init__(self, tape, states):
        self.tape = tape
        self.states = states
        self.currState = states[0]

    def print(self):
        self.tape.print()
        print("Curr State: ", self.stateId)

    def process(self):
        self.print()
        print()
        while not self.currState.isFinal():
            operations = self.currState.process(self.tape)
            self.tape.execute(operations)
            self.changeState(self.currState.getTargetState())
            self.print()
            print()

    def changeState(self, stateId):
        self.stateId = stateId
        self.currState = self.states[stateId]


q0t0 = Transition(['0', 'B', 'B'], ['x', 0, 'B'], 1)
q1t0 = Transition(['/', '/', 'B'], [1, 1, 'B'], 2)
q2t0 = Transition(['0', 'B', 'B'], ['x', 0, 'B'], 3)

q0 = State([q0t0], False)
q1 = State([q1t0], False)
q2 = State([q2t0], False)
q3 = State([], True)

tape3 = Tape(["00", "BB", "BB"])

turing = Turing(tape3, [q0, q1, q2, q3])
turing.process()
#turing.print()

"""
q0t0 = Transition('1', '1', Move.RIGHT, 0)
q0t1 = Transition('x', '1', Move.LEFT, 1)

q0 = State([q0t0, q0t1], False)
q1 = State([], True)

tape = Tape("xx11xx", 2)

turing = Turing(tape, [q0, q1])
turing.process()
"""
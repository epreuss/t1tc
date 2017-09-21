__author__ = 'Estevan'
from enum import Enum

class Movement(Enum):
    LEFT = 0
    RIGHT = 1

    def __str__(self):
        if self == Movement.LEFT:
            return "Left"
        else:
            return "Right"

class Transition:
    def __init__(self, read, write, movement, targetState):
        self.read = read
        self.write = write
        self.movement = movement
        self.targetState = targetState

    def print(self):
        print(self.read + " -> " + self.write + ", " + self.movement.__str__())

class State:
    def __init__(self, transitions, final):
        self.final = final
        self.transitions = transitions

    def process(self, char):
        for t in self.transitions:
            if t.read == char:
                return (t.write, t.movement, t.targetState)
        print("ERROR: State process fail")

    def isFinal(self):
        return self.final

class Tape:
    pos = 0
    chars = ""

    def __init__(self, chars, startPos):
        self.chars = chars
        self.pos = startPos

    def print(self):
        print(self.chars)

    def getChar(self):
        return self.chars[self.pos]

    def write(self, char):
        toList = list(self.chars)
        toList[self.pos] = char
        self.chars = ''.join(toList)

    def move(self, movement):
        if movement == Movement.LEFT:
            self.pos -= 1
        else:
            self.pos += 1

class Turing:
    currState = State

    def __init__(self, tape, states):
        self.tape = tape
        self.states = states
        self.currState = states[0]

    def print(self):
        print("Turing")

    def process(self):
        while not self.currState.isFinal():
            result = self.currState.process(tape.getChar())
            tape.write(result[0])
            tape.move(result[1])
            self.changeState(result[2])
            print(result)
        tape.print()

    def changeState(self, stateId):
        self.currState = self.states[stateId]


q0t0 = Transition('1', '1', Movement.RIGHT, 0)
q0t1 = Transition('x', '1', Movement.LEFT, 1)

q0 = State([q0t0, q0t1], False)
q1 = State([], True)

tape = Tape("xx11xx", 2)

turing = Turing(tape, [q0, q1])
turing.process()

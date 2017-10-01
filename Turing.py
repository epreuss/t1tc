__author__ = 'Estevan'
from enum import Enum
from Parser import Parser


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
        self.lastChosenTransition = 0

    def getCorrectTransition(self, tape):
        correctCount = []
        countIndex = 0
        for t in self.transitions:
            correctCount.append(0)
            for i in range(0, 3):
                if t.read[i] == tape.getChar(i) or t.read[i] == '/':
                    correctCount[countIndex] += 1
            countIndex += 1

        biggest = correctCount[0]
        targetIndex = 0
        for i in range(0, correctCount.__len__()):
            if correctCount[i] > biggest:
                biggest = correctCount[i]
                targetIndex = i

        print("chosen tran: ", targetIndex)
        self.lastChosenTransition = targetIndex
        return self.transitions[targetIndex]

    def process(self, tape):
        operations = []
        t = self.getCorrectTransition(tape)
        for i in range(0, 3):
            if t.read[i] == tape.getChar(i) or t.read[i] == '/':
                operations.append(t.operation[i])
            else:
                operations.append(0)
        return operations

    def getTargetState(self):
        return self.transitions[self.lastChosenTransition].targetState

    def isFinal(self):
        return self.final


class Tape:
    #pos = [0, 0, 0]
    #chars = ["", "", ""]

    def __init__(self, chars):
        self.chars = chars

    def print(self):
        print(self.chars)
        print(self.pos)

    def setInitialPos(self, initial):
        self.pos = initial

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
            print("OP: ", operations)
            self.tape.execute(operations)
            self.changeState(self.currState.getTargetState())
            self.print()
            print()

    def changeState(self, stateId):
        self.stateId = stateId
        self.currState = self.states[stateId]

# Base
q0t0 = Transition(['0', 'B', 'B'], ['x', 0, 'B'], 1)
q1t0 = Transition(['/', '/', 'B'], [1, 1, 'B'], 2)
q2t0 = Transition(['0', 'B', 'B'], ['x', 0, 'B'], 3)

# Copy
"""
Algoritmo de copia:
- Voltar o ponteiro da fita 1 para o inicio, ate encontrar um vazio.
c3t0: Volta a fita 1 para o inicio.
c3t1: Seta o ponteiro para iniciar a copia.
c4t0: Copia o x para a fita 3.
c5t0: Avanca o ponteira da fita 1 e 3.
c4t1: Ao encontrar um vazio na fita 1, acaba.
"""
c3t0 = Transition(['x', '/', '/'], [-1, 0, 0], 3)
c3t1 = Transition(['B', '/', '/'], [1, 0, 0], 4)
c4t0 = Transition(['x', '/', 'B'], ['x', 0, 'x'], 5)
c4t1 = Transition(['B', '/', '/'], [0, 0, 0], 6)
c5t0 = Transition(['/', '/', '/'], [1, 0, 1], 4)


q0 = State([q0t0], False)
q1 = State([q1t0], False)
q2 = State([q2t0], False)

c3 = State([c3t0, c3t1], False)
c4 = State([c4t0, c4t1], False)
c5 = State([c5t0], False)
c6 = State([], True)

tape3 = Tape(["BB00BB", "BBBBBB", "BBBBBB"])
tape3.setInitialPos([2, 0, 0])

turing = Turing(tape3, [q0, q1, q2, c3, c4, c5, c6])
turing.process()
print("================RESULT================")
turing.print()


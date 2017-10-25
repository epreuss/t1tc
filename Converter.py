from Parser5 import *


class Converter:
    @staticmethod
    def reverse(quintuples, alphabet):
        result = []
        result += Converter.getCompute1(quintuples)
        result += Converter.getComputeM(quintuples)
        result += Converter.getComputeN(quintuples)
        result += Converter.getCopyOutput(alphabet)
        result += Converter.getRetraceN(quintuples)
        result += Converter.getRetraceM(quintuples)
        result += Converter.getRetrace1(quintuples)

        return result


    @staticmethod
    def getCompute1(quintuples):
        as1 = Quadruple("As", "As'", ["B", "/", "B"], ["B", Move.RIGHT._value_, "B"])
        as2 = Quadruple("As'", "A" + quintuples[0].stateFrom, ["/", "B", "/"], [Move.RIGHT._value_, "1", Move.NOPE._value_])
        return [as1, as2]

    @staticmethod
    def getComputeM(quintuples):
        m = 2  # this is and id for every quintuple as seen in the reverse turing machines paper
        quadruples = []
        for q in quintuples:
            # These are the result of the transformation of this quintuple to quadruples.
            a1 = Quadruple("A" + q.stateFrom, "A" + str(m) + "'", [q.read, "/", "B"], [q.write, Move.RIGHT._value_, "B"])
            a2 = Quadruple("A" + str(m) + "'", "A" + q.stateTo, ["/", "B", "/"], [q.movement._value_, str(m), Move.NOPE._value_])

            quadruples += [a1, a2]
            m += 1
        return quadruples

    @staticmethod
    def getComputeN(quintuples):
        af1 = Quadruple("A" + quintuples[quintuples.__len__() - 1].stateTo, "Af'", ["B", "/", "B"], ["B", Move.RIGHT._value_, "B"])
        af2 = Quadruple("Af'", "Af", ["/", "B", "/"], [Move.NOPE._value_, "N", Move.NOPE._value_])
        return [af1, af2]

    @staticmethod
    def getCopyOutput(alphabet):
        # c = 'y'
        # Af volta em um passo a primeira fita caso ela fique em cima de um B.
        aft0 = Quadruple("Af", "B0", ['B', '/', '/'], [-1, 0, 0])
        #b0t0 = Quadruple("B0", "B0", [c, '/', '/'], [-1, 0, 0])
        b0t1 = Quadruple("B0", "B1", ['B', '/', '/'], [1, 0, 0])
        #b1t0 = Quadruple("B1", "B2", [c, '/', 'B'], [c, 0, c])
        b1t1 = Quadruple("B1", "B3", ['B', '/', '/'], [0, 0, 0])
        b2t0 = Quadruple("B2", "B1", ['/', '/', '/'], [1, 0, 1])
        b3t0 = Quadruple("B3", "Cf", ['/', '/', '/'], [0, 0, 0])

        chars = alphabet.split(' ')
        copy_transitions = []
        for c in chars:
            t1 = Quadruple("B0", "B0", [c[0], '/', '/'], [-1, 0, 0])
            t2 = Quadruple("B1", "B2", [c[0], '/', 'B'], [c[0], 0, c[0]])
            copy_transitions += [t1, t2]

        #return [aft0, b0t0, b0t1, b1t0, b1t1, b2t0, b3t0]
        return [aft0, b0t1,  b1t1, b2t0, b3t0] + copy_transitions

    @staticmethod
    def getRetrace1(quintuples):
        c1 = Quadruple("C" + quintuples[0].stateFrom, "Cs'", ["/", "1", "/"], [Move.LEFT._value_, "B", 0])
        c2 = Quadruple("Cs'", "Cs", ["B", "/", "B"], ["B", Move.LEFT._value_, "B"])
        return [c1, c2]

    @staticmethod
    def getRetraceM(quintuples):
        m = 2  # this is and id for every quintuple as seen in the reverse turing machines paper
        quadruples = []
        for q in quintuples:
            c1 = Quadruple("C" + q.stateTo, "C" + str(m) + "'", ["/", str(m), "/"], [Move.inverse(q.movement), "B", Move.NOPE._value_])
            c2 = Quadruple("C" + str(m) + "'", "C" + q.stateFrom, [q.write, "/", "B"], [q.read, Move.LEFT._value_, "B"])

            quadruples += [c1, c2]
            m += 1
        return quadruples

    @staticmethod
    def getRetraceN(quintuples):
        c1 = Quadruple("Cf", "Cf'", ["/", "N", "/"], [Move.NOPE._value_, "B", Move.NOPE._value_])
        c2 = Quadruple("Cf'", "C" + quintuples[quintuples.__len__() - 1].stateTo, ["B", "/", "B"], ["B", Move.LEFT._value_, "B"])
        return [c1, c2]


parseResult = Parser5.Parse("entry5.txt")
alphabet = parseResult[2]
quadruples = Converter.reverse(parseResult[1], alphabet)
states = Quadruple.quadruplesToStates(quadruples)

tape3 = Tape(["B" + parseResult[0] + "BBBBBB", "BBBBBBBBBB", "BBBBBBBBBB"])
tape3.setInitialPos([0, 0, 1])

turing = Turing(tape3, states)
turing.process()
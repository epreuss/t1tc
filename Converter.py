from Parser5 import *


class Converter:
    @staticmethod
    def reverse(quintuples):
        result = []
        #result = Converter.getCompute1(quintuples)
        #result += Converter.getComputeM(quintuples)
        #result += Converter.getComputeN(quintuples)
        #result += Converter.getCopyOutput()
        result += [Quadruple("A1", "Cf", ["/", "/", "/"], [0,0,0])]
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
    def getCopyOutput():
        c = 'y'
        aft0 = Quadruple("Af", "Af", [c, '/', '/'], [-1, 0, 0])
        aft1 = Quadruple("Af", "c4", ['B', '/', '/'], [1, 0, 0])
        b1t0 = Quadruple("c4", "c5", [c, '/', 'B'], [c, 0, c])
        b1t1 = Quadruple("c4", "c6", ['B', '/', '/'], [0, 0, 0])
        b2t0 = Quadruple("c5", "c4", ['/', '/', '/'], [1, 0, 1])
        b3t0 = Quadruple("c6", "c6", ['/', '/', '/'], [0, 0, 0])

        #c3t0 = Transition(['x', '/', '/'], [-1, 0, 0], "AF3")
        #c3t1 = Transition(['B', '/', '/'], [1, 0, 0], "B14")
        #c4t0 = Transition(['x', '/', 'B'], ['x', 0, 'x'], "B25")
        #c4t1 = Transition(['B', '/', '/'], [0, 0, 0], "B26")
        #c5t0 = Transition(['/', '/', '/'], [1, 0, 1], "B34")
        return [aft0, aft1, b1t0, b1t1, b2t0, b3t0]

    @staticmethod
    def getRetrace1(quintuples):
        c1 = Quadruple(quintuples[0].stateFrom, "Cs'", ["/", 1, "/"], [Move.LEFT._value_, "B", 0])
        c2 = Quadruple("Cs'", "Cs", ["B", "/", "B"], ["B", Move.LEFT._value_, "B"])
        return [c1, c2]

    @staticmethod
    def getRetraceM(quintuples):
        m = 1  # this is and id for every quintuple as seen in the reverse turing machines paper
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
        c2 = Quadruple("Cf'", quintuples[quintuples.__len__() - 1].stateTo, ["B", "/", "B"], ["B", Move.LEFT._value_, "B"])
        return [c1, c2]


parseResult = Parser5.Parse("entry5.txt")
quadruples = Converter.reverse(parseResult[1])
states = Quadruple.quadruplesToStates(quadruples)

tape3 = Tape(["ByBBBB", "B12NBB", "ByBBBB"])
tape3.setInitialPos([1, 3, 1])

turing = Turing(tape3, states)
turing.process()
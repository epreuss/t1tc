from Parser5 import *


class Converter:
    @staticmethod
    def reverse(quintuples):
        result = Converter.getCompute1(quintuples)
        result += Converter.getComputeM(quintuples)
        result += Converter.getComputeN(quintuples)

        result += Converter.getRetraceN(quintuples)
        result += Converter.getRetraceM(quintuples)
        result += Converter.getRetrace1(quintuples)

        return result


    @staticmethod
    def getCompute1(quintuples):
        as1 = Quadruple("As", "As'", ["B", "/", "B"], ["B", "/", "B"])
        as2 = Quadruple("As'", quintuples[0].stateFrom, ["/", "B", "/"], [Move.RIGHT, 1, Move.NOPE])
        return [as1, as2]

    @staticmethod
    def getComputeM(quintuples):
        m = 1  # this is and id for every quintuple as seen in the reverse turing machines paper
        quadruples = []
        for q in quintuples:
            # These are the result of the transformation of this quintuple to quadruples.
            a1 = Quadruple("A" + q.stateFrom, "A" + str(m) + "'", [q.read, '/', 'B'], [q.write, Move.RIGHT, 'B'])
            a2 = Quadruple("A" + str(m) + "'", "A" + q.stateTo, ['/', 'B', '/'], [q.movement, m, Move.NOPE])

            quadruples += [a1, a2]
            m += 1
        return quadruples

    @staticmethod
    def getComputeN(quintuples):
        af1 = Quadruple(quintuples[quintuples.__len__() - 1].stateTo, "Af'", ["B", "/", "B"], ["B", "/", "B"])
        af2 = Quadruple("Af'", "Af", ["/", "B", "/"], [Move.NOPE, "N", Move.NOPE])
        return [af1, af2]

    @staticmethod
    def getRetrace1(quintuples):
        c1 = Quadruple(quintuples[0].stateFrom, "Cs'", ["/", 1, "/"], [Move.LEFT, "B", 0])
        c2 = Quadruple("Cs'", "Cs", ["B", "/", "B"], ["B", Move.LEFT, "B"])
        return [c1, c2]

    @staticmethod
    def getRetraceM(quintuples):
        m = 1  # this is and id for every quintuple as seen in the reverse turing machines paper
        quadruples = []
        for q in quintuples:
            c1 = Quadruple("C" + q.stateTo, "C" + str(m) + "'", ['/', str(m), '/'], [Move.inverse(q.movement), 'B', Move.NOPE])
            c2 = Quadruple("C" + str(m) + "'", "C" + q.stateFrom, [q.write, '/', 'B'], [q.read, Move.LEFT, 'B'])

            quadruples += [c1, c2]
            m += 1
        return quadruples

    @staticmethod
    def getRetraceN(quintuples):
        c1 = Quadruple("Cf", "Cf'", ["/", "N", "/"], [Move.NOPE, "B", Move.NOPE])
        c2 = Quadruple("Cf'", quintuples[quintuples.__len__() - 1].stateTo, ["B", "/", "B"], ["B", Move.LEFT, "B"])
        return [c1, c2]


quadruples = [Quadruple("s1", "s2", ["a", "b", "c"], ["A", "B", "C"])]
a = Quadruple.quadruplesToStates(quadruples)

a[0].print()

"""
turing = Parser5.Parse("entry5.txt")
tuples = Converter.reverse(turing[1])

for t in tuples:
    t.print()
"""

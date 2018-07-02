class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + '-->'))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinA is None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + '-->'))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a or b == 1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class NorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a or b == 1:
            return 0
        else:
            return 1


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getLabel() + '-->'))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():

    # NOT (( A and B) or (C and D))
    gate1 = AndGate("Gate 1")
    gate2 = AndGate("Gate 2")
    gate3 = OrGate("Gate 3")
    gate4 = NotGate("Gate 4")
    cnn1 = Connector(gate1, gate3)
    cnn2 = Connector(gate2, gate3)
    cnn3 = Connector(gate3, gate4)
    print(gate4.getOutput())

    # NOT( A and B ) and NOT (C and D)
    g1 = NandGate("G1")
    g2 = NandGate("G2")
    g3 = AndGate("G3")
    connector1 = Connector(gt1, gt3)
    connector2 = Connector(gt2, gt3)
    print(gt3.getOutput())



main()

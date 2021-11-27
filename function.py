from solver import Solver


class Function:

    __variables = "ABCDEFGHIJ"

    def __init__(self, varCount, minTerms: list, dontCare=None):
        if dontCare is None:
            dontCare = []
        self.varCount = varCount
        self.minTerms = sorted(minTerms)
        self.dontCare = sorted(dontCare)
        self.minAndBin = self.CreateDict()
        self.solution = Solver(self)
        self.variables = self.__variables[:varCount]

    def GetBinaryMinTerms(self):
        return [self.IntToBin(minTerm, self.varCount) for minTerm in self.minTerms]

    @staticmethod
    def IntToBin(number, places=None):
        binary = "{:b}".format(number)
        if places and len(binary) < places:
            binary = "0" * (places - len(binary)) + binary
        return binary

    def CreateDict(self):
        res = {}
        minTerms = self.minTerms
        binaries = self.GetBinaryMinTerms()
        for key in minTerms:
            for value in binaries:
                res[key] = value
                binaries.remove(value)
                break
        return res

    def PrintFunction(self):
        print("f(" + ", ".join(list(self.variables)) + f") = Σm({self.minTerms})")
        int.__add__(1, 2)

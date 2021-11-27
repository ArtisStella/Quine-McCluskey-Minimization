# from function import Function


class Solver:

    def __init__(self, function):
        self.function = function
        self.steps = []

    def SortBinaries(self):
        minDict = self.function.minAndBin
        minTerms = list(minDict.keys())
        binaryRep = list(minDict.values())
        highestNumberOf1 = self.function.IntToBin(minTerms[len(minTerms) - 1]).count("1")

        groups = []
        for groupNum in range(highestNumberOf1 + 1):
            newGroup = {}
            elements = list(filter(lambda x: (x.count("1") == groupNum), binaryRep))
            for element in elements:
                newGroup[int(element, 2)] = element
            groups.append(newGroup)

        self.steps.append(groups)
        return groups

    def PrintStep1(self):
        groups = self.SortBinaries()
        self.PrintTable(groups, 1)

    def Step(self):
        prevStep = self.steps[-1]

        groups = []
        for groupNum in range(len(prevStep) - 1):

            minDict1 = prevStep[groupNum]
            minTerms1 = list(minDict1.keys())
            binaryRep1 = list(minDict1.values())

            minDict2 = prevStep[groupNum + 1]
            minTerms2 = list(minDict2.keys())
            binaryRep2 = list(minDict2.values())

            newGroup = {}
            unusedGroups = {}
            for minTerm1, binNum1 in enumerate(binaryRep1):
                for minTerm2, binNum2 in enumerate(binaryRep2):
                    if self.OneBitChange(binNum1, binNum2):
                        newGroup[f"{minTerms1[minTerm1]}, {minTerms2[minTerm2]}"] = self.GetDashed(binNum1, binNum2)
                    else:
                        unusedGroups[minTerm1] = binNum1

            groups.append(newGroup)
        self.steps.append(groups)
        return groups

    def PrintStep(self):
        groups = self.Step()
        self.PrintTable(groups, 2)

    def PrimeImplicantTable(self):
        pass

    def Solve(self):
        self.PrintTable(self.SortBinaries(), 1)
        for i in range(2, 4):
            table = self.Step()
            # print(table)
            self.PrintTable(table, i)

    @staticmethod
    def OneBitChange(bin1, bin2):
        dissimilarity = 0
        for i, char in enumerate(bin1):
            if char != bin2[i]:
                dissimilarity += 1
                if dissimilarity > 1:
                    return False
        return True

    @staticmethod
    def GetDashed(bin1, bin2):
        res = ""
        for i, char in enumerate(bin1):
            if char != bin2[i]:
                res += "-"
            else:
                res += char
        return res

    @staticmethod
    def PrintTable(groups, stepNum):
        print(f"---------------STEP {stepNum}---------------\n"
              "Group        Minterm          Binary")
        for groupNum, group in enumerate(groups):
            print(f"{groupNum}            ", end="")
            for i, minterm in enumerate(group.keys()):
                if i == len(group.keys()) - 1:
                    print("{:11}        {:8}".format(str(minterm), group[minterm]))
                else:
                    print("{:11}        {:8}".format(str(minterm), group[minterm]), end="\n             ")
            print()

    @staticmethod
    def RemoveDuplicates(dic):
        temp = {val: key for key, val in dic.items()}
        return {val: key for key, val in temp.items()}

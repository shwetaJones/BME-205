class problemThirteen():
    def __init__(self, pathList):
        self.pathList = pathList
        self.start = ""
        self.end = ""
        self.startNodeDict = {}
        self.endNodeDict = {}

    def createStartNodeDict(self):
        for i in self.pathList:
            i = ','.join(i.split(" "))
            iList = i.split(",")
            self.startNodeDict[int(iList[0])] = iList[2:]
        # print(self.startNodeDict)

    def createEndNodeDict(self):
        for key in self.startNodeDict:
            for item in self.startNodeDict[key]:
                if item not in self.endNodeDict:
                    self.endNodeDict[item] = [key]
                else:
                    self.endNodeDict[item].append(key)
        # print(self.endNodeDict)

    def determineStartandEnd(self):
        combinedDict = {**self.startNodeDict, **self.endNodeDict}
        for i in combinedDict:
            combinedDict[i] = []
            if i in self.startNodeDict:
                startCount = len(self.startNodeDict[i])
                if startCount > 0:
                    combinedDict[i].append(startCount)
                else:
                    combinedDict[i].append(0)
            else:
                combinedDict[i].append(0)
            if i in self.endNodeDict:
                endCount = len(self.endNodeDict[i])
                if endCount > 0:
                    combinedDict[i].append(endCount)
                else:
                    combinedDict[i].append(0)
            else:
                combinedDict[i].append(0)
        for i in combinedDict:
            if combinedDict[i][0] > combinedDict[i][1]:
                self.start = i
            if combinedDict[i][0] < combinedDict[i][1]:
                self.end = i
        print(self.start, self.end)
        return len(combinedDict)
        # print(combinedDict)

    # def eulerPath(self):
    #     # counting the number of vertices with odd degree
    #     # print(self.startNodeDict)
    #     self.startNodeDict = {5: [2], 1: [3], 2: [1], 3: [5, 4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}
    #     odd = [x for x in self.startNodeDict.keys() if len(self.startNodeDict[x]) & 1]
    #     odd.append(list(self.startNodeDict.keys())[0])
    #
    #     if len(odd) > 3:
    #         return None
    #
    #     stack = [odd[0]]
    #     path = []
    #
    #     # main algorithm
    #     while stack:
    #         v = stack[-1]
    #         if self.startNodeDict[v]:
    #             u = self.startNodeDict[v][0]
    #             stack.append(u)
    #             # deleting edge u-v
    #             del self.startNodeDict[u][self.startNodeDict[u].index(v)]
    #             del self.startNodeDict[v][0]
    #         else:
    #             path.append(stack.pop())
    #     return path
    #     # print(path)


def main(inFile):
    file = open(inFile, "r")
    pathList = []
    # for line in file:
    #     pathList.append(line.rstrip())
    pathList = ["0 -> 2", "1 -> 3", "2 -> 1", "3 -> 0,4", "6 -> 3,7", "7 -> 8", "8 -> 9", "9 -> 6"]
    # print(pathList)
    processed = problemThirteen(pathList)
    processed.createStartNodeDict()
    processed.createEndNodeDict()
    processed.determineStartandEnd()
    # processed.eulerPath()
    # print(processed.checkEuler(total))
    print(processed.eulerPath())

if __name__== "__main__":
    main("rosalind_ba3g.txt")
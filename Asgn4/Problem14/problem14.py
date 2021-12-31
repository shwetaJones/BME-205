class problemFourteen():
    """ Description: This class """
    """ Input: """
    """ Output: """
    def __init__(self, data, size, length, strings):
        """ Description: """
        """ Input: """
        """ Output: """
        self.data = data
        self.size = size
        self.length = length
        self.strings = strings

    def determineFinalSeq (self):
        """ Description: """
        """ Input: """
        """ Output: """
        while len(self.strings) != self.length:
            for i in self.data:
                if self.strings[-(self.size-1):] == i[:-1]:
                    self.strings += i[-1]
                elif self.strings[:self.size-1] == i[1:]:
                    self.strings = i[0] + self.strings
        return self.strings

def main(inFile):
    """ Description: """
    """ Input: """
    """ Output: """
    data = []
    with open(inFile) as file:
        for x in file.readlines():
            data.append(x.strip("\n"))
        size = int(data.pop(0))
        length = size+len(data)-1
        strings = data.pop(0)
        processed = problemFourteen(data, size, length, strings)
        finalSeq = processed.determineFinalSeq()
        print(finalSeq)


if __name__ == "__main__":
    # main("rosalind_ba3h.txt")
    main("input_14.txt")


# import sys
# import random
#
# class Graph:
#     def __init__(self, patterns):
#         self.patterns = patterns
#         self.edges = []
#         self.nodes = dict()
#         self.stringPath = []
#         self.sequence = ''
#
#     def findEdges(self):
#         for pattern in self.patterns:
#             for otherPattern in self.patterns:
#                 if pattern[1:] == otherPattern[:-1]:
#                     self.edges.append((pattern, otherPattern))
#
#     def findNodes(self):
#         self.findEdges()
#         for edge in self.edges:
#             node1 = edge[0]
#             node2 = edge[1]
#             if node1 not in self.nodes.keys():
#                 self.nodes[node1] = ([], [])
#             self.nodes[node1][1].append(node2)
#             if node2 not in self.nodes.keys():
#                 self.nodes[node2] = ([], [])
#             self.nodes[node2][0].append(node1)
#
#     def getStart(self):
#         self.findNodes()
#         startNode = random.choices(list(self.nodes.keys()))[0]
#         for node in self.nodes.keys():
#             if len(self.nodes[node][1]) - len(self.nodes[node][0]) == 1:
#                 startNode = node
#         return startNode
#
#     def findPath(self, v):
#         vEdges = self.nodes[v][1]
#         while len(vEdges) > 0:
#             newV = random.choices(vEdges)[0]
#             self.nodes[v][1].remove(newV)
#             self.findPath(newV)
#         self.stringPath.insert(0, v)
#
#     def printString(self):
#         self.findPath(self.getStart())
#         for i in range(0, len(self.stringPath)):
#             if i == 0:
#                 self.sequence += self.stringPath[i]
#             else:
#                 self.sequence += self.stringPath[i][-1]
#         print(self.sequence)
#
#
# def main():
#     patterns = []
#     lineCount = 0
#     readFile = open("rosalind_ba3h.txt")
#     for line in readFile:
#         if lineCount > 0:
#             patterns.append(line.strip())
#         lineCount += 1
#     myGraph = Graph(patterns)
#     myGraph.printString()
#
class problemFifteen:
    """Description: This class determines the best path and the corresponding weight of that path """
    """Input: The input for this class comes from the input file provided to main """
    """Output: The output of this method is the best path and the corresponding weight of that path """
    def __init__(self, start, end, pathList):
        """Description: This method initializes variables for the class to utilize """
        """Input: The input for this method is the start and end node of the path and a list of the lines in the input """
        """Output: There is no output for this method, but several important variables are saved """
        self.start = start; self.end = end
        self.pathDictionary = {}; self.edgeDictionary = {}
        for path in pathList:
            self.edgeDictionary[path.split(":")[0]] = path.split(":")[1] #creates the edge dictionary
            startPath = int((path.split(":")[0]).split("->")[0]) #retrieves the beginning of the path
            endPath = int((path.split(":")[0]).split("->")[1]) #retrieves the end of the path
            if startPath in self.pathDictionary: #creates a path dictionary with the source and its corresponding destination
                self.pathDictionary[int(startPath)].append(int(endPath))
            else:
                self.pathDictionary[int(startPath)] = [int(endPath)]
        self.paths = []

        keys = list(self.pathDictionary.keys()) #makes a list of all the keys in the dictionary
        items = list(self.pathDictionary.values()) #makes a list of all the values in the dictionary
        finalItems = [item for sublist in items for item in sublist] #determines the total number of nodes in the graph
        self.nodes = list(set(keys) | set(finalItems))

    def findValidPaths(self, u, visited, path):
        """Description: This method finds all "valid" paths that have the expected start and end node """
        """Input: The input for this method is a node in the graph, a list of visited nodes, and the current path """
        """Output: There is no output for this method, however, it updates a list valid paths """
        visited[u] = True #sets the node to visited
        path.append(u) #appends that node to the path
        if u == self.end: #checks to see if that node matches the end
            temp = []
            for i in range(len(path)):
                temp.append(path[i])
            self.paths.append(temp) #updates the list of all valid paths
        elif u in self.pathDictionary: #checks to see if the node exists
            for i in self.pathDictionary[u]: #iterates through destinations of node
                if visited[i] == False: #looks for valid destination
                    self.findValidPaths(i, visited, path) #goes to the next node, and repeats the method
        path.pop()
        visited[u] = False #sets node back to not visited

    def setPaths(self):
        """Description: This method sets all the nodes to "False" or unvisited """
        """Input: There is no input for this method, however, it uses the initialized values """
        """Output: The output is all the valid paths, by using the findValidPath method """
        visited = {}
        for i in self.nodes: #iterates through the dictionary of nodes to associate every node with a "False"
            visited[i] = False
        self.findValidPaths(self.start, visited, []) #goes to find all the valid paths given source and destination

    def finalDetermination(self):
        """Description: This method prints out the max weight and best path """
        """Input: There is no input for this method, instead it uses the initialized values """
        """Output: The output for this method is the best path and the weight of the path """
        weightList = []; formattedPaths = []
        for i in self.paths:
            combined = '->'.join([str(a) for a in i]) #formats the path by adding in ->
            formattedPaths.append(combined)
            weight = self.calcWeight(i) #uses the calcWeight method to determine the weight of the path
            weightList.append(weight)
        maxWeight = max(weightList) #calculates the largest weight
        maxIndex = weightList.index(maxWeight) #determines the index of the largest weight
        print(maxWeight)
        print(formattedPaths[maxIndex])

    def calcWeight(self, pathway):
        """Description: This method calculates the weight of the path """
        """Input: The input for this method is the pathway """
        """Output: The output for this method is the weight of the given pathway """
        weight = 0
        for i in range(0, len(pathway)-1): #goes through the pathway
            pair = pathway[i:i+2]
            formattedPair = '->'.join([str(a) for a in pair]) #formats the pair so that it can be identified
            if (formattedPair in self.edgeDictionary): #looks for the pair in the edge dicitonary to determine the weight of the path
                weight += int(self.edgeDictionary[formattedPair])
        return weight

def main(inFile):
    """Description: The main controls the reading of the input and printing of the output of this python file """
    """Input: The input file for this method is a .txt file containing the source and destination of the DAG and the paths with its edge weights """
    """Output: The output is best path, and its weight """
    pathList = []
    with open(inFile, "r") as file:
        start = int(file.readline().rstrip()) #saves the source node
        end = int(file.readline().rstrip()) #saves the destination node
        for line in file:
            line = line.rstrip()
            pathList.append(line)
    processed = problemFifteen(start, end, pathList) #initializes values
    processed.setPaths() #calls method that determines all the valid paths
    processed.finalDetermination() #calls method that prints out the best path and its weight

if __name__== "__main__":
    # main("test.txt")
    main("rosalind_ba5d.txt")
    # main("input_15_2.txt")
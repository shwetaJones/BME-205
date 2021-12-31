class problemTwelve():
    """ Description: This class constructs the De Bruijn Graph of a Collection of k-mers """
    """ Input: The input is sequences """
    """ Output: The output is a dictionary """
    def __init__(self, seqList):
        """ Description: The method initializes variables as self """
        """ Input: The input is a list of sequences """
        """ Output: No output, but saved as self """
        self.seqList = seqList #Initializes sequence list as self

    def nodeDict(self):
        """ Description: This method develops a dictionary of nodes """
        """ Input: There is not input, but uses the self """
        """ Output: The output is a dictionary of nodes """
        nodeDict = {}
        for i in self.seqList: #Iterates through sequences and saves as []
            nodeDict[i[:-1]] = []
        for i in self.seqList: #Iterates through sequences and saves as correpsonding nodes
            nodeDict[i[:-1]].append(i[1:])
        return nodeDict #Returns the resulting dictionary

def main(inFile):
    """ Description: The main prints out the De Bruijn Graph of a Collection of k-mers"""
    """ Input: The input is a text file containing sequences """
    """ Output: The output is the De Bruijn Graph of a Collection of k-mers """
    file = open(inFile, "r")
    seqSet = []
    for line in file:
        seqSet.append(line.rstrip()) #Saves each sequence into a list
    processed = problemTwelve(seqSet) #Initializes the variables
    nodeDict = processed.nodeDict() #Creates a dictionary from sequences
    for i in sorted(nodeDict): #Sorts the dictionary and prints it out in a certain fashion
        print(i + ' -> ' + ','.join(sorted(nodeDict[i])))

if __name__== "__main__":
    main("rosalind_ba3e.txt")
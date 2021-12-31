class problemEleven():
    """ Description: The class outputs the deBruijn graph from a sequence """
    """ Input: The input is the length of the kmer and the sequence """
    """ Output: Returns the deBruijn graph """
    def __init__(self, kmerLength, sequence):
        """ Description: The method initializes variables for the class methods """
        """ Input: The input is the kmerlength and sequence """
        """ Output: No output, but these values are initialized """
        self.kmerLength = int(kmerLength)-1 #Saves the length as self
        self.sequence = sequence #Saves sequence as self
        self.totalLength = len(sequence) #Saves the total length of the sequence as self

    def kmerList(self):
        """ Description: The methods creates a list of kmers """
        """ Input: No input, but uses initializes certain values """
        """ Output: The methods returns a list of kmers """
        kmerList = []
        for i in range(int(self.totalLength) - (self.kmerLength) + 1): #Iterates from beginning to end-kmerlength
            kmerList.append(self.sequence[i:i + (self.kmerLength)]) #Adds kmer to list
        return kmerList #Returns a list of kmers

    def kmerDict(self, kmerList):
        """ Description: The method creates a kmer dictionary using the sequences """
        """ Input: There is no input, but it does use a list of sequences """
        """ Output: It returns a dictionary of kmers """
        kmerDict = {}
        for i in range(len(kmerList)): #Creates a dictionary with empty values
            kmerDict[kmerList[i]] = []
        for i in range(len(kmerList)): #Creates dictionary with corresponding kmers
            if (i+1) < len(kmerList):
                next = kmerList[i+1] #Saves the next kmer
                kmerDict[kmerList[i]].append(next) #Adds to the kmer to the dictionary
        return kmerDict #Returns a dictionary of kmers

def main(inFile):
    """ Description: The class outputs the deBruijn graph from a sequence """
    """ Input: The input is the length of the kmer and the sequence """
    """ Output: Returns the deBruijn graph """
    with open(inFile, "r") as file:
        length = file.readline().rstrip() #Removes unnecessary characters
        sequence = file.readline().rstrip() #Removes unnecessary characters
    processed = problemEleven(length, sequence) #Initializes the variables
    kmerList = processed.kmerList() #Creates the kmerList
    kmerDict = processed.kmerDict(kmerList) #Creates the kmerDictionary
    for i in sorted(kmerDict): #Sorts the dictionary
        if kmerDict[i] != []: #Prints only when there are values
            print(i + ' -> ' + ','.join(kmerDict[i])) #Prints out the dictionary in the expected manner

if __name__== "__main__":
    main("rosalind_ba3d.txt")
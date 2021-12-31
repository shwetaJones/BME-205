class problemTen():
    """ Description: This class uses an input file containing a list of sequences to make a overlap graph"""
    """ Input: The input is a set of sequences  """
    """ Output: The main prints out the overlap graph """
    def __init__ (self, seqSet):
        """ Description: This initializes a variable as self """
        """ Input: The input is a set of sequences  """
        """ Output: The main prints out the final sequences consisting of the sequences """
        self.seqSet = seqSet #Initializes the seqSet as self

    def genomePath (self):
        """ Description: The method creates a kmer dictionary using the sequences """
        """ Input: There is no input, but it does use a list of sequences """
        """ Output: It returns a dictionary of kmers """
        kmerDict = dict() #Creates a dictionary called kmerDict
        for seq in self.seqSet: #Iterates through the sequences
            seq2 = seq[1:] #Looks at the first portion of the sequence
            self.seqSet.discard(seq) #Removes the sequences from the set
            for nSeq in self.seqSet: #Iterates through the sequences
                nSeq1 = nSeq[:-1] #Looks at the end portion of the sequence
                if seq2 == nSeq1: #Checks if these portions match
                    kmerDict[seq] = nSeq #Adds to the dictionary
            self.seqSet.add(seq) #Adds the sequence back to the set
        return (kmerDict) #returns the kmerDict

def main(inFile):
    """ Description: The main takes a list of sequences to generate an overlap graph """
    """ Input: The input is lines of sequences """
    """ Output: The main prints out overlap graph """
    file = open(inFile, "r")
    seqSet = set()
    for line in file: #Goes line by line
        seqSet.add(line.rstrip()) #Removes any additonal characters
    sequences = problemTen(seqSet) #Initializes certain values
    for key, value in sorted(sequences.genomePath().items()): #Iterates through the result and prints out the values
        print(key + ' -> ' + value) #Prints out the

if __name__== "__main__":
    main("rosalind_ba3c.txt")
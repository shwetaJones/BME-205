class problemEight():
    def __init__ (self, kmerLength, sequence):
        """ This method initializes variables to be used within the class """
        self.kmerLength = kmerLength #Initializes the length of the kmer as self
        self.sequence = sequence #Initializes the sequence as self
        self.totalLength = len(sequence) #Initializes the total length of the sequence as self

    def printKmers (self):
        """ The print kmers method prints all the kmers in the sequence """
        kmerList = []
        for i in range(int(self.totalLength)-(int(self.kmerLength))+1): #Goes in from the beginning to the end-kmerlength so that all valid kmers are printed
            kmerList.append(self.sequence[i:i+(int(self.kmerLength))]) #Kmer is appended to a list of kmers
        for i in (sorted(kmerList)): #Sorts the kmerList and prints it out one by one
            print(i)

def main(inFile):
    """ The main reads in the input file, and outputs all the kmers in the sequence with a given kmer length"""
    with open(inFile, "r") as file:
        length = file.readline().rstrip() #Removes the newline character
        sequence = file.readline().rstrip() #Removes the newline character
    val = problemEight(length, sequence) #Initializes certain variables
    val.printKmers() #Indenfies and prints out the kmers in the sequence

if __name__== "__main__":
    main("rosalind_ba3a.txt")
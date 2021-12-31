class problemNine():
    """ Description: This class prints out the final sequences """
    """ Input: The input is a list of sequences """
    """ Output: The output is a compiled sequence """
    def __init__ (self, seqList):
        """ Description: This method initializes seqList to be used within the class """
        """ Input: The input is a list of sequences """
        """ Output: The output of this method is nothing, but a variable is initialized as self """
        self.seqList = seqList #Initializes the seqList as self

    def sequenceGen (self):
        """ Description: This method takes the list of sequences, and compiles it into one assembled sequence """
        """ Input: The input nothing, but it uses the seqList """
        """ Output: The output of this method is the final sequence """
        initial = self.seqList[0] #Takes in the first sequence
        finalSeq = []
        finalSeq.append(initial) #Appends the first sequence into the list
        for i in range(1,len(self.seqList)): #Goes through every sequence in the list starting with the 1st index
            nuc = self.seqList[i][24] #Takes the last 2 nucs in the sequence
            finalSeq.append(nuc)  #Appends the last 2 nucs to the finalSeq list
        final = ''.join(finalSeq) #Joins the list into a string
        print(final) #Prints the final sequences

def main(inFile):
    """ Description: The main takes a list of sequences to generate an assembled sequence """
    """ Input: The input is a lines of sequences """
    """ Output: The main prints out the final sequences consisting of the sequences """
    file = open(inFile, "r")
    seqList = []
    for line in file: #Iterates through the file line by line
        line = line.strip() #Removes any characters like the newline character
        seqList.append(line) #Appends the stripped line into seqList
    final = problemNine(seqList) #Initializes the seqList
    final.sequenceGen() #prints the resulting sequence

if __name__== "__main__":
    main("rosalind_ba3b.txt")
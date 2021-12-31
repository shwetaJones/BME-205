class problemSeventeen:
    """ The class gives the cyclospectrum of the given peptide """
    aaWeight = {'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}
    def __init__(self, aaSeq):
        """ Description: Saves the variables as self"""
        """ Input: The input is a sequence of amino acids """
        """ Output: There is no input, however, the amino acid sequence is saved as self """
        self.aaSeq = aaSeq

    def differentSegments(self, doubleAASeq):
        """ Description: The method determines and returns all the segments in the amino acid sequence """
        """ Input: The input is the amino acid sequence """
        """ Output: The output is a list of all the segments """
        segmentList = []
        for k in range(1, len(self.aaSeq)):
            for n in range(len(self.aaSeq)):
                segmentList.append(doubleAASeq[n:n + k]) #appends all the possible segments in this peptide sequence
        segmentList.append(self.aaSeq) #appends the whole peptide sequence
        return(segmentList)

    def calcWeight(self, segmentList):
        """ Description: The method calculates the weight of all the segments """
        """ Input: The input is the list of segments """
        """ Output: The output is a string of all the masses for the segmente"""
        segmentMassList = [0]
        for segment in segmentList:
            mass = 0
            for aa in segment:
                mass += self.aaWeight[aa] #calculates the mass of the segments
            segmentMassList.append(mass) #appends the mass to the list
        sortedSegments = sorted(segmentMassList) #sorted the mass list
        print(len(sortedSegments))
        return (" ".join([str(x) for x in sortedSegments])) #strings together items in the list

def main(inFile):
    """ Description: This controls and outputs the cyclospectrum of the given peptide sequence """
    """ Input: This input file contains the peptide sequence """
    """ Output: The output is the cyclospectrum of the peptide"""
    with open(inFile, "r") as file:
        aaSeq = file.readline().rstrip()
    doubleAASeq = aaSeq + aaSeq #adds the segments together to make sure to get all the possible segments
    processed = problemSeventeen(aaSeq)
    segmentList = processed.differentSegments(doubleAASeq)
    print(processed.calcWeight(segmentList))

if __name__== "__main__":
    # main("test17.txt")
    main("rosalind_ba4c.txt")
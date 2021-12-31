class problemSixteen:
    """ The class outputs the dna sequences that correspond with the amino acid sequences """
    dnaCodonTable = {
        'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
        'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
        'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
        'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
        'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
        'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
        'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'TAA': '-', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'TAG': '-', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
        'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'TGA': '-', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

    def __init__(self,dnaSeq, aminoAcidSeq):
        """ Initializes variables as self and allows other methods to access these variables """
        self.aminoAcidSeq = aminoAcidSeq
        self.aminoAcidSeqList = [aa for aa in aminoAcidSeq]

        self.dnaSeq = dnaSeq
        self.frame1 = []; self.frame2 = []; self.frame3 = []
        self.aaFrame1 = []; self.aaFrame2 = []; self.aaFrame3 = []

        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        self.revSeq = self.reverseComplement(dnaSeq)[::-1]
        self.revFrame1 = []; self.revFrame2 = []; self.revFrame3 = []
        self.aaRevFrame1 = []; self.aaRevFrame2 = []; self.aaRevFrame3 = []


    def reverseComplement(self, seq):
        """ Description: The methods returns the reverse complement of the given sequence """
        """ Input: The method takes in a sequence """
        """ Output: The method returns the reverse complement of the sequence """
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return (''.join([complement[base] for base in (list(seq))]))

    def createFrames(self):
        """ Description: The method creates a list of valid frames """
        """ Input: There is no input for this method, however, it uses the sequence to create all the seqments that fit within the reading frame """
        """ Output: There is no output for this method, however, it updates existing frame lists """
        for i in range(0,len(self.dnaSeq)-1,3): #iterates through dna sequence in iterations of 3
            if len(self.dnaSeq[i:i+3]) == 3: #checks the length of the segment
                self.frame1.append(self.dnaSeq[i:i+3]) #appends the segment to the corresponding frame
                self.aaFrame1.append(self.dnaCodonTable[self.dnaSeq[i:i+3]]) #appends the amino acid to the corresponding frame
            if len(self.dnaSeq[i+1:i+4]) == 3:
                self.frame2.append(self.dnaSeq[i+1:i+4])
                self.aaFrame2.append(self.dnaCodonTable[self.dnaSeq[i+1:i+4]])
            if len(self.dnaSeq[i+2:i+5]) == 3:
                self.frame3.append(self.dnaSeq[i+2:i+5])
                self.aaFrame3.append(self.dnaCodonTable[self.dnaSeq[i+2:i+5]])

        for i in range(0,len(self.revSeq)-1,3):
            self.revFrame1.append(self.revSeq[i:i+3])
            self.aaRevFrame1.append(self.dnaCodonTable[self.revSeq[i:i+3]])
            if len(self.revSeq[i+1:i+4]) == 3:
                self.revFrame2.append(self.revSeq[i+1:i+4])
                self.aaRevFrame2.append(self.dnaCodonTable[self.revSeq[i+1:i+4]])
            if len(self.revSeq[i+2:i+5]) == 3:
                self.revFrame3.append(self.revSeq[i+2:i+5])
                self.aaRevFrame3.append(self.dnaCodonTable[self.revSeq[i+2:i+5]])


    def determinePeptideEncoding(self):
        """ Description: This method checks to see if the given amino acid sequence is encoded in the dna sequence """
        """ Input: There in no input for this method but uses the variables saved as self """
        """ Output: The output for this method is a all the sequences that encode for the specified amino sequence """
        aaSeqLength = len(self.aminoAcidSeq)

        aaFrame1 = "".join(self.aaFrame1)
        aaFrame2 = "".join(self.aaFrame2)
        aaFrame3 = "".join(self.aaFrame3)
        aaRevFrame1 = "".join(self.aaRevFrame1)
        aaRevFrame2 = "".join(self.aaRevFrame2)
        aaRevFrame3 = "".join(self.aaRevFrame3)

        allSeqs = []
        for i in range(len(aaFrame1)): #iterated through the frame
            if self.aminoAcidSeq == aaFrame1[i:i+aaSeqLength]: #checks to see of the amino acid matches with the specified one
                allSeqs.append("".join(self.frame1[i:i+aaSeqLength])) #appends is to the list
        for i in range(len(aaFrame2)):
            if self.aminoAcidSeq == aaFrame2[i:i+aaSeqLength]:
                allSeqs.append("".join(self.frame2[i:i+aaSeqLength]))
        for i in range(len(aaFrame3)):
            if self.aminoAcidSeq == aaFrame3[i:i+aaSeqLength]:
                allSeqs.append("".join(self.frame3[i:i+aaSeqLength]))

        for j in range(len(aaRevFrame1)):
            if self.aminoAcidSeq == aaRevFrame1[j:j+aaSeqLength]:
                allSeqs.append(self.reverseComplement("".join(self.revFrame1[j:j+aaSeqLength]))[::-1])
        for j in range(len(aaRevFrame2)):
            if self.aminoAcidSeq == aaRevFrame2[j:j+aaSeqLength]:
                allSeqs.append(self.reverseComplement("".join(self.revFrame2[j:j+aaSeqLength]))[::-1])
        for j in range(len(aaRevFrame3)):
            if self.aminoAcidSeq == aaRevFrame3[j:j+aaSeqLength]:
                allSeqs.append(self.reverseComplement("".join(self.revFrame3[j:j+aaSeqLength]))[::-1])
        return allSeqs


def main(inFile):
    """ Description: Controls and reads in the input file to print the dna sequences that correspond with the amino acid """
    """ Input: The input file contains a dna sequence and amino acids """
    """ Output: The output file is dna sequences that correspond with the amino acid sepereted be newlines """
    with open(inFile, "r") as file:
        dnaSeq = file.readline().rstrip()
        aminoAcidSeq = file.readline().rstrip()
    processed = problemSixteen(dnaSeq, aminoAcidSeq) #initializes values
    processed.createFrames()
    allSeqs = processed.determinePeptideEncoding()
    print("\n".join(allSeqs))

if __name__== "__main__":
    # main("test16.txt")
    main("rosalind_ba4b.txt")

import sys
import math
class FastAreader:
    ''' This class reads in the FastA file and provides the main the header and sequence in the FastA file'''
    def __init__(self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname
    def doOpen(self):
        ''' Opens the file in stdin '''
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)
    def readFasta(self):
        ''' Reads the file and returns the header and sequence one by one '''
        header = ''
        sequence = ''
        with self.doOpen() as fileH:
            header = ''
            sequence = ''
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>'):
                line = fileH.readline()
            header = line[1:].rstrip()
            for line in fileH:
                if line.startswith('>'):
                    yield header, sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else:
                    sequence += ''.join(line.rstrip().split()).upper()
        yield header, sequence

class CommandLine():
    ''' Deals with the commandLine options provided and sets the values to be used by main and other classes '''
    def __init__(self, inOpts=None):
        ''' Contains all the information that either saves the information given by the user, or uses the default values'''
        import argparse
        self.parser = argparse.ArgumentParser(description='This program find the motif with the highest relative entropy score', add_help=True) #change
        self.parser.add_argument('--minMotif', type=int, action='store', default=3, dest='minMotif')
        self.parser.add_argument('--maxMotif', type=float, action='store', default=8, dest='maxMotif')
        self.parser.add_argument('--cutoff', type=int, action='store', default=-4, dest='cutoff')
        if inOpts is None:
            self.args = self.parser.parse_args()
        else:
            self.args = self.parser.parse_args(inOpts)

class Calculations:
    def __init__(self, seqList, n, totalKmer, kmerDict, totalKmerDict):
        ''' Description: Initializes all the values that will be utilized within the class '''
        ''' Input: The method gets the list of sequences, big n value, total number of kmers, a dictionary containing all kmer counts, and a dictionary containing kmers within the min and max motif '''
        ''' Output: The method initializes certain values that will be changed in future methods '''
        self.seqList = seqList #saves all the sequences in a list form
        self.n = n*2 #multiplies the total number nucleotides by 2 to account for the reverse strand
        self.totalKmer = totalKmer #saves the total number of kmers
        self.kmerDict = kmerDict #saves all the kmers in the sequences between the min and max motif into a dictionary
        self.totalKmerDict = totalKmerDict #saves all the kmers from 1 to max motif into a dictionary

    def addCountCalc (self):
        '''Description: This method calculates the total count of the given sequence and its reverse complement '''
        '''Input: There is no input for this method, rather it accesses the initialized kmer dictionary'''
        '''Output: The  method appends the total count of the sequence and reverse complement to the kmer dictionary'''
        for seq in self.kmerDict:
            count = self.indivCounts(seq)
            self.kmerDict[seq].append(count)

    def indivCounts(self, seq):
        '''Description: This method counts the total number of seqeunces and reverse sequences within the given file '''
        '''Input: The input for this method is a sequences whos count needs to be calculated'''
        '''Output: The output of this method is the total occurences of the sequence and it's reverse complement'''
        count = 0
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        revSeq = ''.join([complement[nuc] for nuc in seq[::-1]]) #determines the reverese complment strand
        if seq in self.totalKmerDict: #finds the number of occurences of the sequence in the fasta
            count += self.totalKmerDict[seq]
        if revSeq in self.totalKmerDict: #finds the number of occurences of the reverse complement
            count += self.totalKmerDict[revSeq]
        return count #returns the count of the kmers in the sequence

    def expectedValueCalc (self):
        '''Description: This method calculates the expected values for each given strand in the kmer dictionary '''
        '''Input: There is no input for this method, rather is accesses the initialized values and dictionaries '''
        '''Output: The method doesn't have a output either, however, it updates the kmer dicitonary with the expected value'''
        for seq in self.kmerDict: #iterates through the kmer dictionary
            n = len(seq) #determines the length of the sequence
            seq1 = seq[:n-1]
            count1 = self.indivCounts(seq1) #finds the number of occurences of this kmer
            seq2 = seq[1:n]
            count2 = self.indivCounts(seq2) #finds the number of occurences of this kmer
            seq3 = seq[1:n-1]
            count3 = self.indivCounts(seq3) #finds the number of occurences of this kmer
            self.kmerDict[seq].append((count1 * count2) / count3) #uses the counts to determine the expected value

    def zScoreCalc(self):
        '''Description: This method calculates the zscore of a given sequences '''
        '''Input: The method has no input, but instead access the initialized variables'''
        '''Output: The method returns a final dictionary with the total count, expected value, and zscore'''
        for seq in self.kmerDict: #iterates through the kmer dictionary
            s = self.kmerDict[seq][2] #saves the count of that kmer as s
            kmer = self.kmerDict[seq][3] #saves the expected value of the kmer as kmer
            numer = s-kmer #determines the numerator value
            denom = math.sqrt(kmer*(1-(kmer/self.n))) #determines the denominator value
            z=numer/denom #calculates the zscore
            self.kmerDict[seq].append(z) #appends the zscore inot the dictionary
        return self.kmerDict #returns the dictionary

def main(inFile, myCommandLine=None):
    '''Description: The main runs the file, and outputs a final print containing the count, expected value, and zscore '''
    '''Input: The input is the input file provideded through commandline '''
    '''Output: The output is a print statement containing count, expected value, and z score in a sorted manner '''
    if myCommandLine is None:
        myCommandLine = CommandLine()  #read options from the command line
    else:
        myCommandLine = CommandLine(
            myCommandLine)  #interpret the list passed from the caller of main as the commandline.
    minMotif = int(myCommandLine.args.minMotif); maxMotif = int (myCommandLine.args.maxMotif) #saves the min and max motif values
    seqList = []
    for head, seq in FastAreader(inFile).readFasta():
        seqList.append(seq) #appends the seq into a seqlist
    bigN = 0; totalKmer = 0
    kmerDict = {}; totalKmerDict = {}
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    dna = ["A", "T", "C", "G"]
    for seq in seqList: #iterates through all the sequences
        bigN += len(seq) #adds the length of the sequence to the big n value
        for length in range(minMotif, maxMotif+1): #iterates from the min motif to the max motif
            for i in range(len(seq)-length): #makes sure to not go beyond the length of the sequence
                sequence = seq[i:i + length] #saves the sequence
                checkValid = [characters in dna for characters in sequence] #checks if the sequence has noncanotical characters
                validity = all(checkValid) #checks if all bases are valid
                if validity == True: #if the kmer is valid, then do the following
                    revSequence = ''.join([complement[nuc] for nuc in sequence[::-1]]) #determines the reverse sequence
                    if sequence not in kmerDict: #if the kmer is not in the dictionary already
                        if revSequence not in kmerDict: #if the reverse complement of the kmer is not in the dictionary already
                            kmerDict[sequence] = [sequence, revSequence] #adds the kmer to the dictionary
        for length in range(1, maxMotif+1): #collects kmers from length of 1 to max motif
            for i in range(len(seq)-length): #makes sure to not go beyond the length of the sequence
                sequence = seq[i:i + length] #saves the sequence
                checkValid = [characters in dna for characters in sequence] #checks if the sequence has noncanotical characters
                validity = all(checkValid) #checks if all bases are valid
                if validity == True: #if the kmer is valid, then do the following
                    revSequence = ''.join([complement[nuc] for nuc in sequence[::-1]]) #determines the reverse sequence
                    totalKmer += 2 #adds to the total kmer count
                    if sequence in totalKmerDict: #if the sequence exists in the dictionary
                        totalKmerDict[sequence] += 2 #adds to the count of that kmer
                    elif revSequence in totalKmerDict: #if the reverse complement of the sequence exists in the dictionary
                        totalKmerDict[revSequence] += 2 #adds to the count of the reverse complement of the kmer
                    else:
                        totalKmerDict[sequence] = 2 #adds to the dictionary
    processedValues = Calculations(seqList, bigN, totalKmer, kmerDict, totalKmerDict) #initializes these values within that class
    processedValues.addCountCalc() #determines the counts of the different kmers
    processedValues.expectedValueCalc() #determines the expected value for the kmers
    finalDict = processedValues.zScoreCalc() #determines the zscore of the kmers
    #Print Outputs
    print(bigN) #prints the total number of nucleotides in the sequences
    sortedFinalDict = dict(sorted(finalDict.items(), key=lambda item: item[1][4])) #sorts the dictionary based on zscore
    sortedDict = {}
    for k in sorted(sortedFinalDict, key=len, reverse=True): #sorts the dictionary based on kmer lenght
        sortedDict[k] = sortedFinalDict[k]
    for i in sortedDict:
        if sortedDict[i][0] > sortedDict[i][1]:#sorts the dictionary in alpha order
            temp = sortedDict[i][0]
            sortedDict[i][0] = sortedDict[i][1]
            sortedDict[i][1] = temp
        if sortedDict[i][4] < myCommandLine.args.cutoff: #prints if the zscore is less than the cutoff value
            print('{0:8}:{1:8}\t{2:0d}\t{3:0.2f}\t{4:0.2f}'.format(sortedDict[i][0], sortedDict[i][1],
                                                                   sortedDict[i][2], sortedDict[i][3],
                                                                   sortedDict[i][4]))
if __name__ == "__main__":
    # main("test", ["--minMotif", "3", "--maxMotif", "4", "--cutoff", "-4"])
    main("Zm4-genomic.fna", ["--minMotif", "3", "--maxMotif", "8", "--cutoff", "-4"]) #Time: 0:33
    # main("Synechococcus7002.fna", ["--minMotif", "3", "--maxMotif", "8", "--cutoff", "-4"]) #Has 6 FastA Sequences #Time: 0:56
    # main("Ecoli-UMN026.fa", ["--minMotif", "3", "--maxMotif", "8", "--cutoff", "-4"]) #Time: 1:28
    # main("Arthrospira-platensis-NIES-39.fna", ["--minMotif", "3", "--maxMotif", "8", "--cutoff", "-4"]) #Time: 1:50
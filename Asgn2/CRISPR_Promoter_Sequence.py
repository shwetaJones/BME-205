import sys
from random import random
import random
import math


# #########################################################################
# File: Jones_Shweta_randomizedMotifSearch.ipynb
#  executable: randomizedMotifSearch.py
# Purpose: To determine the relative entropy score and corresponding consensus given a fasta sequence
#   stdin: fasta sequence containing DNA sequences
#   stderr: errors and status
#   stdout: the relative entropy score and consensus
# Author: Shweta Jones
# Group: Sahasra Shankar, Kritin Nandish, Maheep Luthra
# History:      sj 08/08/2021 Created
#               sj 08/09/2021 Updated
#               sj 08/10/2021 Updated
# #########################################################################
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
        self.parser = argparse.ArgumentParser(
            description='This program find the motif with the highest relative entropy score', add_help=True)
        self.parser.add_argument('-i', '--iterations', type=int, action='store', default=1000, dest='iterations',
                                 help='Provide the number of runs the motif search should take, the default is 1000 iterations.')
        self.parser.add_argument('-p', '--pseudoCount', type=float, action='store', default=1, dest='pseudoCount',
                                 help='Provide the psuedo count, the default is 1 pseudo count.')
        self.parser.add_argument('-k', '--kmerLength', type=int, action='store', default=13, dest='kmerLength',
                                 help='Provide the kmer length')
        if inOpts is None:
            self.args = self.parser.parse_args()
        else:
            self.args = self.parser.parse_args(inOpts)


class Calculations:
    def __init__(self):
        ''' Description: Initializes all the values that will be utilized within the class '''
        ''' Input: The method does not have any inputs '''
        ''' Output: The method initializes certain values that will be changed in future methods '''
        self.aCount = 0;
        self.tCount = 0;
        self.cCount = 0;
        self.gCount = 0
        self.aNull = 0;
        self.tNull = 0;
        self.cNull = 0;
        self.gNull = 0
        self.total = 0
        self.profArray = []

    def createNull(self, a, t, c, g, pCount):
        ''' Description: Calculates the Null Model '''
        ''' Input: This method uses the number of A, T, C and G and the pseudo count '''
        ''' Output: The method saves the null values of each of the nucleotides to be used in other methods '''
        self.aCount += a;
        self.tCount += t;
        self.cCount += c;
        self.gCount += g
        self.total = a + t + c + g + (pCount * 4)  # determines the total numebr of nucleotides with psuedocounts
        self.aNull = ((a + pCount) / self.total);
        self.tNull = ((t + pCount) / self.total);
        self.cNull = ((c + pCount) / self.total);
        self.gNull = ((g + pCount) / self.total)  # calculates the null probabilities of each of the nucleotides

    def randomMotif(self, seqList, kmerLength):
        ''' Description: Retrieves random motifs of a certain length in each of the sequences '''
        ''' Input: This method uses a list of sequences and the length of the k-mer which is specified by the user '''
        ''' Output: The method returns a random motif within each of the sequences '''
        totalLength = len(seqList[0])
        ranList = [random.randint(0, totalLength - (kmerLength + 1)) for i in
                   seqList]  # Creates a list of random motifs that could be anywhere from the beginning of the sequence to the end-kmerlength of the sequence
        motifList = [];
        count = 0
        for i in seqList:
            motifList.append(i[ranList[count]:ranList[
                                                  count] + kmerLength])  # Finds and saves the selected motif into a list of motifs
            count += 1
        return motifList

    def createProfile(self, motifList, kmerLength, pseudoCount):
        ''' Description: This method determines the profile given the list of motifs and length of the k-mer '''
        ''' Input: The input for this method is the list of motif, the length of the k-mer, and the pseudo count '''
        ''' Output: The method returns the profile '''
        self.profArray = [];
        subList = []
        for i in range(kmerLength):  # Creates an empty list of lists
            subList.append([])
        numMotif = len(motifList)
        aProfList = [];
        tProfList = [];
        cProfList = [];
        gProfList = [];
        for i in range(
                kmerLength):  # Creates a 2D array to create the profile by counting the number of nucleotides in specific positions
            for j in range(numMotif):
                subList[i].append(motifList[j][i])
            aProfList.append((subList[i].count("A") + pseudoCount) / (numMotif + (pseudoCount * 4)))
            tProfList.append((subList[i].count("T") + pseudoCount) / (numMotif + (pseudoCount * 4)))
            cProfList.append((subList[i].count("C") + pseudoCount) / (numMotif + (pseudoCount * 4)))
            gProfList.append((subList[i].count("G") + pseudoCount) / (numMotif + (pseudoCount * 4)))
        self.profArray.append(aProfList);
        self.profArray.append(tProfList);
        self.profArray.append(cProfList);
        self.profArray.append(gProfList)  # Places the probabilities into a profile array
        return self.profArray

    def iterMotifs(self, seqList, kmerLength):
        ''' Description: Determines all the motifs in a given set of sequences, and determines a motif with the highest score given the profile '''
        ''' Input: The method uses the all the sequences and the length of the k-mer '''
        ''' Output: The output is the final motif that has the highest value '''
        totalLength = len(seqList[0])
        finalMotif = []
        for i in range(
                len(seqList)):  # Iterates through all the sequences to find the best possible motif for each sequence
            motifList = []
            for j in range(totalLength - kmerLength):  # Finds all the possible motifs in a given sequence
                motifList.append(seqList[i][j:j + kmerLength])
            motifDict = {}
            for k in range(len(motifList)):  # Iterates through all the motifs and calculates based on the profile
                count = 1
                for l in range(
                        kmerLength):  # Iterates through the length of the kmer and calculates it's score based on profile
                    if (motifList[k][l]) == "A":
                        count *= (self.profArray[0][l])
                    elif (motifList[k][l]) == "T":
                        count *= (self.profArray[1][l])
                    elif (motifList[k][l]) == "C":
                        count *= (self.profArray[2][l])
                    elif (motifList[k][l]) == "G":
                        count *= (self.profArray[3][l])
                motifDict[motifList[k]] = count  # Places the motif and it's correpsonding score in a dictionary
            finalMotif.append(max(motifDict,
                                  key=motifDict.get))  # Determines the motif with the highest value and adds it to a list of motifs
        return finalMotif

    def relativeEntropy(self, profile, consensus):
        ''' Description: Calculates the relative entropy of the consensus sequence '''
        ''' Input: The function uses the profile of the final motif and the determined consensus '''
        ''' Output: The method returns the relative entropy score of the consensus '''
        score = 0
        for i in range(len(
                consensus)):  # Goes through all the nucleotides within the consensus and calculates the total relative entropy score
            if consensus[i] == "A":
                score += (profile[0][i]) * (math.log2((profile[0][i]) / self.aNull))
            elif consensus[i] == "T":
                score += (profile[1][i]) * (math.log2((profile[1][i]) / self.tNull))
            elif consensus[i] == "C":
                score += (profile[2][i]) * (math.log2((profile[2][i]) / self.cNull))
            elif consensus[i] == "G":
                score += (profile[3][i]) * (math.log2((profile[3][i]) / self.gNull))
        return (score)


def main(myCommandLine=None):
    ''' Description: Runs the entire program by reading the command line and outputting the corresponding profile and relative entropy score '''
    ''' Input: The input is the options given by the user through the commandLine '''
    ''' Output: The main function prints out the consensus with the highest relative entropy score and its score into the specified output file '''
    if myCommandLine is None:
        myCommandLine = CommandLine()  # read options from the command line
    else:
        myCommandLine = CommandLine(
            myCommandLine)  # interpret the list passed from the caller of main as the commandline.

    seqList = []
    aCount = 0;
    tCount = 0;
    cCount = 0;
    gCount = 0
    for head, seq in FastAreader('').readFasta():  # iterates through all the sequences within the Fasta
        processedSeq = Calculations()
        seqList.append(seq)
        aCount += seq.count("A");
        tCount += seq.count("T");
        cCount += seq.count("C");
        gCount += seq.count("G")
    processedSeq.createNull(aCount, tCount, cCount, gCount,
                            myCommandLine.args.pseudoCount)  # Determines the Null Model given the counts of nucleotides within the sequences
    allEntropy = [];
    allConsensus = []
    for i in range(
            myCommandLine.args.iterations):  # Iterates through the number of user provided user iterations and outputs the relative entropy score along with its corresponding consensus
        oldMotifList = processedSeq.randomMotif(seqList,
                                                myCommandLine.args.kmerLength)  # Creates the initial motif list using the random motif generator
        processedSeq.createProfile(oldMotifList, myCommandLine.args.kmerLength, myCommandLine.args.pseudoCount)
        newMotifList = processedSeq.iterMotifs(seqList, myCommandLine.args.kmerLength)
        while oldMotifList != newMotifList:  # Determines the best motif list which is attained with the new and old motif list are the same
            oldMotifList = newMotifList  # Saves the last motif list to the oldMotifList
            profile = processedSeq.createProfile(oldMotifList, myCommandLine.args.kmerLength,
                                                 myCommandLine.args.pseudoCount)  # Finds the profile of the last motif list
            newMotifList = processedSeq.iterMotifs(seqList,
                                                   myCommandLine.args.kmerLength)  # Saves the motif list to a newMotifList to compare
        consensus = []
        for i in range(
                myCommandLine.args.kmerLength):  # Iterates through the length of the kmer and determines the consensus sequence
            aVal = profile[0][i];
            tVal = profile[1][i];
            cVal = profile[2][i];
            gVal = profile[3][i]  # Places the number of nucleotides to a variable
            maxNuc = ([aVal, tVal, cVal, gVal]).index(
                max([aVal, tVal, cVal, gVal]))  # Determines which nucleotide was in the highest frequence
            if maxNuc == 0:
                nucVal = "A"
            elif maxNuc == 1:
                nucVal = "T"
            elif maxNuc == 2:
                nucVal = "C"
            elif maxNuc == 3:
                nucVal = "G"
            consensus.append(nucVal)  # Appends the nucleotide to the consensus
        entropyScore = processedSeq.relativeEntropy(profile,
                                                    consensus)  # Determines the relative entropy score with the profile and consensus
        allConsensus.append(consensus)  # Appends the consenses to a list of consensus's
        allEntropy.append(entropyScore)  # Appends the entropy score to a list of entropy's
    finalEntropy = max(allEntropy)  # Finds the highest entrpy score
    finalConsensus = "".join(allConsensus[allEntropy.index(
        finalEntropy)])  # Consolidated the nucleotides within the consenses into one string
    print(str(finalConsensus) + "   " + str(
        finalEntropy))  # Prints the consensus and it's entropy score to the output file

if __name__ == "__main__":
    main()
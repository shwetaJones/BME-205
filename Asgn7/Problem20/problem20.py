class problemTwenty():
    def __init__(self, seq1, seq2, values, transitions, emissions):
        """Description: Initializes variables as self to be accessed by other methods """
        """Input: The input is the 2 sequences and matrix in the input file """
        """Output: There is no output """
        self.seq1 = seq1
        self.seq2 = seq2
        self.values = values
        self.counts = {}
        for i in transitions:
            for j in emissions:
                self.counts[j + i] = 0 #initializes every combination to 0

    def determineCounts(self):
        """Description: This method finds all the combinations """
        """Input: There is no input for this method, uses self """
        """Output: The counts is updated """
        for i in range(len(self.seq1)):
            slice = self.seq1[i] + self.seq2[i] #combines into one string
            for key in self.counts.keys(): #checks to see if it is in the dictionary
                if slice == key:
                    self.counts[key] += 1 #adds to the count dictionary

    def calcProbability(self):
        """Description: Determines the conditional probability """
        """Input: There is no input for this method, uses self """
        """Output: The output is the conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π. """
        total = 1
        for key in self.counts: #iterates through the count dictionary
            total *= (self.values[key] ** self.counts[key]) #calculates the conditional probability
        return total

def main(inFile):
    """Description: The main reads in the input file and prints out the conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π."""
    """Input: The input file contains string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission)"""
    """Output: It returns the conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π"""
    file = open(inFile, "r")
    lines = file.readlines()
    input = [(line.strip()) for line in lines]
    seq1 = input[0]
    emissions = input[2].strip().split()
    seq2 = input[4]
    transitions = input[6].strip().split()
    matrixLines = []
    for i in range(9, len(input)):
        matrixLines.append([str(x) for x in input[i].rstrip().split() if type(x) == str]) #appends each matrix line to a dictionary
    matrix = {}
    for i in range(len(transitions)):
        for j in range(len(emissions)):
            matrix[emissions[j] + transitions[i]] = float(matrixLines[i][j + 1]) #saves each probability to its correpsonding combination
    processed = problemTwenty(seq1, seq2, matrix, transitions, emissions)
    processed.determineCounts()
    print(processed.calcProbability())
    outfile = open("Jones_Shweta_problem20.out.txt", "w")
    outfile.write(str(processed.calcProbability()))
    outfile.close()

if __name__ == "__main__":
    main("rosalind_ba10b.txt")
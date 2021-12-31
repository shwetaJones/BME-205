class problemNineteen():
    def __init__(self, matrix, line, transitions):
        """Description: Initializes variables as self to be accessed by other methods """
        """Input: The input is the matrix and line from the input file """
        """Output: There is no output """
        self.matrix = matrix
        self.line = line
        self.counts = {}
        for i in transitions:
            for j in transitions:
                self.counts[i + j] = 0

    def determineCounts(self):
        """Description: This method updates the counts of kmers in the path """
        """Input: There is no input for this method, uses self """
        """Output: The sounts is updated, nothing is returned """
        for i in range(0, len(self.line)-1): #finds all the two-mers
            slice = self.line[i:i+2]
            for key in self.matrix.keys():
                if slice == key: #checks to see if the two-mer is valid/in the keys
                    self.counts[key] += 1 #adds to the count of the two-mer

    def calcProbability(self):
        """Description: This method determines the probability """
        """Input: There is no input for this method, uses self """
        """Output: The probability of the given path is returned """
        total = 1
        for key in self.counts:
            total *= (self.matrix[key]**self.counts[key]) #determines the probability using matrix and counts
        return (total*0.5)

def main(inFile):
    """Description: The main uses the input file to determine sna print the probability of the given path in the input file"""
    """Input: The input file contains a hidden path and its corresponding transition matrix """
    """Output: The method returns the probability ot the hidden path """
    file = open(inFile, "r")
    lines = file.readlines()
    input = [(line.strip()) for line in lines]
    line = input[0]
    transitions = input[2].strip().split()
    matrixLines = []
    for i in range(5, len(input)):
        matrixLines.append([str(x) for x in input[i].rstrip().split() if type(x) == str])
    matrix = {}
    for i in range(len(transitions)):
        for j in range(len(transitions)):
            matrix[transitions[i]+transitions[j]] = float(matrixLines[i][j+1])
    processed = problemNineteen(matrix, line, transitions)
    processed.determineCounts()
    print(processed.calcProbability())
    outfile = open("Jones_Shweta_problem19.out.txt", "w")
    outfile.write(str(processed.calcProbability()))
    outfile.close()

if __name__ == "__main__":
    main("rosalind_ba10a.txt")
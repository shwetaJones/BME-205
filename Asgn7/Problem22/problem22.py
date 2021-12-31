import numpy as np
class problemTwentyTwo():
    def __init__(self, emString, transitions, emissions, tMatrix, eMatrix):
        """Description: Initializes variables as self to be accessed by other methods """
        """Input: The input for this are the emission string, transitions, emissions, transition matrix, and emission matrix"""
        """Output: There is no output for this method"""
        self.emString = emString
        self.transitions = transitions
        self.emissions = emissions
        self.tMatrix = tMatrix
        self.eMatrix = eMatrix
    
    def determineProbability(self):
        """Description: This method calculated the probability that the HMM emits x """
        """Input: There is no input for this method, uses self """
        """Output: The output is the probability """
        indexList = [self.emissions.index(emission) for emission in self.emString] #creates a list of the indexes of all the emissions

        tProbs = np.zeros((len(self.transitions),len(indexList))) #initialized the matrix of transition probabilties
        for i in range(len(self.transitions)):
            tProbs[i][0] = (1/len(self.transitions))*self.eMatrix[i][indexList[0]] #initializes the values for the transition paths

        for i in range(1,len(indexList),1):
            for j in range(len(self.transitions)):
                tProbs[j][i] = sum(self.eMatrix[j][indexList[i]]*tProbs[k][i-1]*self.tMatrix[k][j] for k in range(len(self.transitions))) #determines the probabilties and saves it into the matrix

        totalProb = 0
        for i in range(len(self.transitions)):
            totalProb += tProbs[i][-1] #goes through each probability and adds it together
        return totalProb #returns the probability

def main(inFile):
    """Description: The main recieves the input file and prints out the probability """
    """Input: The input file contains a string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission)."""
    """Output: The method orints and saves the probability Pr(x) that the HMM emits x """
    file = open(inFile, "r")
    lines = file.readlines()
    input = [(line.strip()) for line in lines]

    emString = input[0].strip()
    emissions = input[2].strip().split()
    transitions = input[4].strip().split()

    tMatrix = np.array([input[7 + i].split()[1:] for i in range(len(transitions))], float) #saves the values into a transition matrix
    eMatrix = np.array([input[(7 + len(transitions) + 2) + i].split()[1:] for i in range(len(transitions))], float) #saves the values into the emission matrix

    processed = problemTwentyTwo(emString, transitions, emissions, tMatrix, eMatrix)
    print(processed.determineProbability())
    outfile = open("Jones_Shweta_problem22.out.txt", "w")
    outfile.write(str(processed.determineProbability()))
    outfile.close()

if __name__ == '__main__':
    main('rosalind_ba10d.txt')
import numpy as np
class problemTwentyOne():
    def __init__(self, emString, eMatrix, tMatrix, tDict):
        """Description: Initializes variables as self to be accessed by other methods """
        """Input: The input included the emission string, transition matrix, emission matrix, and transition dictionary"""
        """Output: There is no output """
        self.emString = emString
        self.eMatrix = eMatrix
        self.tMatrix = tMatrix
        self.tDict = tDict

    def determinePath(self):
        """Description: The method determines the transition path given the values in the input file """
        """Input: There is no input for this method, uses self """
        """Output: The output is the path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π."""
        transitions = [[0 for i in range(len(self.tMatrix))] for j in range(len(self.emString))] #initializes the transitions matrix with 0's
        for i in range(len(self.tMatrix)):
            transitions[0][i] = self.eMatrix[i][self.emString[0]] + np.log(1 / len(self.tMatrix)) #updates the transitins matrix with the first 3 probabilities

        old = [[0 for i in range(len(self.tMatrix))] for j in range(len(self.emString))] #initializes the old matrix with 0's
        for i in range(1, len(self.emString)):
            for j in range(len(self.tMatrix)):
                state = [self.eMatrix[j][self.emString[i]] + self.tMatrix[k][j] + transitions[i - 1][k] for k in range(len(self.tMatrix))] #determines the probabilties
                old[i][j] = np.argmax(state) #places the probability value to the old matrix
                transitions[i][j] = state[np.argmax(state)] #app

        current = np.argmax(transitions[len(self.emString) - 1]) #sets the current state with the "last" state
        stateList = [np.argmax(transitions[len(self.emString) - 1])] #begins the list of states, basically the end state
        for i in range(len(self.emString) - 1, 0, -1): #goes backward
            current = old[i][current]
            stateList.insert(0, current) #inserts the state to the beginning of the list of states

        path = []
        for state in stateList: #iterates through the generates list of states and joins them into a string to be returned to the main method
            path.append(''.join([self.tDict[state]]))
        return ("".join(path))

def main(inFile):
    """Description: The main uses an input file containing a path """
    """Input: The input is a file containing a string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission)"""
    """Output: The output is the conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π"""
    file = open(inFile, 'r')
    lines = [(line.strip()) for line in file.readlines()]
    emString = lines[0] #determines the emission string
    emissions = lines[2].strip().split() #determines the emissions
    transitions = lines[4].strip().split() #determines the transitions

    infile = open(inFile, 'r')
    values = infile.read().split()
    ind = [i for i in range(len(values)) if '--------' == values[i]] #finds all indices where the dashes occur
    tDict = {i: transitions[i] for i in range(len(transitions))} #creates a transition dictionary
    tMatrix = {i: {j: np.log(float(values[ind[2] + len(transitions) + 2 + i * (len(transitions) + 1) + j])) for j in range(len(transitions))} for i in range(len(transitions))} #creates the transition matrix
    eMatrix = {i: {emissions[j]: np.log(float(values[ind[3] + len(emissions) + 2 + i * (len(emissions) + 1) + j])) for j in range(len(emissions))} for i in range(len(transitions))} #creates the emission matrix

    processed = problemTwentyOne(emString, eMatrix, tMatrix, tDict)
    finalPath = processed.determinePath()
    print(finalPath)
    outfile = open("Jones_Shweta_problem21.out.txt", "w")
    outfile.write(str(finalPath))
    outfile.close()

if __name__ == '__main__':
    main("rosalind_ba10c.txt")
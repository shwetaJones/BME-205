class problemTwentyThree():
    def __init__(self, emissions, transmissions, eState, tState):
        """ Description: This method saves values as self to be accessed by other methods """
        """ Input: Takes in emissions, transmissions, eState, and tState to be saved as self """
        """ Output: No output """
        self.emissions = emissions
        self.transmissions = transmissions
        self.eState = eState
        self.tState = tState

    def matrix1(self):
        """ Description: Returns a matrix of transtion probabilities """
        """ Input: There is no input for this method, instead is uses values saved as self """
        """ Output: This method returns the transition probabilities matrix """
        combCount = {}
        for i in range(0, len(self.transmissions)-1): #iterates through the transmissions to keep a count of the occurences of two-mers
            if self.transmissions[i:i+2] in combCount:
                combCount[self.transmissions[i:i+2]] += 1
            else:
                combCount[self.transmissions[i:i+2]] = 1
        initMatrix = {};finalMatrix = {}
        for i in self.tState: #iterates through the transmissions
            initMatrix[i] = []
            for j in self.tState: #iterates through the transmissions
                if i + j in combCount: #checks to see if it exists in the dictionary
                    initMatrix[i].append(combCount[i + j])
                else:
                    initMatrix[i].append(0)
            finalMatrix[i] = []
            sumTrans = sum(initMatrix[i]) #determines the sum for each row
            for j in range(len(self.tState)):
                if sumTrans != 0:
                    finalMatrix[i].append(int(initMatrix[i][j]) / sumTrans)
                else: #accounts for when the transition doesn't exist
                    finalMatrix[i].append(1 / len(self.tState))
        return finalMatrix

    def matrix2(self):
        """ Description: Returns a matrix of emission probabilties """
        """ Input: There is no input for this method, instead is uses values saved as self """
        """ Output: This method returns the emission probabilities matrix """
        combCount = {}
        for i in range(len(self.emissions)): #iterates through the transmissions to keep a count of the occurences of two-mers
            combination = self.transmissions[i] + self.emissions[i]
            if combination in combCount:
                combCount[combination] += 1
            else:
                combCount[combination] = 1
        initMatrix = {}; finalMatrix = {}
        for i in self.tState: #iterates through the transmissions
            initMatrix[i] = []
            for j in self.eState: #iterates through the emissions
                if i+j in combCount: #checks to see if it exists in the dictionary
                    initMatrix[i].append(combCount[i+j])
                else:
                    initMatrix[i].append(0)
            finalMatrix[i] = []
            sumTrans = sum(initMatrix[i]) #determines the sum for each row
            for j in range(len(self.eState)):
                if sumTrans != 0:
                    finalMatrix[i].append(int(initMatrix[i][j])/sumTrans)
                else: #accounts for when the transition doesn't exist
                    finalMatrix[i].append(1/len(self.tState))
        return finalMatrix

def main(inFile):
    """ Description: The main reads in the input file and outputs the matrix in the expected format """
    """ Input: The input is the input file """
    """ Output: The output is matrices printed out in the correct format """
    file = open(inFile, 'r')
    data = file.read().strip().split("\n")
    emissions = data[0]
    eState = data[2].split()
    transmissions = data[4]
    tState = data[6].split()
    processed = problemTwentyThree(emissions, transmissions, eState, tState)
    matrix1 = processed.matrix1()
    matrix2 = processed.matrix2()
    print(data[6])
    for i in matrix1:
        print(i + " " + str(" ".join([str(i) for i in matrix1[i]]))) #prints out the key, and the transmission probabilties associated with it
    print("--------")
    print ("    " + data[2])
    for i in matrix2:
        print(i + " " + str(" ".join([str(i) for i in matrix2[i]]))) #prints out the key, and the emission probabilties associated with it

if __name__ == "__main__":
    main("rosalind_ba10h.txt")
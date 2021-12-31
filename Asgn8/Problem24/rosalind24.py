import numpy as np
class problemTwentyFour:
    def __init__(self, x, transition, emission, emissionList, stateList):
        """ Description: This saves vairables as self to be accessible by other methods in the class"""
        """ Input: The input is the x, transition, emission, emissionList, and stateList"""
        """ Output: There is no output for this method """
        self.x = x
        self.transition = transition
        self.emission = emission
        self.emissionList = emissionList
        self.stateList = stateList

    def softDecode(self):
        """ Description: This method creates all the probabilities """
        """ Input: There is no input, rather it uses the variables saved as self """
        """ Output: The output is the probabilities"""
        n = len(self.x)
        l = self.transition.shape[0]
        x2ind = {}
        for i in range(len(self.emissionList)): #associates each of the emissions with value
            x2ind[self.emissionList[i]] = i
        xList = []
        for i in range(len(self.x)): #locates each of the emissions within the x string
            xList.append(x2ind[self.x[i]])

        # Performs forward algorithm to get probabilities
        forward = [[0 for i in range(l)] for ii in range(n)]
        for k in range(l):
            forward[0][k] = self.emission[k, xList[0]] / l
        for i in range(1, n):
            for j in range(l):
                forward[i][j] = sum([forward[i - 1][val] * self.transition[val, j] * self.emission[j, xList[i]] for val in range(l)])

        # Performs backward algorithm to get probabilities
        backward = [[0 for i in range(l)] for ii in range(n)]
        for k in range(l):
            backward[n - 1][k] = 1
        for i in range(n - 2, -1, -1):
            for j in range(l):
                backward[i][j] = sum([backward[i + 1][val] * self.transition[j, val] * self.emission[val, xList[i + 1]] for val in range(l)])

        probabilities = np.zeros((n, l), dtype=float) #initializes the probabilities matrix with 0's
        for i in range(n):
            for k in range(l):
                probabilities[i, k] = forward[i][k] * backward[i][k] / sum(forward[n - 1]) #fills up the probabilties matrix with values from the backward and forward algorithm
        return probabilities

def main(inFile):
    """ Description: The main uses the input file to create a set of probabilities for the given file """
    """ Input: The input is a string x, alphabet, states, transition matrix, and emission matrix """
    """ Output: The output is a set of all the probabilities in the expected format """
    f = open(inFile, 'r')
    data = f.read().strip().split()
    x = data[0]
    ind = [i for i in range(len(data)) if '--------' == data[i]]
    emissionList = data[ind[0] + 1:ind[1]]
    stateList = data[ind[1] + 1:ind[2]]
    transition = np.zeros((len(stateList), len(stateList)), dtype=float) #initializes the transition matrix
    emission = np.zeros((len(stateList), len(emissionList )), dtype=float) #initializes the emission matrix
    for i in range(len(stateList)):
        transition[i, :] = [float(d) for d in data[ind[2] + len(stateList) + 2 + i * (len(stateList) + 1):ind[2] + len(stateList) + 1 + (i + 1) * (len(stateList) + 1)]] #fills up the transition matrix
        emission[i, :] = [float(d) for d in data[ind[3] + len(emissionList) + 2 + i * (len(emissionList ) + 1):ind[3] + len(emissionList ) + 1 + (i + 1) * (len(emissionList ) + 1)]] #fills up the emission matrix
    processed = problemTwentyFour(x, transition, emission, emissionList, stateList)
    probabilities = processed.softDecode()
    print(' '.join(stateList))
    for i in range(probabilities.shape[0]):
        print(' '.join(list(map(str, probabilities[i, :])))) #formats the probabilities in the appropriate manner

if __name__ == '__main__':
    main("rosalind_ba10j.txt")
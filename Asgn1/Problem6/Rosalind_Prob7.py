import sys
class Problemsix():

    def __init__ (self, words):
        self.words = words

    def printCounts (self):
        counts = dict()
        for word in self.words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        for count in counts:
            print (count, counts[count])

def main ():
    readLine = open(sys.argv[1], "r")
    line = readLine.read()
    words = line.split()
    values = Problemsix(words)
    values.printCounts()

if __name__== "__main__":
    main()

# readLine = open("rosalind_ini6.txt", "r")
# line = readLine.read()
# words = line.split()
# counts = dict()
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
# for count in counts:
#     print (count, counts[count])
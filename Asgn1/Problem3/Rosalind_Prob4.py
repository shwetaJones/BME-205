import sys
class Problemfour():

    def __init__ (self, dna):
        self.dna = dna

    def acount (self):
        return (self.dna.count('A'))

    def ccount (self):
        return (self.dna.count('C'))

    def gcount (self):
        return (self.dna.count('G'))

    def tcount (self):
        return (self.dna.count('T'))

def main ():
    with open(sys.argv[1], "r") as file:
        dna = file.read()
    wholedna = Problemfour (dna)
    print (wholedna.acount(), wholedna.ccount(), wholedna.gcount(), wholedna.tcount())

if __name__== "__main__":
    main()

# file = open ("rosalind_dna.txt", "r")
# dna = file.read()
# numA = dna.count('A')
# numT = dna.count('T')
# numC = dna.count('C')
# numG = dna.count('G')
# print ("{0} {1} {2} {3}\n".format(numA, numC, numG, numT))


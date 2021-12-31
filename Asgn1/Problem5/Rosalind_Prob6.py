import sys
class Problemsix():

    def __init__ (self, readLine):
        self.readLine = readLine

    def printLine (self):
        count = 0
        for line in self.readLine:
            count += 1
            if count%2 == 0:
                print(line)

def main ():
    readLine = open(sys.argv[1], "r")
    file = Problemsix(readLine)
    file.printLine()

if __name__== "__main__":
    main()

# readLine = open("rosalind_ini5.txt", "r")
# count = 0
# for line in readLine:
#     count +=1
#     if count%2 == 0:
#         print(line)
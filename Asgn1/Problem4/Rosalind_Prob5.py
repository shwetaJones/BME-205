import sys
class Problemfive():

    def __init__ (self, line):
        self.line = line
        self.val1 = int(line.split()[0])
        self.val2 = int(line.split()[1])

    def total (self):
        total = 0
        for i in range(self.val1, self.val2):
            if i % 2 == 1:
                total += i
        return total

def main ():
    with open(sys.argv[1], "r") as file:
        line = file.read()
    processedLine = Problemfive(line)
    print (processedLine.total())

if __name__== "__main__":
    main()

# readLine = open("rosalind_ini4.txt", "r")
# line = readLine.read()
# val1 = int(line.split()[0])
# val2 = int(line.split()[1])
# total = 0
# for i in range(val1, val2):
#     if i%2 == 1:
#         total += i
# print(total)
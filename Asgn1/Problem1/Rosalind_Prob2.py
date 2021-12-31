import sys
class Problemtwo():

    def __init__ (self, values):
        self.val1 = int(values.split()[0])
        self.val2 = int(values.split()[1])

    def hypotenuse (self):
        return ((self.val1**2) + (self.val2**2))

def main ():
    with open(sys.argv[1], "r") as file:
        values = file.read()
    val = Problemtwo (values)
    print (val.hypotenuse())

if __name__== "__main__":
    main()

# readLine = open("rosalind_ini2.txt", "r")
# line = readLine.read()
# val1 = int(line.split()[0])
# val2 = int(line.split()[1])
# hyp = (val1**2) + (val2**2)
# print(hyp)
# Problem 1 - Getting Python
# Problem 2 - Counting DNA Nucleotides
file = open ("rosalind_dna.txt", "r")
dna = file.read()
numA = dna.count('A')
numT = dna.count('T')
numC = dna.count('C')
numG = dna.count('G')
print ("{0} {1} {2} {3}\n".format(numA, numC, numG, numT))

# Problem 3 - Variables and Some Arithmetic
readLine = open("rosalind_ini2.txt", "r")
line = readLine.read()
val1 = int(line.split()[0])
val2 = int(line.split()[1])
hyp = (val1**2) + (val2**2)
print(hyp)

# Problem 4 - Strings and Lists
openFile = open("rosalind_ini3.txt", "r")
line = openFile.read()
nums = openFile.read()
a = int(nums [0])
b = int(nums [1])
c = int(nums [2])
d = int(nums [3])
print (line[a:b+1], line[c:d+1])

# Problem 5 - Conditions and Loops
readLine = open("rosalind_ini4.txt", "r")
line = readLine.read()
val1 = int(line.split()[0])
val2 = int(line.split()[1])
total = 0
for i in range(val1, val2):
    if i%2 == 1:
        total += i
print(total)

# Problem 6 - Working with Files
readLine = open("rosalind_ini5.txt", "r")
count = 0
for line in readLine:
    count +=1
    if count%2 == 0:
        print(line)

# Problem 7 - Dictionaries
readLine = open("rosalind_ini6.txt", "r")
line = readLine.read()
words = line.split()
counts = dict()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
for count in counts:
    print (count, counts[count])
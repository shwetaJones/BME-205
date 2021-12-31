# openFile = open("rosalind_ini3.txt", "r")
# line = openFile.read()
# nums = openFile.read()
# # line = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
# # nums = "22 27 97 102"
# # a = int(nums [0])
# # b = int(nums [1])
# # c = int(nums [2])
# # d = int(nums [3])
# a = 15
# b = 25
# c = 82
# d = 87
# print (line[a:b+1], line[c:d+1])

import sys
# class Problemthree():
#     def __init__ (self, line):
#         # self.num1 = int(line[1])
#         # self.num2 = int(line[2])
#         # self.num3 = int(line[3])
#         # self.num4 = int(line[4])
#         # self.nums = nums
#         self.line = line
#         print (self.line)
#         print(self.line[1])
#
#     def firstReturn (self):
#         return (self.line)
#         # return (self.line[self.num1:(self.num2 + 1)])
#
#     def secondReturn (self):
#         return (self.line)
#         # return (self.line[self.num3:(self.num4 + 1)])

def main ():
    with open(sys.argv[1], "r") as file:
        line = file.read()
        nums = file.read()
    print (line)
    print (nums)

        # nums = file.read()
    # val = Problemthree (line)
    # print (val.firstReturn(), val.secondReturn())

if __name__== "__main__":
    main()
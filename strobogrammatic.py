
#A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees.
#For example, 16891 is strobogrammatic.

#Create a program that finds all strobogrammatic numbers with N digits.

import math

valid_nums = [1, 6, 8, 9, 0]

valid_nums_mid = [1, 8, 0]

valid_nums_first = [1, 6, 8, 9]

def get_symmetric_num(n):
    if n == 6:
        return 9
    if n == 9:
        return 6
    return n

def find_strobogrammatic(n):

    strlist = []
    for i in range(math.floor(n/2)):
        currlist = []
        if i == 0:
            for num in valid_nums_first:
                currlist.append(str(num))
        else:
            for num in valid_nums:
                for s in strlist:
                    currlist.append(s + str(num))
        strlist = currlist

    if (n % 2) != 0:
        currlist = []
        if n == 1:
            for num in valid_nums_mid:
                currlist.append(str(num))
        else:
            for num in valid_nums_mid:
                for s in strlist:
                    currlist.append(s + str(num))
        strlist = currlist


    for i in reversed(range(math.floor(n/2))):
        currlist = []
        for s in strlist:
            sym_num = get_symmetric_num(int(s[i]))
            s = s + str(sym_num)
            currlist.append(s)
        strlist = currlist

    return strlist

stro = find_strobogrammatic(4)
print(stro)
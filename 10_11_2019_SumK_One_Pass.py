
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


import math


a = [2, -2, 10, 5, 8, 1, 18]
k = 16

index_dict = {}

for x in a:
    diff = k - x
    if x in index_dict.keys():
        print("True")
    else:
        index_dict[diff] = 1

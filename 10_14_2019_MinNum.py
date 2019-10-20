#Given an array of integers, find the first missing positive integer in linear time and constant space.
#In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
#negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.

import math

a = [10, 11, 8, -1, 11, 90, 1, 3]
i = 0
j = len(a) - 1

while i < j:
    if a[i] < 1 or a[i] > len(a):
        if a[j] < 1 or a[j] > len(a):
           j = j - 1
        else:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i = i + 1
            j = j - 1
    else:
        i = i + 1

k = 0
while k < i:
    index = abs(a[k]) - 1
    a[index] = -1 * abs(a[index])
    k = k + 1

print(a)

k = 0

min_value = i
while k < i:
    if a[k] > 0:
        min_value = k
    k = k + 1

print (min_value + 1)
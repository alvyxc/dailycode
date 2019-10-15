
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


import math

found = False

def merge(arr, l, m, r):

    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i = 0        # Initial index of first subarray
    j = 0        # Initial index of second subarray
    k = l        # Initial index of merged subarray

    while i < len(L) and j < len(R) :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return arr

def findK(arr, l, m, r, k):

    low_index = l
    high_index = r

    while low_index <= m and high_index >= m:
        sum = arr[low_index] + arr[high_index]

        if sum == k:
            return [arr[low_index], arr[high_index]]
        elif sum < k:
            low_index = low_index+1
        else:
            high_index = high_index-1
    return []


def mergeSortFind(arr,l,r, k):
    global found
    if l < r:

        m = math.floor((l+r)/2)

        # Sort first and second halves
        mergeSortFind(arr, l, m, k)
        mergeSortFind(arr, m+1, r, k)
        if not found:
            merge(arr, l, m, r)
            found_values = findK(arr, l, m, r, k)
            if found_values :
                found = True
                print(found_values)

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
k = 11

mergeSortFind(arr,0,n-1, k)

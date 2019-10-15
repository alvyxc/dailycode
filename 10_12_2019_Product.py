#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?


array = [1, 2, 3, 4, 5]

product_array = [1] * len(array)

i = 0
left_product = 1
while i < len(array):
    product_array[i] = left_product
    left_product = left_product * array[i]
    i = i + 1

i = len(array) - 1
right_product = 1
while i >= 0:
    product_array[i] = product_array[i] * right_product
    right_product = right_product * array[i]
    i = i - 1

print(product_array)
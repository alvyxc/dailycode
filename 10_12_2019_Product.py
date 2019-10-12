
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
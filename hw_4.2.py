from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)
numbers = [8, 2, 3, -1, 7]
result = multiply_list(numbers)
print(result)
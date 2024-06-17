def is_armstrong(number):
    # Convert the number to a string to iterate over each digit
    digits = str(number)
    # Create a generator expression for the sum of the cubes of its digits
    armstrong_sum = sum(int(digit) ** 3 for digit in digits)
    # Check if the sum of the cubes of the digits is equal to the number itself
    return armstrong_sum == number

# Test the function with a few examples
numbers_to_test = [153, 370, 371, 407, 123, 9474,3333]

for num in numbers_to_test:
    result = "is" if is_armstrong(num) else "is not"
    print(f"{num} {result} an Armstrong number.")
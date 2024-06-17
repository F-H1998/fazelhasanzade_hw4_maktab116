def is_armstrong(number):

    digits = str(number)
    armstrong_sum = sum(int(digit) ** 3 for digit in digits)
    return armstrong_sum == number
numbers_to_test = [153, 370, 371, 407, 123, 9474,3333]

for num in numbers_to_test:
    result = "is" if is_armstrong(num) else "is not"
    print(f"{num} {result} an Armstrong number.")

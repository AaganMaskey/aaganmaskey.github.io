def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)
num = int(input('Enter number '))
print(f'The factorial of {num} is {fact(num)}')
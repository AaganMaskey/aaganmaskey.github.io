def is_prime(num):
    if num % 2 == 0:
        return False
    elif num == 3 or num == 2:
        return True
    else:
        i = 3
        while i < num:
            if num % i == 0:
                return False
            else:
                return True

takeNumber = int(input("Enter any number \n"))
print(is_prime(takeNumber))
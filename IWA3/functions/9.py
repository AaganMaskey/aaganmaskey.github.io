def prime(num):
    i = 3
    if num % 2 == 0:
        print(f'{num} is NOT PRIME \n')
    elif num == 3:
        print(f'{num} is PRIME \n')
    else:
        while (i < num):
            if num % i == 0:
                print(f'{num} NOT PRIME \n')
                break
            else:
                print(f'{num} is PRIME \n')
                break
            i += 2
getNum = int(input("Enter any number \n"))
prime(getNum)
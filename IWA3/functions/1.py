def threeNumbers(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
maxNum = threeNumbers(55,66,1000)
print('The max of given numbers is:', maxNum)
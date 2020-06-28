def list(getList):
    sum = 0
    for i in getList:
        sum += i
    return sum
userList = [12,43,23,65,75]
print("The sum is of given list is", list(userList))
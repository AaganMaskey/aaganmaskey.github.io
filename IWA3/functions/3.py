def list(getList):
    product = 1
    for i in getList:
        product *= i
    return product
userList = [9,2,-1]
print("The product is of given list is", list(userList))
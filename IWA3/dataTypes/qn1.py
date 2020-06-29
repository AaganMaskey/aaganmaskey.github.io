getInput = input("Enter the string \n")
dict = {}
for n in getInput:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)

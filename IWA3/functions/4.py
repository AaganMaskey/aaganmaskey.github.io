def reverseString(string):
    return string[::-1]
inputString = input ("Enter the word to reverse \n")
print("The string BEFORE reverse is", inputString)
reversedString = reverseString(inputString)
print("The string AFTER reverse is", reversedString)

num = input("Enter the number list separated by an empty space \n")
number_list = num.split()
product = 1
for number in number_list:
    product = product * int(number)
print(f"The product of given list is {product} \n")
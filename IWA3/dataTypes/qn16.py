num = input("Enter the number list separated by an empty space \n")
number_list = num.split()
number_sum = 0
for number in number_list:
    number_sum = number_sum + int(number)
print(f"The sum of given list is {number_sum} \n")
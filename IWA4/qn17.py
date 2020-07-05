a = int(input("Enter the FIRST NUMBER \n"))
b = int(input("Enter the SECOND NUMBER \n"))
oper = input("Enter the MATHEMATICAL OPERATORS  (+, -, *): ")
if oper == "+":
    print(f"The sum of {a} and {b} is {a+b}")
elif oper == "-":
    print(f"The difference of {a} and {b} is {(a-b)}")
elif oper == "*":
    print(f"The product of {a} and {b} is {a*b}")
else:
    print("The operator IS NOT SUPPORTED \n")
dic = {"Full Name": "Hari Bahadur", "Salary": 15000, "Post": "Staff"}
print(dic)
key = input("Enter the key to be deleted")
if key in dic:
   del dic[key]
print(dic)
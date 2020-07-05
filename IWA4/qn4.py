male = ['John','Rock','Michael','Henry','James']
print(f"The list of male is {male}")
print(f"The ID of male is {id(male)}")
female = ['Jesicca, Jenny, Emma, Lauren, Charlotte']
print(f"The list TO APPEND is {female}")
print(f"The ID of female is {id(female)}")
male.extend(female)
print(f"The APPENDED list of male is {male}")
if id(male) == id(female):
    print ("The ID HAS NOT CHANGED")
else:
    print ("The ID HAS CHANGED")
sorted(male)
print(f"The SORTED list is {sorted(male)}")
print(f"The FIRST item on the list is {male[0]}")
print(f"The SECOND item on the list is {male[1]}")
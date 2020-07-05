people = []
people1=('Ram','Sharma',45)
people.append(people1)
people2=('Hari','Nepal',35)
people.append(people2)
people3 = ("Shyam","Bahadur",25)
people.append(people3)
print(f"The APPENDED LIST {people}")
people.sort(key = lambda x: x[2])

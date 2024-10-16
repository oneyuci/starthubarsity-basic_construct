my_tuple = (1, 2, 3)
my_tuple = (3,4,5)

print(my_tuple)

number = {"joy", "samuel", "joy", "amos"}
print(number)

number2 = {10, 4, 5, 3, 10, 2, 4}
print(number2)

number2.add(7)
print(number2)

number2.remove(5)
print(number2)

number3 = number.union(number2)
print(number3)

number4 = number.intersection(number2)
print(number4)

number5 = number.difference(number2)
print(number5)

person = {"Name": "John",
          "Age" : 00,
          "Email": "Sunychuks223@gmail.com"}
person2 = person["Name"]
print(person2)

person3 = person["Age"]
print(person3)

person4 = person["Email"]
print(person4)

person["Name"] = "Yuci"
person["Age"] = 11
person["Email"] = "Nill"
print(person)

person["Gender"] = "Male"
print(person)

person.pop("Name")
print(person)



mov_list = ["Money Heist", "Prison Break", "Nikita", "Game of Thrones"]
mov_list.insert(2,"Into the Badlands")
del mov_list[0]
print(mov_list)

stu_dic = {"Name": "Paul", "Name2:": "Jude" , "Grade_Paul": "A+", "Grade_Jude": "A-" }
stu_dic["Grade_Jude"] = "B+"

stu_dic["Name3"] = "Gift"

print(stu_dic)


my_set = {"Logic", "is" , "a", "science", "of", "correct", "reasoning.", "Reasonable", "chat", "is", "organised", "in", "a", "well", "order.", "I.e", "Syatematic", "and", "organized", "order"}
my_set2 = " ".join(my_set)
print(my_set2)
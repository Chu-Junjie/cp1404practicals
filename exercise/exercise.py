# 1
# filename = input("Enter the filename: ")
# file = open(filename, 'r')
#
# for line in file:
#     if line.startswith("#"):
#         print(line.strip())
#
# file.close()

# 2
# s = "\tPython,Monty \n"
# print(s[1],".",sep="")
# print(s.strip(),".",sep="")
# print(s.lstrip(),".",sep="")
# print(s.strip().split())
# s = s.replace('','*')
# print(s)

# 3
# names = ["Cliff", "Lukas", "Lea"]
#
# for i in range(len(names)):
#     with open(f"{names[i]}.txt", "w") as out_file:
#         print(f"{i + 1}{names[i]}", file=out_file)

# 4
# FILENAME = "name.txt"
#
# with open("name.txt", "r") as in_file:
#     lines = in_file.readlines()
#
# print(lines)
#
# for i in range(0,len(lines),2):
#     name = lines[i].strip()
#     country = lines[i + 1].strip()
#     print(f"{name} was born in {country}")

# 5
# names = ["Ada","Alan","Bill","John"]
# print(",".join(names))
# name_to_remove = input("Who do you want to remove: ")
#
# while name_to_remove != "":
#     try:
#         names.remove(name_to_remove)
#     except ValueError:
#         print(f"{name_to_remove} was not found in the list.")
#     print("Name left:",",".join(names))
#     name_to_remove = input("Who do you want to remove: ")

# 6
# data = [['Derek,7'],]

# 7
# name_and_age = {"lukas": 21, "Bill": 61}
# name_and_age["lukas"] = 20
# print(name_and_age)

# 8

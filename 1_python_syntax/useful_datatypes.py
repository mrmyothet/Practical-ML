name_list = []

name = input("What is your name? ").lower()

while name != "wai":
    name_list.append(name)
    name = input("What is your name? ").lower()

print(name_list)

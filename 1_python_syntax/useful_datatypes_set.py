name_list = set()
name = input("What is your name? ").lower()

while name != "wai":
    name_list.add(name)
    name = input("What is your name? ").lower()
print(name_list)

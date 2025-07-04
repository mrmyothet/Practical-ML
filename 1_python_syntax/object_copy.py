import os
from dotenv import load_dotenv


class MyObject:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __repr__(self):
        load_dotenv()
        ML_Summer_School_ID = os.getenv("ML_Summer_School_ID")
        return f"{ML_Summer_School_ID} (name='{self.name}', data={self.data})"
    

obj1 = MyObject("Parent", [10, 20])
obj2 = MyObject("Child", [obj1])


print(f" obj1: {obj2}")
print(f" obj2: {obj2}")

obj1.data[0] = 100
print(f" obj2: {obj2}")

# Deep copy
print("\nDeep copy example:")

import copy

obj1 = MyObject("Parent", [10, 20])
obj2 = MyObject("Child", [copy.deepcopy(obj1)])


print(f" obj1: {obj2}")
print(f" obj2: {obj2}")

obj1.data[0] = 100
print(f" obj2: {obj2}")
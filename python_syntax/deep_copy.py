original_list = [1, 2, [3, 4]]

copy_list = original_list

print(f"original_list: {original_list}")
print(f"copy_list: {copy_list}")

copy_list[2][0] = 99
print(f"original_list: {original_list}")
print(f"copy_list: {copy_list}")

# Deep copy 

import copy

original_list = [1, 2, [3, 4]]
copy_list = copy.deepcopy(original_list)

print(f"original_list: {original_list}")
print(f"deepcopy_list: {copy_list}")

copy_list[2][0] = 99
print(f"original_list: {original_list}")
print(f"deepcopy_list: {copy_list}")
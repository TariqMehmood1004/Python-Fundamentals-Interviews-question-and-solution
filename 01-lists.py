# 1. Creating a list
lists = [1, 2, 3, 4, "Python", True]
print(lists)    # [1, 2, 3, 4, 'Python', True]

# # Accessing elements by indexing
print(lists[0]) # 1
print(lists[1]) # 2
print(lists[2]) # 3
print(lists[3]) # 4
print(lists[4]) # Python
print(lists[5]) # True
print(lists[-1]) # Accessing very last value

# =======================

# Modifying an element
lists[0] = 100
print(lists) # [100, 2, 3, 4, 'Python', True]

# =======================

# Appending an elements/values to the lists
lists.append(500)
print(lists) # [100, 2, 3, 4, 'Python', True, 500]

# =======================

# Removing an element
lists.remove(100)
print(lists) # [2, 3, 4, 'Python', True, 500]

# =======================

# List slicing
slices = lists[1:3]
print(slices) # [3, 4]

# Python program to illustrate the 
# difference between shallow and deep copy

import copy

class Car:
  def __init__(self, name, colors):
    # data members = parameters
    self.name = name
    self.colors = colors
    
# Create a Honda car object
HONDA_COLORS = ["Red", "Blue"]
HONDA_CAR = Car("Honda", HONDA_COLORS)

print(f"[HONDA CAR]: {HONDA_CAR}")
# [HONDA CAR]: <__main__.Car object at 0x000001C547427A10>

# ===============

# Deepcopy of Honda
DEEP_COPY_HONDA = copy.deepcopy(HONDA_CAR)
DEEP_COPY_HONDA.colors.append("Green")

print("[Deepcopy]:", DEEP_COPY_HONDA.colors)
# [Deepcopy]: ['Red', 'Blue', 'Green']

print("[Original]:", HONDA_CAR.colors)
# [Original]: ['Red', 'Blue']
# => does not change the original object

# ===============

# Shallow Copy of Honda
SHALOW_COPY_HONDA = copy.copy(HONDA_CAR)
SHALOW_COPY_HONDA.colors.append("Green")

print("[shalowCopy]:", SHALOW_COPY_HONDA.colors)
# [shalowCopy]: ['Red', 'Blue', 'Green']

print("[Original]:", SHALOW_COPY_HONDA.colors)
# [Original]: ['Red', 'Blue', 'Green']
# => has made changes in the original object

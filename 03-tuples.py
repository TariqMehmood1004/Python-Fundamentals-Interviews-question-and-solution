# Creating tuples
tuples = (1, 2, 3, 1, 2, 3, True, 'Tariq')

print(f"[TUPLES]: {tuples}")
# [TUPLES]: (1, 2, 3, 1, 2, 3, True, 'Tariq')

# =============

# Adding values/elements
# tuples.add(5)
# print(f"[ADD TUPLES]: {tuples}")
# AttributeError: 'tuple' object has no attribute 'add'

# ============

# Slicing the elements
sliced = tuples[1:3]
print(f"[SLICED TUPLES]: {sliced}")

# ============

# Accessing elements by indexing
for t in tuples:
    print(f"[ELEMENT]: {t}")
    
    """_output_
    [ELEMENT]: 1
    [ELEMENT]: 2
    [ELEMENT]: 3
    [ELEMENT]: 1
    [ELEMENT]: 2
    [ELEMENT]: 3
    [ELEMENT]: True
    [ELEMENT]: Tariq
    """
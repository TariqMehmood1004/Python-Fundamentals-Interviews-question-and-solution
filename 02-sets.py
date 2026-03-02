# Creating the sets
sets = {1, 2, 3, 4, 5,"Python", True, 5, 1} # automatically removes duplicates
print(f"[SETS]: {sets}")    # [SETS]: {1, 2, 3, 4, 5, 'Python'}

# ================

# Adding elements/values
sets.add(100)
sets.add(200)
print(f"[SETS]: {sets}")    # [SETS]: {1, 2, 3, 4, 5, 'Python', 100, 200}

# ================

# Removing elements/values
sets.remove(100)            # KeyError if the element is not present
print(f"[SETS]: {sets}")    # [SETS]: {1, 2, 3, 4, 5, 'Python', 200}

# ================

# Accessing elements/values (No indexing because it is unordered)
for s in sets:
    print(f"[ELEMENT]: {s}")

    """_output_
    [ELEMENT]: 1
    [ELEMENT]: 2
    [ELEMENT]: 3
    [ELEMENT]: 4
    [ELEMENT]: 5
    [ELEMENT]: 200
    [ELEMENT]: Python
    """
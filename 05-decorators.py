# Defining the decorator function
def logger(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper

# Applying decorator to the add() method
@logger
def add(a, b):
    return a + b

sum = add(2,3)
print(f"[SUM]: {sum}")

# Function called
# [SUM]: 5

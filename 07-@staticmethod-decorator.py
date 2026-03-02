# Creating a classmethod
class MyClass:
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def get_max_value(x, y):  # without self.
        return max(x, y)

# Creating an instance of MyClass
obj = MyClass(10)

# Calling the staticmethod
print(f"[STATIC METHOD]: {obj.get_max_value(20, 30)}")
# [STATIC METHOD]: 30
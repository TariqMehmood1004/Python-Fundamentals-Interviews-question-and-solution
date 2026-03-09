# Creating a classmethod
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def get_max_value(self):
        return self.value

# Creating an instance of MyClass
obj = MyClass(10)

# Calling the classmethod
print(f"[CLASS METHOD]: {obj.get_max_value()}")
# [CLASS METHOD]: 10
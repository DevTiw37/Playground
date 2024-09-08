class MyClass:
    def __init__(self):
        self.__private_var = 10

    def public_method(self):
        print(self.__private_var)

# Accessing the private attribute directly:
my_object = MyClass()
# print(my_object.__private_var)  # Raises AttributeError

# Accessing the private attribute indirectly:
# print(my_object._MyClass__private_var)  # Prints 10, but not recommended use this method

my_object.public_method() # Use this instead
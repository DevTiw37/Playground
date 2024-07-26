print(dir())
var = 1
print("Variable name var created")
print(dir())
def myfun():
    print("First",dir())
    var1 = 1
    print("Variable name var1 created")
    print("Second",dir())
print("Before calling the function")
print(dir())
print("After calling the function")
myfun()
print(dir())


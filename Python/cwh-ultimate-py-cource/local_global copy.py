x = 10
def my_fun():
    global y
    y = 10
    print(y)
my_fun()
print(y)
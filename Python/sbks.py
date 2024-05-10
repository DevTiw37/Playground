num = int(input("Enter a positive integer: "))
a,b = 0,1
print(a)
print(b)
if num <= 0:
    print("Enter positive integer")
else:
    for i in range(3,num+1):
        c = a + b
        print(c)
        a = b
        b = c
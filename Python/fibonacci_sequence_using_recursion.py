def fibonacci(num):
    if num in [1,2]:
        return 1
    return fibonacci(num -1) + fibonacci(num - 2)

for i in range(1,20):
    print(fibonacci(i))

# 1 1 2 3 5 8 13 21 34 55
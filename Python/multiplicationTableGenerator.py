def product(multiplicand, multipliers):
    for i in range(1, multipliers+1):
        print(f"{multiplicand} x {i} = {multiplicand*i}")
    
a,b = map(int, input("Enter two numbers: ").split())

print(f"The multiplication table of {a} upto {b} is ")
product(a,b)
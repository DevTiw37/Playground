def calculate_even_sum(start, end):
    sum = 0
    for i in range(start,end+1):
        if i%2 == 0:
            sum = sum + i
    return sum

a,b = map(int, input("Enter starting and ending number: ").split())

print(f"Sum of all even numbers from {a} to {b} is {calculate_even_sum(a,b)}")
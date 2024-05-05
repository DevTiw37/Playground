def calculate_odd_sum(star, end):
    sum = 0
    for i in range(star, end+1):
        if i % 2 != 0:
            sum = sum + i
    return sum

a,b = map(int,input("Enter star and end number: ").split())

print(f"Sum of odd numbers from {a} to {b} is {calculate_odd_sum(a,b)}")
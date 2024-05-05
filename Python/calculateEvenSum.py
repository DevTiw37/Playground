def calculete_even_sum(start,end):
    sum = 0
    for i in range(start,end+1):
        if i%2==0:
            sum = sum + i
    return sum

print(calculete_even_sum(0,10))
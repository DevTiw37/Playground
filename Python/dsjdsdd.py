num = int(input("Enter a positive number: "))

if num > 1:
    is_prime = True
    for i in range(2,num):
        if num%i == 0:
            is_prime = False

if is_prime == True:
    print("Its a prime")
elif is_prime == False:
    print("Not a prime")

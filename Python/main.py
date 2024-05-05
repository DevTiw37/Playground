# This is a simple python program to make a chalculator which can perform arithematic operations like 
# Addition, Subtraction, Multiplication, Division, Floor Division, Modulo and Exponent

print("Input format \"A operation B\"\nExample: 2 + 2 \n")
for _ in range(int(input("Enter no. of test cases: "))):
    # Taking input from the user
    user_input = input("Enter two numbers and a operator in the above format: ")
    value = user_input.split()
    try:
        a = int(value[0])
        b = int(value[2]) # I have changed the address of the list to make input format as a c(operator) b
    except ValueError:
        print("Error: Please enter integer for a and b")
    c = value[1]
    
    # Making all the calculation using if-else statements
    if (c=="+"):
        print(a+b)
    elif (c=="-"):
        print(a-b)
    elif (c=="*"):
        print(a*b)
    elif (c=="/"):
        print(a/b)
    elif (c=="//"):
        print(a//b)
    elif (c=="%"):
        print(a%b)
    elif (c=="**"):
        print(a**b)
    else:
        print("Error: Please chose a valid operator")
# n = input("Enter some number: ")
# print(f"Multiplication table of {n} is: ")
# try:
#     for i in range(1,11):
#         print(f"{i} x {n} = {i*int(n)}")
# except:
#     print("Sorry some error occured")
# print("Some important lines of code")
# print("end of program")

#-------------------------------------------------------------------------------

num = int(input("Enter a number between 4 to 11: "))
if (num < 4 or num > 10):
    raise ValueError("Invalid")
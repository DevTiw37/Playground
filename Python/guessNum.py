import random
rnum = random.randrange(100)
print(rnum)
num = int(input("I'm thinking of a number between 0 to 100, can you guess it?: "))
if num == rnum:
    print("Correct! You guessed it right. Correct answer is",rnum)
elif abs(num - rnum) <= 5 and num < rnum:
    print("That was pritty close! but it's lesser. Correct answer is",rnum)
elif num < rnum :
    print("No! it's lesser. Correct answer is",rnum)
elif abs(num - rnum) <= 5 and num > rnum:
    print("That was pritty close! but it's greater. Correct answer is",rnum)
elif num > rnum:
    print("No! it's greater. Correct answer is",rnum)

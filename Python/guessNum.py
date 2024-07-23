import random
play = "n"
while play == "n" or play == "N":
    rnum = random.randrange(101)
    # print(rnum)
    num = int(input("I'm thinking of a number between 0 to 100, can you guess it?: "))
    if num > 110:
        print("That's way beyond the range!")
    elif num > 100:
        print("That's beyond the range!")
    elif num == rnum:
        print("Correct! You guessed it right. Correct answer is", rnum)
    elif abs(num - rnum) <= 5 and num < rnum:
        print("That was pritty close! but it's lesser. Correct answer is", rnum)
    elif num < rnum:
        print("No! it's lesser. Correct answer is", rnum)
    elif abs(num - rnum) <= 5 and num > rnum:
        print("That was pritty close! but it's greater. Correct answer is", rnum)
    elif num > rnum:
        print("No! it's greater. Correct answer is", rnum)
    play = input("Do you want to quit? Y or N: ")
    

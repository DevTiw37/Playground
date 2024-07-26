# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decod

str = input("Enter a message: ")
words = str.split(" ")
option = input("Type 1 for coding, 2 for decoding: ")
if (option == "1"):
    for word in words:
        if len(word) >= 3:
            r1 = "scx"
            r2 = "ysd"
            word = r1 + word[1:] + word[0] + r2
            print(word, end=" ")
        else:
            print(word[::-1], end=" ")
else:
    for word in words:
        if len(word)>=3:
            word = word[3:-3]
            word = word[-1] + word[:-1]
            print(word, end=" ")
        else:
            print(word[::-1], end=" ")
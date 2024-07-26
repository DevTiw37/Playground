# Reffer - https://gemini.google.com/share/continue/1217ef4e9066
# Answers - 4, 4, 1, 2, 1, 2, 3, 2, 2, 1, 2, 1, 2, 3, 2

from num2words import num2words

print("Hint - 4, 4, 1, 2, 1, 2, 3, 2, 2, 1, 2, 1, 2, 3, 2\n")

question_bank = [
    ["What is the correct way to print \"Hello World!\" to the console in Python?",
     "<p>Hello World!</p>", "echo \"Hello World!\"", "cout << \"Hello World!\" << endl;", "print(\"Hello World!\")", 4],
    ["Which of the following is NOT a valid data type in most programming languages?",
     "Integer", "Float", "Boolean", "Breakfast", 4],
    ["What is the purpose of a loop in coding?", "To repeat a block of code a specific number of time.",
     "To define a function.", "To store data permanently.", "To close a program.", 1],
    ["What symbol is used to comment out a line of code in JavaScript?",
        "#", "//", "/* */", "!", 2],
    ["What does HTML stand for?", "Hyper Text Markup Language", "High Tech Machine Language",
     "Holistic Texting Meta Language", "Hidden Texting Markup Link", 1],
    ['What is the difference between a function and a method in programming?', 'There is no difference, they are interchangeable.', 'Functions are standalone while methods are attached to objects',
        'Functions are for calculations and methods are for data manipulation.', 'Functions are used in high-level languages and methods in low-level languages.', 2],
    ['What is the time complexity of a nested loop iterating through a matrix (2D array)?',
     'O(log n)', 'O(n)', 'O(n^2)', 'O(n^3)', 3],
    ['What is the purpose of an if-else statement in coding?', 'To define a variable.',
        'To execute code conditionally based on a boolean expression.', 'To loop through a set of data.', 'To call a function.', 2],
    ['What does the term "recursion" mean in programming?', 'A loop that iterates forever.', 'A function that calls itself within its own definition.',
        'An error that occurs during program execution.', 'A way to access data from another program.', 2],
    ['What is the difference between GET and POST requests in HTTP?', 'GET is used to retrieve data, POST is used to create data.',
        'GET is faster than POST.', 'GET requests are secure, POST requests are not.', 'GET requests can only send small amounts of data.', 1],
    ['What is the concept of inheritance in object-oriented programming?', 'Sharing code between unrelated objects.', 'Creating new objects from existing objects with similar properties and behaviors.',
        'A way to define variables that can hold multiple data types.', 'A method for managing memory allocation in a program.', 2],
    ['What is the difference between a linked list and an array in data structures?', 'Arrays are faster for random access, linked lists are faster for insertions and deletions.',
        'Arrays can only store one data type, linked lists can store multiple data types.', 'Arrays are stored contiguously in memory, linked lists are not.', 'Arrays are used for storing primitive data types, linked lists are used for objects.', 1],
    ['What is the purpose of a hash table in programming?', 'To store data in a sorted order.', 'To efficiently associate keys with values',
        'To represent hierarchical relationships between objects.', 'To store large amounts of binary data.', 2],
    ['What are some common design patterns used in software development?', 'There is only one universal design pattern for all situations.', 'Design patterns are pre-written code snippets for specific tasks.',
        'Design patterns are reusable solutions to common programming problems.', 'Design patterns are specific algorithms used for data processing.', 3],
    ['What are some key considerations for writing clean and maintainable code?', 'Using complex algorithms to impress other programmers.', 'Following consistent naming conventions and proper indentation.',
        'Writing the shortest code possible, regardless of readability.', 'Including minimal comments as the code should be self-explanatory.', 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000,
          80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
counter = 0

for i in range(len(question_bank)):
    question_items = question_bank[i]
    print(f"Level: {i + 1} Question for {num2words(levels[i], lang='en_IN')} rupees\n")
    print(f"Q{i+1}) {question_items[0]}")
    print("Options are: ")
    print(f"a. {question_items[1]} \nb. {question_items[2]}\nc. {
          question_items[3]}\nd. {question_items[4]}")
    answer = input("Chose option as (1,2,3,4) or quit to abort: ")
    counter = counter + 1
    if answer == "quit":
        if i == 0:
            break
        print(f"You earned {num2words(levels[i-1])} rupees!")
        break
    elif int(answer) == question_items[5]:
        print("Correct!")
    else:
        print("Sorry, you lost the game!")
        break

if counter == len(levels):
    print("Adbhut! you are a crorepati now 💸")
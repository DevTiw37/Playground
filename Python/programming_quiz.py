import tkinter as tk
import random
from num2words import num2words
from tkinter import messagebox

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


class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kaun Banega Crorepati")
        self.master.geometry("800x600")

        self.current_level = 0
        self.score = 0
        self.lifelines = {"50:50": True, "Double Dip": True}

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        # Question label
        self.question_label = tk.Label(
            self.master, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        # Option buttons (using radio buttons for single selection)
        self.option_vars = [tk.StringVar()
                            for _ in range(4)]  # List of IntVars for options
        self.option_buttons = []
        for i in range(4):
            ## option_text = tk.StringVar()
            option_button = tk.Radiobutton(
                self.master, textvariable = self.option_vars[i], value=i + 1)
            option_button.pack()
            self.option_buttons.append(option_button)

        # Answer button
        self.answer_button = tk.Button(
            self.master, text="Submit Answer", command=self.check_answer)
        self.answer_button.pack(pady=10)

        # Lifelines display
        self.lifeline_label = tk.Label(self.master, text=f"Lifelines: 50:50 - {
                                       'Available' if self.lifelines['50:50'] else 'Used'}, Double Dip - {'Available' if self.lifelines['Double Dip'] else 'Used'}")
        self.lifeline_label.pack()

        # Lifeline buttons (use separate buttons for each lifeline)
        self.lifeline_5050_button = tk.Button(
            self.master, text="50:50", command=self.use_5050_lifeline, state=tk.DISABLED if not self.lifelines['50:50'] else tk.NORMAL)
        self.lifeline_5050_button.pack(pady=5)
        self.lifeline_double_dip_button = tk.Button(
            self.master, text="Double Dip", command=self.use_double_dip_lifeline, state=tk.DISABLED if not self.lifelines['Double Dip'] else tk.NORMAL)
        self.lifeline_double_dip_button.pack()

        # Money display
        self.money_label = tk.Label(self.master, text=f"Money Won: ₹ {num2words(
            levels[self.current_level], lang='en_IN')}", font=("Arial", 14))
        self.money_label.pack(pady=20)

    def display_question(self):
        current_question = question_bank[self.current_level]
        question_text = current_question[0]
        options = current_question[1:5]
        correct_answer = current_question[5]
        
        self.question_label.config(text=question_bank[self.current_level][0])
        for i in range(4):
            self.option_vars[i].set(0)  # Reset option selections

        self.answer_button.config(state=tk.NORMAL)  # Enable answer button

    def check_answer(self):
        selected_option = int(self.option_vars.get())
        if selected_option == 0:
            tk.messagebox.showerror("Error", "Please select an option!")
            return  # Exit the function if no option is selected

        correct_answer = question_bank[self.current_level][5]
        if selected_option == correct_answer:
            self.score = levels[self.current_level]
            self.current_level += 1

            self.money_label.config(text=f"Money Won: ₹ {num2words(
                levels[self.current_level], lang='en_IN')}")

            if self.current_level == len(levels) - 1:
                self.game_over("won")
            else:
                self.display_question()  # Display next question
        else:
            self.game_over("lost")

    def use_5050_lifeline(self):
        if not self.lifelines["50:50"]:
            tk.messagebox.showinfo("Lifeline Used", "50:50 is already used!")
            return

        correct_answer = question_bank[self.current_level][5]
        incorrect_options = []
        for i in range(1, 5):
            if i != correct_answer:
                incorrect_options.append(question_bank[self.current_level][i])

        # Randomly remove one incorrect option to maintain fairness
        random.shuffle(incorrect_options)
        option_text = question_bank[self.current_level][0] + "\n"
        for i in range(4):
            if self.option_vars[i].get() == correct_answer or self.option_vars[i].get() in incorrect_options:
                option_text += f"{'abcd'[i]
                                  }. {question_bank[self.current_level][i+1]}\n"
            else:
                # Disable remaining incorrect option
                self.option_vars[i].set(0)

        self.question_label.config(text=option_text)
        self.lifelines["50:50"] = False
        self.lifeline_5050_button.config(state=tk.DISABLED)

    def use_double_dip_chance(self):
        if not self.lifelines["Double Dip"]:
            tk.messagebox.showinfo(
                "Lifeline Used", "Double Dip is already used!")
            return

        # Simulate user's guess based on current selection
        user_guess = self.check_answer()
        if user_guess is None:  # User didn't select an option
            return

        if user_guess == "lost":
            self.game_over("lost")
        else:
            self.lifelines["Double Dip"] = False
            self.lifeline_double_dip_button.config(state=tk.DISABLED)

    def game_over(self, status):
        self.answer_button.config(state=tk.DISABLED)
        self.lifeline_5050_button.config(state=tk.DISABLED)
        self.lifeline_double_dip_button.config(state=tk.DISABLED)

        if status == "won":
            tk.messagebox.showinfo("Congratulations!", f"You won ₹ {
                                   num2words(levels[-1], lang='en_IN')}! You are a Crorepati!")
        else:
            correct_answer = question_bank[self.current_level][5]
            correct_option_text = question_bank[self.current_level][correct_answer]
            tk.messagebox.showinfo("Game Over", f"You lost! The correct answer was: {correct_option_text}\nYou won ₹ {
                                   num2words(levels[self.current_level - 1] if self.current_level > 0 else 0, lang='en_IN')}")


root = tk.Tk()
app = QuizApp(root)
root.mainloop()

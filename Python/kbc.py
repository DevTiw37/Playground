# Source https://g.co/gemini/share/1217ef4e9066
# Source https://g.co/gemini/share/574c7149f1ec

def main():
    """Runs the quiz program."""

    dataset = [
        ["What is the correct way to print \"Hello World!\" to the console in Python?",
         "<p>Hello World!</p>", "echo \"Hello World!\"", "cout << \"Hello World!\" << endl;", "print(\"Hello World!\")", 4],
        ["Which of the following is NOT a valid data type in most programming languages?",
         "Integer", "Float", "Boolean", "Breakfast", 4],
        ["What is the purpose of a loop in coding?", "To repeat a block of code a specific number of time.",
         "To define a function.", "To store data permanently.", "To close a program.", 1],
        ["What symbol is used to comment out a line of code in JavaScript?", "#", "//", "/* */", "!", 2],
        ["What does HTML stand for?", "Hyper Text Markup Language", "High Tech Machine Language",
         "Holistic Texting Meta Language", "Hidden Texting Markup Link", 1],
    ]

    score = 0
    for i, question in enumerate(dataset):
        print(f"Q{i+1}) {question[0]}")

        for j, option in enumerate(question[1:-1]):  # Exclude answer and index from options
            print(f"\t{j+1}. {option}")

        answer = input("Enter your answer (number): ")
        if answer.isdigit() and int(answer) == question[-1]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question[question[-1]])

    print(f"You scored {score} out of {len(dataset)} questions.")

if __name__ == "__main__":
    main()

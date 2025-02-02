from random import randint
def rock_paper_scissor(response):
    choice = {'rock': 'paper', 'paper':'scissor', 'scissor': 'rock'}
    rnum = randint(0,2)
    choice_list = list(choice.keys())
    computer_choice = choice_list[rnum]
    if computer_choice == response:
        return 'Its a draw', computer_choice
    if computer_choice == choice[response]:
        return 'You lost!', computer_choice
    return 'You won!', computer_choice

user_response = input('Enter rock, paper or scissor: ')
print(rock_paper_scissor(user_response))
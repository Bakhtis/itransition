# -*- coding: utf-8 -*-

import random
import sys
from prettytable import PrettyTable

def parse_choice(choice_str, choices):
    if choice_str == 911:
        return 0
    return choices.get(choice_str)

def user_choice(choices):
    while True:
        try:
            print("Ваш ход. Выберите один из вариантов: " +  ', '.join(choices.values()) + ". Для помощи наберите 911.")
            choice_str = int(input())
            choice = parse_choice(choice_str, choices)
            if choice is not None and choice != 0:
                return choice_str
            elif choice == 0:
                print_help(choices)
            else:
                print("Неверный выбор. Пожалуйста, выберите один из вариантов: " + ', '.join(choices.values()) + ".")
        except:
            print("Неверный ввод. Пожалуйста, выберите один из вариантов:" +  ', '.join(choices.values()) + ".")


def print_help(choices):
    print("Помощь:")
    half_choices = len(choices)//2
    num_choices = len(choices)
    table = PrettyTable([''] + list(choices.values()))
    max_length = max(len(choice) for choice in choices.values())

    for choice_num, choice in choices.items():
        outcomes = []
        for opponent_num, _ in choices.items():
            if (choice_num - opponent_num) % num_choices == 0:
                outcome = 'Ничья'
            elif (choice_num - opponent_num) % num_choices <= half_choices:
                outcome = 'Поражение'
            else:
                outcome = 'Победа'
            outcomes.append(outcome)
        table.add_row([choice.ljust(max_length)] + outcomes)

    print(table)

def computer_choice(num_choices):
    return random.randint(1, num_choices)

def winner(user_choice, computer_choice, num_choices):
    half_choices = num_choices // 2
    if (user_choice - computer_choice) % num_choices == 0:
        return "Ничья"
    elif (user_choice - computer_choice) % num_choices <= half_choices:
        return "Победил компьютер !"
    else:
        return "Вы Победили!"

def main():
    num_args = len(sys.argv) - 1
    if num_args % 2 == 0 or num_args < 3:
        print("Пожалуйста, введите нечетное количество вариантов через пробелы.")
    else:
        choices_str = ' '.join(sys.argv[1:])
        choices = {index + 1 : choice.strip() for index, choice in enumerate(choices_str.split())}
        num_choices = len(choices)
        game(choices, num_choices)

def game(choices, num_choices):
    user = user_choice(choices)
    computer = computer_choice(num_choices)

    print("Ваш ход: " + parse_choice(user, choices))
    print("Ход компьютера: " +  parse_choice(computer, choices))
    result = winner(user, computer, num_choices)
    print(result)

if __name__ == "__main__":
    main()

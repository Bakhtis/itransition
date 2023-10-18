import random
def user_choice():
    while True:
        try: 
            choice = int(input("Ваш ход. Выберите от 1-5, где 1 = камень, 2 = спок, 3 = бумага, 4= ящерица, 5 = ножницы, 6 = помощь : "))
            if 1 <= choice <= 5:
                return choice
            elif choice == 6:
                print(r'''  +-------------+---------+---------+---------+---------+---------+
                            | v PC\User > |  камень | спок    | бумага  | ящерица | ножницы |
                            +-------------+---------+---------+---------+---------+---------+ 
                            | камень      |  Ничья  | Победа  | Победа  |Поражение|Поражение|
                            +-------------+---------+---------+---------+---------+---------+
                            | спок        |Поражение| Ничья   | Победа  | Победа  |Поражение|
                            +-------------+---------+---------+---------+---------+---------+
                            | бумага      |Поражение|Поражение| Ничья   | Победа  | Победа  |
                            +-------------+---------+---------+---------+---------+---------+
                            | ящерица     | Победа  |Поражение|Поражение|  Ничья  | Победа  |
                            +-------------+---------+---------+---------+---------+---------+
                            | ножницы     | Победа  | Победа  |Поражение|Поражение|  Ничья  |
                            +-------------+---------+---------+---------+---------+---------+''');
                print ("Еще раз; пожалуйста, выберите цифру от 1 до 5")
            
            else:
                print("Еще раз; пожалуйста, выберите цифру от 1 до 5")
        except ValueError:
            print("Неверный ввод. Прошу внести цифру от 1 до 5")

def computer_choice():
    return random.randint(1,5)

def winner(user_choice, computer_choice):
    if  (user_choice == 1 and (computer_choice ==5 or computer_choice ==3)) or \
        (user_choice == 2 and (computer_choice ==3 or computer_choice ==4)) or \
        (user_choice == 3 and (computer_choice ==4 or computer_choice ==5)) or \
        (user_choice == 4 and (computer_choice ==2 or computer_choice ==1)) or \
        (user_choice == 5 and (computer_choice ==1 or computer_choice ==2)):
            return "Вы победили!"
    elif user_choice == computer_choice:
        return "Ничья"
    else:
        return "Победил компьютер!"
    
    
def game(): 
    user = user_choice()
    computer =computer_choice()

    print(f"Ваш ход: {user}")
    print(f"Ход компьютера: {computer}")
    result = winner(user, computer);
    print(result);

game()

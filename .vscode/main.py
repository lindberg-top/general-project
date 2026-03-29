import random
# guess number 
def game1():
    number = random.randint(1, 10)
    print("Угадай число от 1 до 10")
    while True:
        try:
            guess = int(input("Ваше предположение: "))
            if guess == number:
                print("Поздравляю, вы угадали!")
                break
            elif guess < number:
                print("Слишком мало, попробуйте еще  раз!")
            else:
                print("Слишком много, попробуйте еще раз!")
        except ValueError:
            print("Пожалуйста, введите целое число!")
            
            
def game2():
    print("\nИгра 'Орёл или Решка!'")
    choice = input("Выберите 1 - Орёл, или 2 - Решка: ")
    result = random.choice(['1', '2'])
    if choice == result:
        print("Вы выиграли!")
    else:
        print("Не повезло")  
        

def main_menu():
    while True:
        print("\n" + "="*30)
        print("ДОБРО ПОЖАЛОВАТЬ В ИГРОВОЙ ЦЕНТР!")
        print("="*30)
        print("Выберите игру:")
        print("1 — Угадай число")
        print("2 — Орёл или решка")
        print("0 — Выход")
        
        choice = input("Выберите игру (1/2/0): ")
        
        if choice == '1':
            game1()
        elif choice == '2':
            game2()
        elif choice == '0':
            print("Спасибо за игру. Удачи!")
            break
        else:
            print("Неверный ввод, выберите - 1, 2 или 0")
            
            
if __name__ == "__main__":
    main_menu()

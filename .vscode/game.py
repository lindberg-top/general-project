def check_message(message):
    while True:
        message = input("Введите сообщение: ")
        words = message.split()
        
        if len(words) == numbers:
            print("получилось")
            break
        else:
            print("попробуй еще раз")
            
            
numbers = int(input("Введите число: "))
check_message(numbers)
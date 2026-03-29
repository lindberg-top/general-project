# # # # # def bio(name, age, country):
# # # # #     print("Меня зовут: ", name, "мне", age, "лет", "я из: ", country)
    
# # # # # # bio(name="Nikolay", age=20, country="Russia")

# # # # def calculator():
# # # #     a = int(input("Введите первое число: "))
# # # #     b = int(input("Введите второе число: "))
    
# # # #     sign = input("Выберите знак: +, -, *, /: ")
        
# # # #     if sign == "+":
# # # #         print("Ответ: ", a + b)
        
# # # #     elif sign == "-":
# # # #         print("Ответ: ", a - b)
        
# # # #     elif sign == "*":
# # # #         print("Ответ: ", a * b)
        
# # # #     elif sign == "/":
# # # #         if b != 0:
# # # #             print("Ответ: ", a / b)
# # # #         else:
# # # #             print("Делить на 0 нельзя")
            
# # # #     else:
# # # #         print("error!")

# # # # calculator()

# # # def say_hi():
# # #     return "Привет, я учу Python!"
# # # name = say_hi()
# # # print(name)










# # def square(n):
# #     return n ** 2 
# #                        # ЗАДАНИЕ 2
# # math = square(5)
# # print(math)

# def filter_even(numbers):
#     result = []
    
#     for num in numbers:
#         if num % 2 == 0:
#             result.append(num)
            
#     return result
# print(filter_even([1, 2, 3, 4, 5, 6]))



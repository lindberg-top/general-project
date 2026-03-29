# # # # # def nums(numbers):
# # # # #     lst = []
    
# # # # #     for el in numbers:
# # # # #         if el % 2 == 0:
# # # # #             lst.append(el)
# # # # #     return lst

# # # # # lst = nums([1,2,3,4,5,6])
# # # # # print(lst)
    
    
# # # # def filter_even(numbers):
# # # #     return [n for n in numbers if n % 2 == 0]
# # # # result = filter_even(1,2,3,4)
# # # # print(result)

# # # def count_even(numbers):
# # #     result = []
# # #     count = 0
    
# # #     for el in numbers:
# # #         if el % 2 == 0:
# # #             count += 1
# # #             result.append(el)
            
# # #     return count

# # # result = count_even([2,4])
# # # print(result)        

# # def sum_even(numbers):
# #     result = []
# #     total = 0
    
# #     for el in numbers:
# #         if el % 2 == 0:
# #             total += el
            
# #     return total
# # result = sum_even([2,4,5,6])
# # print(result)

# def get_even(numbers):
#     num = []
    
#     for el in numbers:
#         if el % 2 == 0:
#             num.append(el)
            
#     return num

# num = get_even([1,2,3,4])
# print(num)

def get_element(numbers):
    lst = []
    count = 0
    
    for n in numbers:
        if n % 2 == 0:
            lst.append(n)
            count += n
            
    return count

lst = get_element([1,2,3,4,5,6])
print(lst)
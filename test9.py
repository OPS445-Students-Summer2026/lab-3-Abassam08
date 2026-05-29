# #!/usr/bin/env python3

# courses = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
# # print(courses[0])
# # courses[0] = 'eac150'
# # print(courses[0])
# # print(courses)
# # courses.append('ops235')
# # print(courses)
# # courses.insert(0, 'hwd101')
# # print(courses)
# courses.remove('ops335')
# print(courses)

# sorted_courses = courses.copy()
# sorted_courses.sort()
# print(sorted_courses)

list_of_numbers = [ 1,5, 2, 6, 8, 5, 10, 2 ]
# length_of_list = len(list_of_numbers)
# smallest_in_list = min(list_of_numbers)
# largest_in_list = max(list_of_numbers)

# print("List length is: " + str(length_of_list) + ", smallest element in the list is: " + str(smallest_in_list) + ", largest element in the list: " + str(largest_in_list))
# for i in list_of_numbers:
#     if i != '5' and i != '1':
#      print(i)
# def square(num):
#     return num * num

# for value in list_of_numbers:
#     print(square(value))

# def square_list(number_list):
#     new_list = []
#     for number in number_list:
# #         new_list.append(number * number)
# #     return new_list
# # print(square_list(list_of_numbers))
# def square_list(number_list):
#     new_list = []
#     for number in number_list:
#         new_list.append(number * number)
#     return new_list
# new_list_of_numbers = square_list(list_of_numbers)
# print(list_of_numbers)
# print(new_list_of_numbers)

def delete_numbers(numbers):
    numbers.remove(5)
    numbers.remove(6)
    numbers.remove(8)
    numbers.remove(5)
delete_numbers(list_of_numbers)
[print(list_of_numbers)]
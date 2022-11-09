# import random

# superheroes=[{
#     'name': 'Batman',
#     'city': 'Gotham',
#     'symbol': 'Bat',
#     'bad_guys': ["Mafia", "Bad Guys", "Criminals"]
# },

# {
#     'name': 'Superman',
#     'city': 'Detroit',
#     'symbol': 'S',
#     'bad_guys': ["Mafioso", "Bad Dude", "Criminales"]
# }]

# batman = {
#     'real_name': 'Bruce Wayne',
#     'location': 'Gotham',
#     'symbol': 'Bat',
#     'age': 'undisclosed'
# }

# for key, value in batman.items():
#     print(f"This is the key: {key}; this is the corresponding {value}.")

# def party():
#     print('Number of days coding')
#     return 1000

# print(party())    

# def hello():
#     return 10

# x = hello()


# print(x + 10)   

# test_data = [12, 14, -9, 23]


# def add(lst):
#     new_list = []
#     for x in test_data:
#         new_list.append(x + 100)
#     return new_list   

# print(add(test_data))           

# numbers = [7, 13, 8, 42]

# for x in range(0, len(numbers)):
#     print(x)
#     print(numbers[x])
# if numbers[len(numbers) - 1] == 42:
#     print("You are a successful coder with a beautiful woman.")    

# for num in range(10):
#     if num % 4 == 0:
#         print('Hello')
#     elif num % 2 == 0:
#         print('World')
#     else:
#         print(num)        

# pet_info = {
#     'name':'Fido',
#     'age': 4,
#     'trick': 'Roll over'
# }

# for stuff in pet_info:
#     # print(stuff)
#     print(pet_info[stuff])

# to_do = {
#     'first': 'Use the 20-minute rules',
#     'second': 'Ask for help',
#     'third': 'Ask a TA',
#     'fourth': 'Ask and instructor'
# }

# for num, step in to_do.items():
#     print(num + ", I will " + step)

# for x in range(150):
#     print(x)

# for x in range(5, 1000):
#     if x % 5 == 0:
#         print(x)

# for x in range(100):
#     if x % 10 == 0:
#         print('Coding')
#     elif x % 5 == 0:
#         print("Dojo") 
#     else:
#         print(x)    

# for x in range(2018, 0, -4):
#     print(x)

# low_num = 2
# high_num = 20
# mult = 3

# for x in range(low_num, high_num, 1):
#     if x % mult == 0:
#         print(x)

# test_data = [-1, -3, 5, 4]

# def replace(lst):
#     new_list = []

#     for x in lst:
#         if x > 0:
#             x = 'Positive'
#             new_list.append(x)
#         else:
#             new_list.append(x)

#     return new_list

# print(replace([1, -3, 4])) 
# You can either input a variable with an already assigned value or, as shown, manually input data as long as data format matches. This is where the "test_data" variable came into play
#                        

# def counter(lst):
#     y = 0

#     for x in lst:
#        if x > 0:
#             y = y + 1   
#     lst[len(lst) - 1] = y
#     return lst

# print(counter([1, 4, 5, -10]))
# There was no need to create a new_list variable but it would have create excess code for the same output as the above. The purpose of this function was to count all the positive integers in a list and replace the last value in the list with the number of positive integers.

# def total(lst):
#     total = 0

#     for x in lst:
#         total += x
#     return total

# print(total([4, 5, 6]))        
# Intended effect was addition of all the numbers within the list

# def average(lst):
#     sum = 0

#     for x in lst:
#         sum += x

#     return float(sum) / float(len(lst))

# print(average([2, 3, 4, 9]))  
# Remember that you can return a function as long as variables inputs are correct. The float was used since we were seeing an average. The purpose of this function was to find the average of a list. 
     

# def how_long(lst):
#     counter = 0
#     for x in lst:
#         counter += 1
#     return counter    
   
# print(how_long([2, 4, 6, 7]))
# Output of this function is the length of a list.

# def minimum(lst):
#     if len(lst) == 0:
#         return False

#     result = lst[0]
#     for x in lst:
#         if x > result:
#             result = x    
#     return result

# print(minimum([-4, 3, 6, -9, 8]))
# This function identified the largest value in the list

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37, 2, 1, -9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}

# def ultimate(lst):
#     results = {
#         'sumTotal': None,
#         'average': None,
#         'minimum': None,
#         'maximum': None,
#         'length': 0,
#     }

#     if len(lst) < 0:
#         return results

#     else:
#          results['sumTotal'] = 0
#          results['minimum'] = lst[0]
#          results['maximum'] = lst[0]

#     for x in lst:
#         if x > results['maximum']:
#             results['maximum'] = x
#         elif x < results['minimum']:
#             results['minimum'] = x

#         results['sumTotal'] += x  
#         results['length'] += 1

#     results['average'] = float(results['sumTotal']) / float(results['length'])

#     return results
# print(ultimate([2, 4, 6]))                 

# 1. Set dictionary keys so values so they can can be compared to other values. 
# 2. Compare dictionary values as highest or lowest for the respective key. Start simple and basic: what information doesn't require calculation for input > minimum, maximum. length of list. Iterating thru the list to determine max/min is a necessary step prior to assigning further values to additional keys.
# 3. Set the length and sumTotal variable to count with each iteration. They count OUTSIDE of the min/max/total assignment so they are indented BACK, but still with in the Loop.
# 4. Once all the pertinet pieces are put together and we no longer need to count each iteration, calculate & assign value to the 'avereage' key.
# 5. Return the entire dictionary after all loops are complete and lines of code run.
# *Use 'None' as a placeholder in dictionary since it will eventually be populated with an integer. Use '0' since the function adds to this with each repitition & you can't add to 'None.


# def reverse(lst):

#     half_len = int(len(lst) / 2)
    
#     for x in range(half_len):
#         lst[x], lst[len(lst) - 1 - x] = lst[len(lst) -1 - x], lst[x]
#     return lst
    
# a = reverse([3,6,9,12])    

# print(a)

# Create function that takes in a list and returns a new list with the values in reverse order w/out creating a new list.
# Lne 231: Index x, index of list length - 1 - x
# Iteration: lst = [3, 4, 5]
# Iteration #1: x = 0
# lst[0], lst[2] = lst[2], lst[0]
#  Set the value of index 0, index 2 > index, 2, index 0

# def greet(name = '', repeat = 2):
#     print(f"Good morning {name}" * repeat)

# greet("bill")

# x = [[5,2,3], [10,8,9]]

# x[1][0] = 15

# print(x)

# students = [
#     {"first_name" : "Michael", "last_name" : "Jordan"},
#     {"first_name" : "John", "last_name" : "Rosales"}
#     ]

# students[0]["last_name"] = "Bryant"     

# print(students[0]["last_name"])

# directory = {
#     "basketball" : ["Kobe", "Jordan", "James", "Curry"],
#     "soccer": ["Messi", "Ronaldo", "Rooney"]
#     }

# directory["soccer"][0] = "Andres"

# print(directory["soccer"])

# z = [{"x": 10, "y": 20}]

# z[0]["y"] = 30

# print(z)

# students = [
#     {"first_name" : "Michael", "last_name" : "Jordan"},
#     {"first_name" : "John", "last_name" : "Rosales"},
#     {"first_name" : "Mark", "last_name" : "Cuban"},
# ]

# def sorter(some_lst):
#     for dict in some_lst:
#         display_string = ""
#         for curr_key in dict.keys():
#              display_string += f"{curr_key} - {dict[curr_key]},"
#         print(display_string)

# sorter(students)        
# Line 294: For each dictionary in the list, evaluate EACH key in EVERY dictionary.
           
# students = [
#     {"first_name" : "Michael", "last_name" : "Jordan"},
#     {"first_name" : "John", "last_name" : "Rosales"},
#     {"first_name" : "Mark", "last_name" : "Cuban"},
# ]

# def sorter(some_list):
#     for x in range(len(some_list)):
#         for key in some_list[x]:
#             # print(some_list[x][key])
#              print(key, '-', some_list[x][key])
# sorter(students)     
# 
# The above (306 - 311), can be written slightly differently for ease of use:
# 
# def sorter(some_list):
#     for x in range(len(some_list)):
#         student_dict = some_list[x]
#         for key in student_dict:
#             print(key, "-", student_dict[key])
# sorter(students)            
# 
#    
# Line 307 > Grabs each dictionary in the list and hangs onto it. It is then with the keys we access the value and can print just the value.
#Line 308 > creates a For Loop to be run on the list item grabbed by the first line of code. Since the data type we are deailng with is a list, the For Loop will produce index values when iterating the list. First iteration grabs the first value/item at that index. In this case it is a dictionary. Since we are now dealing with a dictionary, we have to iterate through it by the key_name, hence, nested For Loop to run on the one the first For Loop grabbed. 
# Nested For Loop = (Key is the iterative variable, dictionaries iterated by key): Go through each key in the dictionary the previous For Loop grabbed. 
# Line 310 > setting a variable allows you to avoid additional square brakcets when accessing:
# some_list[x][key]: Iteration #1 > grab the value at list index 0, iterate through keys and identify the value at each key within the item at index 0.
# Line 317 > create variable to hold each item as you iterate. 
# student_dict is equal to the dictionary at index 0, which means it holds both key-value pairs.
# for key in student_dict:
    # print(key, "-", student_dict[key]) print the key itself as well as the value assigned at that partcular key

# students = [
#     {"first_name" : "Michael", "last_name" : "Jordan"},
#     {"first_name" : "John", "last_name" : "Rosales"},
#     {"first_name" : "Mark", "last_name" : "Cuban"},
#     ]     



# def iterate(key_name, some_list):  
    # students = [
    # {"first_name" : "Michael", "last_name" : "Jordan"},
    # {"first_name" : "John", "last_name" : "Rosales"},
    # {"first_name" : "Mark", "last_name" : "Cuban"},
    # ]  
    # for x in range(len(some_list)):

    #     print(some_list[x][key_name])

# iterate('first_name', students)

# users = [
#     {"gangster" : "Al Capone", "racket" : "Bootlegging"},
#     {"gangster" : "Paul Castellano", "racket" : "Bootlegging"},  
# ]
# iterate("gangster", users)

#In the above, the user would provide the specific key they wanted to search out. For example, if they wanted just the value at "first_name" in each dictionary, they would input that into their query when the function is called. The function reads the key name as what to search. The "some_list" parameter tells the us where the data will be retrieved from. In this case, the function translates to "Print the first names in the students list of dictionaries." Each student has an assigned dictionary, grab each one via the For Loop and identify the value at key "first_name"
# For some reason, when the variable was put inside the function, I received error students not defined. When I moved the "students" list outside and above the function, it worked.??????????


# dojo = {
#     "locations" : ["San Jose", "Seattle", "Dallas", "Chicago", " Tulsa", "DC", "Burbank"],
#     "instructors" : ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
# }

# def printer(some_dict):
#     for key in some_dict:
#         print(len(some_dict[key]), key.capitalize())
#         for value in some_dict[key]:
#             print(value)
        
# printer(dojo)   

# def printer(some_dict):
#     for key in some_dict:
#         print(key.capitalize(), len(some_dict[key]))
#         for value in some_dict[key]:
#             print(value)

# printer(dojo)
# Line 376 > create a function that takes in a paremeter (in this example, the input type is a dictionary whose values are lists)
# Line 377 > This For Loop iterates through the dictionary by the key, grabbing each dictionary 1 at a time. This is the key/value pair that gets passed to the next block(s) of code.
# Line 378 > Print the interator(key) and the length of the value. Since the value is a list, this is done with len() built-in.
# Line 379 > With the first key/value pair grabbed by the first For Loop, iterate the value(s) and print those.

# dojo_1 = {
#     "locations" : ["Houston", "Dallas", "San Antonio"],
#     "instructors" : ["Bill", "John", "Mary", "Michael Scott"]
# }

# def crackler(some_dict):
#     for key in some_dict:
#         print(key.capitalize(), len(some_dict[key]))
#         for value in some_dict[key]:
#             print(value)
# crackler(dojo_1)
# Repeat of above example of iterating through a dictionary whose values are lists.

# def greet(name = "", repeat = 2):
#     print(f"Good afternoon, {name}." * repeat)

# greet("Bill")

# empty_list = []
# ninjas = ["Bill", "Bob", "Nicole"]

# ninjas.pop(1)
# ninjas[0] = "Robert"
# print(ninjas)

# students = {"name" : ["Bill", "Bob"], "belt" : "Black", "style" : "Muay Thai"}

# print(students["name"][0])

# lst = [1, 3, 6, 10]

# lst[0], lst[2] = lst[2], lst[0]

# print(lst)

# SELECTION SORT VARIATIONS#

# def selection(list_a):
#     indexing_length = range(0, len(list_a) - 1)

#     for i in indexing_length:
#         min = i

#         for j in range(i+1, len(list_a)):
#             if list_a[j] < list_a[min]:
#                 min = j
#Line 424: The reason to - 1 and not loop through this value is that there is no next value to compare it to.

# Selection Sort Written Different Ways:


# def sort(nums):
#     for i in range(0, len(nums)- 1):
#         minpos = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[minpos]:
#                 minpos = j

#             temp = nums[i]
#             nums[i] = nums[minpos]
#             nums[minpos] = temp

#             print(nums)

# nums = [5,3,8,6,7,2]
# sort(nums)

# OR # 

# nums = [45, 12, 13, 22] 

# def sorter(nums):
#     for i in range(0, len(nums)-1):
#         minpos = i
#         for j in range(i+1, len(nums)):
#             if nums[j] < nums[minpos]:
#                 minpos = j
#         if minpos != i:
#             nums[i], nums[minpos] = nums[minpos], nums[i]
#     return nums    

# nums = [45, 12, 13, 22]     
# sort(nums)
# print(sorter(nums))   

# Selection Sort#

# my_arr = [-64, 25, -12, 22, 11] 
  
# for i in range(len(my_arr)): 
#     min_idx = i 
#     for j in range(i+1, len(my_arr)): 
#         if my_arr[min_idx] > my_arr[j]: 
#             min_idx = j
#     temp = my_arr[i]
#     my_arr[i] = my_arr[min_idx]
#     my_arr[min_idx] = temp

# print(my_arr)    

# MY ATTEMPT AT WRITING WHILE TALKING THROUGH#

# def selection_sort(some_list):
#     for i in range(0,len(some_list)):
#         min_val = i
#         for j in range(i+1, len(some_list)):
#             if some_list[j] < some_list[min_val]:
#                 min_val = j

#         some_list[min_val], some_list[i] = some_list[i], some_list[min_val]        

#     return some_list

# print(selection_sort([4, 2, 9, 7]))            
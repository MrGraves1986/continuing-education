# n = int(input("Number: "))

# if n > 0:
#     print("Number is positive!")


# print("This is how to run a python program in the terminal...")

# def mult(a,b):
#     return a*b

# print(mult(3,4))

# name = input("Name: ")
# print(f"Hello, {name}")

# x = int(input("Number: "))

# if x > 0:
#     print("Number is positive!")
# elif x < 0:
#     print("Number is negative!")
# else:
#     print("Depsite my infinite knowledge, I don't know.")    

# input() will result in the program asking for input when run in the terminal. Once the number is input, it can have comparisons run on it to create further action, i.e., conditional statement(s) such as the above.
# Utlize int() since Python cannot run a comparison on an int & str.

# Sequences#

# name = "Harry"
# print(name[1])

# names = ["Harry", "Ron", "Hemione"]
# print(names[0])

# Note: Tuple is an immutable data type > it cannot be changed after creation.
# Set:collection of unique values, does not keep things in any particular order. Every valuable appears only once vs a list or tuple where values can show up multiple times > [3,4,3,5,4,9]

# names = ["Jimmy", "Shorty", "Big Anthony"]
# names.append("Bobo")
# names.sort()
# print(names)

# Sets#
#1. Create the set:
# s = set()
# # 2. Add elements into the set:
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# # *If I try to s.add(3) again, it will still only show '3' 1 time because every value in a set has to be unique.
# # 3. Print the set to see what is inside of it.
# s.remove(1)
# print(s)


# names = ["Bill", "Tom", "Jim"]

# for name in names:
#     print(name)

# houses = {
#     "Harry": "Gryffindor",
#     "Draco": "Slytherian"
# }



# print(houses["Harry"])



# def square(a):
#     return a*a

# print(square(5))    

# if not > This can be used in a python function. It means,"If (condition) == 0...". 

# if not self.function():
#     return False
#If the function output equals 0, return 'False' 

# def square(x):
#     return x*x

# for i in range(10):
#     print(f"The squre of {i} is {square(i)}!")    

# x = int(input("Number: "))

# print(f"The number you chose is {x}")

# num = int(input("Number: "))

# if num > 0:
#     print("Number is positive.")
# elif num < 0:
#     print("Number is actually negative.")
# else:
#     print("I have no clue but think it might be 0.")

# dog = {
#     "breed": "Lab",
#     "name": "Chaco",
#     "fav_toy": "Ball"
# }

# print(dog["breed"])

# names = ["John", "Larry", "Bill"]

# for name in names:
#     print(name)

# Modules: used to help in bigger projects by having functions in one file and running them in another. For example, if I have a module named functions.py and loops.py, I would have to import the functions.py folder into loops.py via 'import functions' at top of my document. Once imported, and I wanted to call a function, I would use .notation >


# functions.py

# def mult(x)
#    return x*x

# *******************
# loops.py

# import functions
# 
# for i range(5)
    # print(f"The square of {i} is {functions.mult(i)}")

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# point1 = Point(3,5)

# print(point1.y)

# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, passenger):
#         if not self.open_seats():
#             return False
#         self.passengers.append(passenger)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)

# def announce(f):
#     def wrapper():
#         print("About to run the function")
#         f()
#         print("Done with function")

#     return wrapper

# @announce
# def hello():
#     print("Hello, world!")

# hello()    

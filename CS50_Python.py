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

if not self.function():
    return False
#If the function output equals 0, return 'False' 
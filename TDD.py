
# Python built-in testing framework that I need to import. Formerly called PyUnit.
import unittest

# Test Driven Development

# def isEven(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# class IsEvenTest(unittest.TestCase):
#     def testTwo(self):
#         # self.assertEqual(isEven(2), True)
#         self.assertTrue(isEven(2))

#     def testThree(self):
#         # self.assertEqual(isEven(3), False)
#         self.assertFalse(isEven(3))

#     def setUp(self):
#         print("Running Setup")

#     def tearDown(self):
#         print("Running tearDown tasks")

# if __name__ == "__main__":
#     unittest.main()

# The initial function (unit) is what we are testing to see if it works correctly.
# The class created inherits from unittest.TestCase and each subsequent function is a test to be run.
# Line 12: assertEqual(a,b) takes in two parameters. The first parameter is the outcome of the unit given its' specific parameter. Since 2 is even and will return "True", this is compared to the second parameter, "True". Since True == True, the test passes.
# Line 13: assertTrue() means bool(x) is True since isEven(2) is True.
# Line 17: assertFalse means bool(x) is False. Since isEven(3) is False, False == False and the test passes. Since both tests pass, we are given "Ok" in the terminal.

# def isOdd(x):
#     if x % 2 != 0:
#         return True
#     else:
#         return False

# class isOddTest(unittest.TestCase):
#     def testone(self):
#         self.assertEqual(isOdd(3), True)

#     def testwo(self):
#         self.assertEqual(isOdd(8), False)

#     # def setUp(self):
#     #     print("Running setUp")

# if __name__ == "__main__":
#     unittest.main()    

# def reverseList(some_list):
#     for x in range(int(len(some_list) / 2)):
#         some_list[x], some_list[len(some_list) - 1 - x] = some_list[len(some_list) - 1 - x], some_list[x]
#     return some_list

# class lsTester(unittest.TestCase):

# print(reverseList([3,6,8,9]))

# My mistake was using == vs. =. == used to compare values, = used to assign values. Since I was swapping values, I needed to assign values rather than compare.

# Swith some_list[x] with the last index of the list. In this case, it's 2 indexes, so, swith 0 & 2.
# Last Index = len(list) - 1 - x 

# mylst = [3,5,6,7,9]

# mylst2 = mylst[::-1]

# # mylst.reverse()

# print(mylst2)

# def sort(my_list):
#     # my_list.reverse()
#     # return my_list
#     my_list2 = my_list[::-1]
#     return my_list2

# a = [8,9,3]
# print(sort(a))

# names = ["bill", "bob", "sam"]

# print(names[:2])

# vars = [2,4,5,7,8,9,12]

# print(vars[1::2])

# Write tests first and ensure they fail, THEN go back and create the unit to runs tests on.
# *********************************************************************#
# The 'unit' we are going to run tests on.
# def reverse(some_list):
#     some_list.reverse()
#     return some_list

# # Create unit tests. These will be classes that inherit from (unittest.TestCase). Like other classes, these will have methods that are the individual tests to run.
# class unit_tests(unittest.TestCase):
#     # Each method is a test to run. We will see if the unit outcome asserts an equal value. If so, the function worked as the test is comprised of two lists in the opposite order of each other. The unit objective is to reverse the list given as an argument.
#     def test1(self):
#         self.assertEqual(reverse([1,3,5]), [5,3,1])
# # This sequence runs the tests.
# if __name__ == "__main__":
#     unittest.main()

# class tester(unittest.TestCase):

#     # def upper(self):
#     #     self.assertTrue("foo".upper(), "FOO")

#     # def upper(self):
#     #     self.assertFalse("foo".isupper())

#     def split(self):
#         x = "hello world"
#         self.assertEqual(x.split(), ["hello", "world"])

# if __name__ == "__main__":
#     unittest.main()
# ****************************************************
# Write a function that reverses a list and 3 test cases on the unit.
# def reverse(some_list):
#     some_list.reverse()
#     return some_list

# class tddTest(unittest.TestCase):

#     def test_1(self):
#         self.assertTrue(reverse([1,3,5]), [5,3.1])    

#     def test_2(self):
#         self.assertEqual(reverse([4,5,6]), [6,5,4])

#     def test_3(self):
#         self.assertTrue(reverse(["A", "B", "C", "D"]), ["D", "C", "B", "A"])

# if __name__ == "__main__":
#     unittest.main()        

# Check to see if word is a palindrome

def pal(word1):
    word2 = word1[::-1]
    if word2 == word1:
        return True
    else:
        return False

class palTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(pal("racecar"))

    def test2(self):
        self.assertTrue(pal("dad"))    

    def test3(self):
        self.assertEqual(pal("mom"), True)    


if __name__ == "__main__":
    unittest.main()
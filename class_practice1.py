# OOP #
# Consists of classes. Each class is made up of two things:
# Attributes: variables within a class
# Methods: functions within a class
# Each object created out of a class is called an "instance" of that class
# Methods that you do not want passed along to instances can be made "private". Default is "public" which means all methods & attributes will be passed along to each instance/object.

# class User:
#     def __init__(self, user_name, email_address):
#         self.name = user_name
#         self.email = email_address
#         self.account_balance = 0
#     def deposit(self, amount):
#         self.account_balance += amount
#     def withdraw(self, amount):
#         self.account_balance -= amount
#     def transfer(self, transferee, amount):
#         self.account_balance -= amount
#         transferee.account_balance += amount     

# guido = User("Guido Scaro", "guido@mail.com")
# terry = User("Terry Babbins", "terry@mail.com")
# guido.name = "Guido Scaramuzzi"
# guido.email = "guido@mail.com"
# guido.account_balance = 100

# guido.deposit(100)
# guido.deposit(150)
# guido.deposit(50)
# guido.transfer(terry, 50)
# print(terry.account_balance)
# print(guido.account_balance)


# print(guido.account_balance)

#When I set guido to equal the output given the parameters, those parameters get passed in to the method the object calls as "self". When "guido" calls the "deposit" method, name, email & account_balance all get passed in. This allows the method to interact with and potentially change the value of an attribute. In this case, account balance is changed because we have a method that adds the amount passed into it, along with self. This is also known as the implicit passage of self which is why we don't have to pass the argument itself when calling a method from an object > guido.deposit(100). The method will/can change the "account_balance" since it was passed in as "self" and properly identified in the method. 
# class User:
#     def __init__ (self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance=0)
# class BankAccount:
#     def __init__(self,int_rate=0, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#         else:
#             self.balance -= 5
#             print("Insufficient Funds")    
#         return self    

#     def display_info(self):
#         print(f"Account Balance: ${self.balance}")
#         return self

#     def int_yield(self):
#         if self.balance >= 0:
#             self.balance = self.balance + self.balance * self.int_rate
#         return self


# class User:
#     def __init__ (self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance=0)

#     def make_deposit(self, amount):
#         self.account.deposit(amount)
#         return self

#     def make_withdrawal(self, amount):
#         if amount <= self.balance:
#             self.account.make_withdrawal(amount)
#         else:
#             print("Insufficient Funds")
#             self.balance -= 5
#         return self

#     def display_balance(self):
#         self.account.display_info()    
#         return self

# jimbo = User("Jimbo Jones", "jimbo@mail.com")
# jimbo.make_deposit(100).display_balance()


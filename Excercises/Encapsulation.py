#Encapsulation

# Can be changed - public vars
class Student:
    def __init__(self):
        self.name = "Rakshit"

s = Student()

s.name = "NotRakshit"
print(s.name)

# Pvt vars - don't touch until yk what your'e doing

class Student:
    def __init__(self):
        self._name = "Rakshit"

s = Student()

print(s._name)

# Protected vars - py hides them so we can't print

class Student:
    def __init__(self):
        self.__name = "Rakshit"

s = Student()

print(s.__name)  ## error

"""
    👉 Practice Tasks for You
    1. Create class Employee with private salary
    2. Create class Bank with private balance and deposit method
    3. Create class Student with private marks and getter
    4. Create class Car with private speed and update method
    5. Prevent negative values using setter
"""

# Soln 1 ->

class Employee:
    def __init__(self):
        self.__salary = 80000

emp1 = Employee()
print(emp1.__salary)

# Soln 2 ->

class Bank:
    def __init__(self):
        self.__balance = 50000

    def deposit(self, amount):
        self.__balance += amount
        print('Amount deposited successfully')

    def show_balance(self):
        print('Current balance : ', self.__balance)

p1 = Bank()

p1.deposit(50000)
p1.showBalance()

# Soln 3 ->

class Student:
    def __init__(self):
        self.__marks = 67

s1 = Student()

print(s1.__marks)

# Soln 4 ->

class Car:
    def __init__(self):
        self.__speed = 67
    
    def update_speed(self, speed):
        if speed > 0:    
            self.__speed = speed

    def show_speed(self):
        print(self.__speed)

c1 = Car()

c1.update_speed(80)
c1.show_speed()

# Soln 5 ->

class Positive:
    def __init__(self):
        self.__value = 1

    def update_value(self, value):
        if value >= 0:
            self.__value = value
        
    def show_value(self):
        print(self.__value)

v1 = Positive()

v1.update_value(-80)
v1.show_value()
# Oops - I ( Classes and Objects)

# Eg - 
# class BankAcc:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def show(self):
#         print("Balance: ", self.balance)


# acc = BankAcc(1000)
# acc.deposit(500)
# acc.show()

"""
💡 Practice Tasks:
1. Create class Car with brand and price
2. Create class Rectangle to calculate area
3. Create class Student with name and marks
4. Create class Person with greeting method
5. Create bank account class with deposit function
"""

# Soln 1 ->
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

c1 = Car("Ford", 500000)
print("Brand: ", c1.brand)
print("Price: ", c1.price)


# Soln 2 ->
class rectangle: 
    def __init__(self, length, breath) : 
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath


A = rectangle(10, 20)
print(A.area())

# Soln 3->

class Student:
    def __init__(self , name, marks):
        self.name = name 
        self.marks = marks 

    def pr_name(self):
        print(self.name )

    def pr_marks(self):
        print("Marks:  ", self.marks)

Student1 =  Student( "rakshii" , 36)

Student1.pr_name()
Student1.pr_marks()


#Soln 4 ->
class person: 
    def __init__ (self, name):
        self.name = name  

    def myname(self):
        print("hello sensei : ", self.name)

final = person("Rakshit")

final.myname()

#Soln 5 ->
class bankaccount:
    def __init__(self, balance) :
        self.balance =  balance 

    def pr_balance(self):
        print("Your carried balance is =  " , self.balance)    

    def deposit(self, amount):
        finalamount = self.balance + amount
        print(finalamount)


rkacc = bankaccount(100)

rkacc.pr_balance()
rkacc.deposit(500)
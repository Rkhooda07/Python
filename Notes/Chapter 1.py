# Arithemtic opertor 

a=5
b=1
sum=a+b
diff=a-b
div =a/b
mul=a*b
sq=a**b  #a^b
mod=a%b #remainder 
print(sum) 
print(diff)
print(div)
print(mul)
print(sq) 
print(mod)

#relational operators

a=10
b=20

print(a==b) #false
print(a!=b)  #true
print(a>=b) #false
print(a<=b) #true
print (a<b) #true
print(a>b) #false

# assignment operators

num =20
num  **=10
print ("num :",num)

#logical operators

print (not False)
print (not True)

val1 = True
val2 = False
print("And operator : ",val1 and val2 )

a=5
b=10
print("Or operator : ",a==b or a<=b )


#type conversion (type casting)

a=int("5")
b=4.4
print(type(a))
sum = a+b
print (sum)

a=5.5
a=str("a")

print(type(a))

#Taking input values 

name= input ("Tell me your name : ")
print("Welcome -", name)

age = int (input ("what's yo age: "))
print("You entered :" , age)
print (type(age))


#practice time

#Q1-
num1= int (input ("num1 : "))
num2 = int (input ("num2 : "))
sum=num1+num2
print(sum)

# Q2-
a =float(input("Enter side of sq: "))
area = a*a

# print("Area of sq:", area)

#Q3- 
a = float(input("enter num1 : "))
b = float (input("enter num2: "))
avg = a+b/2
print("Average value of both numbers is : " , avg)

#Q4-
num1= int(input("enter num1:" ))
num2 = int(input("enter num2: "))

if a>=b:
    print ("TRUE")
else:
    print("FALSE")
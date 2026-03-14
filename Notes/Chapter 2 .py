# Strings 

str1= "This is a string"
str2= 'Rakshit hooda'
str3= """This is also a string"""

#To skip a line

str = "My name is Rakshit.\nI am learning Python" # \n to skip a line
str= "My name's rakshit .\ti study CS"             # \t to leave space for tab
print(str) 

str1 = "Rakshit"
len1 = len(str1)
print(len1)

str2= "Hooda"
len2= len(str2)
print (len2)

final_str=str1+" "+str2
print (final_str)
print (len(final_str))

#character

str = "Rakshit hooda"
print(str[2])

#Slicing

str= "Rakshit hooda"
print(str[:4])  #[0:4]
print(str[5:])  #[5:len(str)]
print(str[0:7])
print(str[8:len(str)])

#negative index -

str= "Rakshit hooda" #negative counting from backward
print(str[-5:-1])

# String functions-

str = "i am learning Python"
print(str.endswith ("on"))   # ""is a substr
print(str.capitalize())
print(str)
str= str.capitalize()
print(str)
print (str.replace("o", "a"))
print(str.replace("Python", "Javascript"))
print(str.find("o"))
print(str.find("from")) # -1 is invalid index
print(str.find("Python"))
print(str.count("a"))

#Practice questions - 

#Q1-
name = input("Enter first name : ")
length = len(name)
print("Length of your first name : ", length)

#Q2- 
str = "KR$NA dollor $ign one time"
ocr= str.count("$")
print(ocr)

#Conditional statements

marks = int(input("Enter your marks : "))
if (marks>=90):
    print("Grade -> A")
elif (marks>=80 and marks<90):
    print("Grade ->B")
elif (80>marks>=70):
    print("Grade ->C")
else:
    print ("Grade -> D")

#Nesting (writing a new statement in a statement if)
age = 77
if (age>=18):
    if (age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#Practice questions-

#Q1-
num =int(input("Enter a number : "))
if num%2==0:
    print("It is even no.")
else:
    print ("It is odd no.")

# Q2-
num1 = int(input("Enter 1st number -> "))
num2 = int(input("Enter 2nd number -> "))
num3 = int(input("Enter 3rd number -> "))
if (num1>=num2 and num1>=num3):
    print("greatest of all is : ",num1)
elif (num2>=num1 and num2>=num3):
    print("greatest of all is : ",num2)
else:
    print("greatest of all numbers is : ",num3)

#Q3- 
num= int (input("Enter a number : "))
if (num%7==0):
    print("Yes ,it is a multiple of 7")
else:
    print("No ,it is not a multiple of 7")
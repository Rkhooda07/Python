# Lists  (mutable)...can assign values 

marks =[74.5, 77.6, 33.5, 75.9]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

student= ["Rakshit",91.5, "Haryana"]
print(student[0])
student[0]="Rk hooda"  # Lists are mutable in Python
print(student)

#List slicing

marks= [54,78,25,93,53]
print(marks[1:3])       #ending index is not included
print(marks[:4])
print(marks[2:])
print(marks[-3:-1])

#List methods

list= [2,1,3]
list.append(4)  #adds one element at the end
print(list)
print(list.sort()) #sorts in ascending order
print(list)

list= ["apple", "banana", "carrot"]
print(list.sort(reverse=True)) #sorts in descending order
print(list)

list.reverse()  #reverse the list
print(list)

list=[1,7,4,1]
list.insert(4, 9)  #insert a value
print(list)

list.remove(1)  #Removes the first occurence of element
print(list)

list.pop(2)  #removes the value at index 2
print(list)

# TUPLES  (immutable)...can't assign values

tup = (2,1,4,3)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])

tup =() 
print(tup)
tup=(1)
print(tup)
print(type(tup))

tup= (1,)
print(tup)
print(type(tup))

tup= (1,3,2,5,3)
print(tup[1:3])
print(tup[1:3])
print(tup[0:])

print(tup.index(5))    #returns index of first occurence
print(tup.count(3))    # counts total occurences

#Practice questions-

#Q1- 
movies =[]
movies.append(input("enter 1st movie name : "))
movies.append(input("enter 2nd movie name: "))
movies.append(input("enter 3rd movie name : "))

print(movies)

#Q2- 
list =[1,2,3,2,1]
copy_list = list.copy()
copy_list.reverse()
if (copy_list==list):
    print("Yea , list is palindromic")
else:
    print("No the list is not palindromic")

list = [1,"abc", "abc" ,1]
copy_list= list.copy()
if (copy_list==list):
    print("Palindrome")
else:
    print("NOT palindrome")

#Q3-

grades = ("C","D","A","A","B","B","A")
print(grades.count("A"))     

#Q4-
grades =["C","D","A","A","B","B","A"]
grades.sort()
print(grades)
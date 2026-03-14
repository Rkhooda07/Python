# Loops  [Iterations - running in loop] (repeat instructions)

count =1
while count<=5:    #repeat until condition is true
    print("Hello") #some work 
    count+=1
print(count)

i=1
while i<=5:
    print("Rakshit", i)
    i+=1

#Print numbers from 1 to 10

i=1
while i<=10:
    print(i)
    i+=1
print("Loop ended")

#Print numbers from 10 to 1

i=10
while i>=1:
    print(i)
    i-=1
print("Loop ended")

#practice quesitons-

#Q1-
i=1
while i<=100:
    print(i)
    i+=1
print("Loop ended")

#Q2-
i=100
while i>=1:
    print(i)
    i-=1
print("Loop ended")

#Q3-
n= int(input("Enter number : "))
i=1
while i<=10:
    print(n*i)
    i+=1

#Q4-
nums = [1,4,9,16,25,36,49,64,81,100]

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3]) #...print(nums[len(nums)-1])

                    #  OR
idx=0
while idx < len(nums):
    print(nums[idx])   #num[0], num[1], num[2]...
    idx +=1

heroes =["ironman", "superman", "batman","thor"]

#traverse
i=0
while i < len(heroes):
    print(heroes[i])
    i+=1

#Q5-
nums = (1,4,9,16,25,36,49,64,81,100,36)

x=36
i=0  #initialization - starting value
while i<len(nums):
    if (nums[i]==x):
        print("Found at idx :", i)
        break
    else:
        print("finding:")
    i+=1

# Break

i=1
while i<=5:
    print(i)
    if (i==3):
        break
    i+=1

print("End of the loop")

#Continue

i=0
while i<=10:
    if (i==5):
        i+=1
        continue #skip
    print(i)
    i+=1

i=0           #To print even num
while i<=10:
    if (i%2 !=0): 
        i+=1
        continue #skip
    print(i)
    i+=1

#For loop   (Sequential traversal)

list =[1,2,3,4,5]

for nums in list:
    print(nums)

veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]

for val in veggies:
    print(val)

tup = (2,4,6,2,6,7)

for nums in tup:
    print(nums)

str = "RakshitHooda"
for char in str:
    print(char)
else:
    print("END")

#Practice questions

#Q1-
list = [1,4,9,16,25,36,49,64,81,100]
for num in list:
    print(num)

#Q2-
nums = (1,4,9,16,25,36,49,64,81,100)

x=25
idx=0
for el in nums:
    if (el==x):
        print("Found at idx :", idx)
    idx+=1

#Range  (returns sequence of nums)  range(start,stop,step)

print(range(5))

seq =range(5)
print(seq[0])
print(seq[1])

seq = range(10)

for i in seq:
    print(i)

             #OR
for i in range(10):     #range(stop)
    print(i)
for i in range(2,10):   #range(start, stop)
    print(i)
for i in range(2,10,2): #range(start,stop,step)
    print(i)

for i in range(2,100,2):   #even numbers from 1 to 100
    print(i)

for i in range(1,100,2):   #odd numbers from 1 to 100
    print(i)

#Practice questions

#Q1-
for num in range(1,101):
    print(num)

#Q2-
for num in range(100,0, -1):
    print(num)

#Q3-
n= int(input("Enter the number :"))

for i in range(1,11):
    print(i*n)
                    # OR
n=7
for n in range(7,71,7):
    print(n)

#Pass statement  (null statement that does nothing)

for i in range(10):   #used as placeholder for future code
    pass

if i>5:
    pass

print("Some useful work")

#Practice questions-

#Q1-
n=7

sum=0
for i in range(1,n+1):
    sum+=i

print("Total sum: ", sum)

                  #OR
n=100
sum=0
i=1
while i<=100:
    sum+=i
    i+=1

print("Total sum : ", sum)

#Q2-
n=5
fact=1

for i in range(1,n+1):
    fact *=i
    
print("Factorial of 7 : ", fact)

                #OR
n = 3
fact = 1
i = 1
while i<=3:
    fact *=i
    i+=1

print("Factorial of 3 : ", fact)
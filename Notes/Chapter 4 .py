# Dictionary  (mutable) 

info ={
    "key" : "value",   # key can also be str , int, floating value
    "name" : "Rakshit",
    "subjects": ["Python",  "C++" , "java"],
    "topics": ("dict" ,"set"),
    "age" : 17,
    "is_adult" : True,
    "marks" : 95.5
}

print(type(info))
print(info["name"])
print(info["age"])
info["name"] = "07" #overwrite
info["Surname"] ="Hooda"
print(info)

null_dict ={}
null_dict ["name"] ="Rakshit hooda"
print(null_dict)

# Nested dictionary 

student ={
    "name": "Rakshit hooda",
    "subjects" : {
        "phy": 73,
        "chem" :75,
        "maths" : 71
    }
}       

print(student["subjects"]["chem"])    

#Dictionary methods

print(len(student))          
print(list(student.keys()))    #returns all keys

print(list(student.values()))  #returns all values

pairs =(list(student.items()))   #returns all (key,val) pairs as tuples
print(pairs[0])

print(student["name2"])      #error
print(student.get("name2"))  #noerror -> None (returns the key acc. to value)

student.update({"city": "Delhi"})
print(student.get("city"))

new_dict = {"state" : "Haryana", "age" :17}
student.update(new_dict)
print(student)

# Set -> unordered -> unique values only(can't store dict and list as they're mutable)

collection = {1,2,4,4, "Hello" , "World", "World"}

print(collection)
print(type(collection))
print(len(collection))  #total no. of items

collection = set()   #syntax of empty set
print(type(collection))

#Set methods 

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1)
collection.add("Rakshit hooda")
collection.add((1,2,3))
collection.add([1,2,3])  #error bcz ist is unhashable i.e. mutable

collection.clear()

print(len(collection))

collection ={"Hello", "my", "name", "is", "Rakshit"}

print(collection.pop())
print(collection.pop())
print(collection.pop())

set1= {1,2,3}     #Union
set2= {3,4,5}

print(set1.union(set2)) #{1,2,3,4,5}
print(set1)
print(set2)

set1= {1,2,3}       #Intersection
set2= {2,3,4}

print(set1.intersection(set2))  #{2,3}

#Practice questions -

#Q1-
py_dict= {
    "table": ["a piece of furniture" , "list of facts and figure "],
    "cat": "a small animal"
}

print((py_dict))

#Q2-
subjects ={
    "python", "java", "c++", "python","javascript","java",
    "python","java","c++", "c"
}

print(len(subjects))

#Q3-
marks={}

x= int(input("enter phy marks: "))
y = int(input("enter chem marks: "))
z = int(input("enter maths marks: "))

marks.update({"phy":x, "chem": y, "maths": z})
print(marks)

#Q4-
set={9, "9.0"}  #if both values are same we can save them as str

print(set)
              # OR
set = {
    ("float" , 9.0),
    ("int", 9)
}

print(set)
#sum of (0 to 10)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = n[-1]
c=(a * (a + 1) / 2)
print(c)

# 5 fruits revers
fruits = ("Pine apple,apple,banana,Mango,Water melon")  
print("The original tuple is: ", fruits)  
reversed_fruits = fruits[::-1]  
print("The reversed_fruits is: ", fruits)

# Student Grades
Student_Grades ={"a":88,"b":72,"c":77}
print(Student_Grades)
Student_Grades["d"]=92
print(Student_Grades)
Student_Grades["c"]=90
print(Student_Grades)

# Unique Element
values = [1,4,4,5,8,7,9,1,0,6,2,3,9,8,2,5,8]
print("Original list:", values)
values_duplicate = set(values)
print("Set (no duplicates):", values_duplicate)

#List Comprehensio
squares = [x**2 for x in range(1, 11)]
print(squares)

#Unpacking Tuples
persons=("Teja",22,"Addanki")
name,age,city=persons
print(name)
print(age)
print(city)

#Merge two dictionaries
grades={
    "a":9.5,
    "b":9.0,
    "c":8.8
}
age={
    "a":25,
    "b":23,
    "c":24
}
merged_dict = {name: {"Grade": grades[name], "Age": age[name]} for name in grades}
print("Merged dictionary", merged_dict)

#Set Intersection and Union
set1={1,4,7,9,6,3}
set2={9,5,3,2,0,8}
intersection = set1.intersection(set2)
union = set1.union(set2)
print("value of intersection",intersection)
print("value of union",union)

#List to Dictionary Conversion
students_list = [("a", 8.8), ("b", 9.0), ("c", 9.2)]
students_dict = dict(students_list)
print("list of students",students_dict)

#Nested Directories
myDict = {
    "jk":{"a":88,"b":72,"c":77},
    "sk":{"a":80,"b":74,"c":71},
    "vk":{"a":78,"b":84,"c":70}
}
def print(name):
    if name in myDict:
        print(f"{name} grades:{myDict[name]}")
    else:
        print(f"student{name} not found.")

name = input("Enter the name : ")
print(name)
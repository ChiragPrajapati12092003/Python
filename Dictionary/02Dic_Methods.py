student = {
    "name" : "chirag prajapati",
    "subject" : {
        "map" : 56,
        "oopc" : 58,
        "toc" : 52,
        "python" : 60,
    }
}

print(student.keys()) #returns all keys in form of list

print(list(student.keys())) #typecast , it returns in form of list

print(len(student))
print(len(list(student.keys())))

print(student.values())#returns all values of dic.
print(list(student.values()))#returns all values of dic.
#we can store dic into list and list into dic

print(student.items()) #returns all (key,value) pairs as tuple
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])
print(pairs[1])

print(student["name"])
print(student.get("name")) #returns the key according to value or visaversa

# agar kabhi hamne likne mai galti ki toh
# print(student["name2"]) #yeh hame error dega jise uske baad code run hi nai hoga
# print(student.get("name2")) #or yeh sirf None print karvayegi

student.update({"city" : "gandhinagar"})
print(student)


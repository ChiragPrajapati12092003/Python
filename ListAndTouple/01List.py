# #in python strings are immutable and lists are mutable

# marks1 = 94.4
# marks2 = 87.5
# marks3 = 95.2
# marks4 = 66.4
# marks5 = 45.1

# #agar ham thode se hi data ko store karne ke liye new variable banate rahenge to phir unlo track karna muskil ho jayega so unko ek hi variable mai store karke rakh sakte hai 

# marks = [94.4, 87.5, 95.2, 66.4, 45.1] #list
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ["chirag",56,"engineer"]
# print(student[1])
# student[1]=55
# print(student)
# print(student[5]) #5th number ki index hai hi nai to phir koi value nai aayegi  


#not possible in string
# str = "hello"
# print(str[0])
# str[0]="y"

#yaha par bhi slicing ka same hi fanda hai jaisa string mai tha
Marks = [85, 94, 76, 63, 48]
print(Marks[1:4])
print(Marks[-3:-1])
print(Marks[1:])
print(Marks[:3])
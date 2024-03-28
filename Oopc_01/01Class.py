#name of class always start with capital latter
class Student:
    name = "anonymas" # class attribute
    college_name = "ABC college"

    # #default constructor
    # def __init__(self):
    #     pass

    #parameterized constructors    
    def __init__(self, fullname,marks): #self always first rahega usko kuch bhi bol sakte hai like abcd uske baad kuch bhi variable le sakte hai
        # print(self)
        self.name = fullname # sabhi student ka name alag hoga aur marks bhi so isse obj.attr kehte hai 
        self.marks = marks #obj.attribute > class attribute
        print("adding new student in database") #this is constructor 

# To access karne ke liye object banana padta hai

s1 = Student("chirag",98)  #object air yaha par automatically constructor call ho jayega
print(s1.name,s1.marks) #chirag
# print(s1)    

s3 = Student("shaurya",88)
print(s3.name,s3.marks)
print(s3.college_name)
print(Student.college_name)

# s2 = Student()
# print(s2)

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)    
# print(car1.brand)    
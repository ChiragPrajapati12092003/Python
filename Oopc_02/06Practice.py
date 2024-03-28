
#Que = 1
# Define a circle class to create a circle with radius r using the constructor
#also define an area() method for calculate area
#and define perimeter() method for calculate perimeter

# class Circle:
#     def __init__(self,radius):
#         self.radios = radius

#     def area(self):
#         return (22/7) * self.radios **2

#     def perimeter(self):
#         return 2*(22/7)*self.radios    

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


# Que = 2
# Define a Employee class with attribute role,department & salary.This class also showDetails() method
 

# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =",self.role)    
#         print("dept =",self.dept)    
#         print("salary =",self.salary)    

# e1 = Employee("accountant" , "Finance" , "60,000" )    
# e1.showDetails()  

#Create Engineer class that inherit properties from employee & has additional attribute name & age

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT","75,000")

# engg2 = Engineer("Chirag" , 20 )
# engg2.showDetails()         



# Que = 3
#Create a class called Order which stores item & its price.
#   Use dunden function __gt__() to convay that:
#      order1>order2 if price of order1>order2  


class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price


    def __gt__(self,order2):
        return self.price > order2.price    


order1 = Order("Chips",20)        
order2 = Order("tea" ,15)

print(order1>order2) #True

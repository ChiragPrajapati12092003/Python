# # When one class(child / derived) derives the properties & methods of another class(parent / base)

# --------------This is single inheritance------------
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")    


# class TyoyotaCar(Car):
#         def __init__(self,name):
#              self.name = name

# car1 = TyoyotaCar("fortuner")
# car2 = TyoyotaCar("prius")   

# print(car1.name)
# print(car1.start()) #here start() method is used bcx it's inherited
# print(car1.color)




# ----------------------multi-level inheritance---------------

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")    


# class TyoyotaCar(Car):
#         def __init__(self,brand):
#              self.brand = brand

# class Fortuner(TyoyotaCar):  #we can access all properties of all above class
#      def __init__(self,type):
#           self.type = type             


# car3 = Fortuner("diesel")
# print(car3.start())


# -----------------Multiple inheritance--------------

# derived calss is inherit properties more than one parent class

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#         varC = "welcome to class C"

# c1 = C

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)



# ------------------Super Method-------------

#super() method is used to access methods of the parent class.

class Car:
    def __init__(self,type):
         self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")    


class TyoyotaCar(Car):
        def __init__(self,name,type):
             super().__init__(type) # now it can access whole constructor or method here  
             self.name = name
             super().start()

car1 = TyoyotaCar("prius","electric")
print(car1.type)    # is not valid without super method bcz it not have access for type which are self         
# Total Types of methods : (1) staticmethod
#                          (2) classmethod (cls)
#                          (3) instance or normal methods (self)

# class Person:
#     name = "anonymous"

#     def changeName(self,name):
#         self.name = name

#         # Person.name = name #isse bhi main class ka attribute change ho sakta hai
#         # self.__class__.name = "Chirag" # isse bhi kar sakte hai

# p1 = Person()
# p1.changeName("Chirag Prajapati")
# print(p1.name)    #yaha par naya hi attribute create ho rah hai jisse jo main class hai vaha par koi fark nai padega

# print(Person.name)    # yaha par to anonymous aata hai jab self.name use kare tab




# ------agar ham function ke andar hi class ko use kar paye ---

# A class method is bound to the class & receives the class as an implcit first argument.

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name


p2 = Person()
p2.changeName("Chirag")    
print(p2.name)    
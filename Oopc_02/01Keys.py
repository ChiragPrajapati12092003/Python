# ----------------Delete key----------------

#used to delete object properties or object itself.

# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("chirag")  
# print(s1.name)      
# del s1
# print(s1.name)



# -------------------------private key------------------

#used to create private attribute

# class Account:
#     def __init__(self, acc_no , acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # we can make prive by apply (__) at starting

#     def reset_pass(self):
#         print(self.__acc_pass) # wecan access acc_pass in class only


# acc1 = Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())
# # print(acc1.acc_pass) # we cannot access this outside of class bcz it's private

class Person:
    __name = "abcd"

    def __hello(self):             #it's private method
        print("hello person!")

    def welcome(self):
        self.__hello()


p1 = Person()
# print(p1.__name)    #it's private so we can't access it
print(p1.welcome())        #yaha par p1 welcome ko call karega and welcome hello ko call karega
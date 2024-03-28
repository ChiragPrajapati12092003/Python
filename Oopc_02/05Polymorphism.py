# Polymorphism => bahot sare forms means ek hi chij ko different different ways se use kiya jaye
# in Python we have best example of polymorphism is operator oveloading
#when the same operator is allowed to have different meaning according to the context

# print(1 + 2) # 3
# print (type(1))

# print("apna" + " college") # concatenate
# print(type("apna"))

# print([1,2,3] + [3,4,5,6]) #merge
# print(type([1,2,3]))
# #yaha par number ke time pe + ka matlab alag hai and string ke time pe + ka matlab alag hai and  list ke time pe bhi alag hai



#yaha par ham + ko apne hisab se use kar sakte hai

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +" , self.img, "j")

#normal function
    # def add(self , num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img   
    #     return Complex(newReal,newImg)
        
# this is dundon function 
               
    def __add__(self , num2): 
        newReal = self.real + num2.real
        newImg = self.img + num2.img   
        return Complex(newReal,newImg)
    
    def __sub__(self , num2): 
        newReal = self.real - num2.real
        newImg = self.img - num2.img   
        return Complex(newReal,newImg)
        
        

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

# print(num1+num2) #hame yeh direct likhne se answere aa jana chahiye

# num3 = num1.add(num2)
# num3.showNumber()

#python doen't know how to add complex number so we have to create it with dunder functions

num4 = num1 + num2
num4.showNumber()

num5 = num1 - num2
num5.showNumber()
# jab koi attribute ki value kisi function pe depend kare to function ko hi property banayenge
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math ) / 3) + "%" #isko hum @property mai likhenge bcz yeh function pe depend karta hai


    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math ) / 3) + "%"  #OR

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math ) / 3) + "%"      

stu1 = Student(98,56,99)
print(stu1.percentage)  

stu1.chem = 86
print(stu1.chem) #yaha par marks change kiya hai vo update bhi ho jayega par percentage direct update nai hoga 
# print(stu1.percentage)#yaha par old percentage hi aayega

# stu1.calcPercentage()
# print(stu1.percentage) #yaha par new percentage aayenge

print(stu1.percentage)#ab latest value aayegi


'''
light = input("showed light color : ")
if(light == "red"):
    print("Stop")  #yaha par 4 space ka gap aayega 
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")            


Marks = int(input("Marks : "))
if(Marks >= 90):
    print("A")
elif(Marks >= 80 and Marks <90):
    print("B")
elif(Marks >=70 and Marks <80):
    print("C")
else:
    print("D")           


A = int(input("A : "))
G = input("M or F :")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")       '''

#Single Line If  OR  Ternary Operator

# food = input("food : ")
# eat =  "yes" if food == "cake" else "no"
# print(eat)

# food2 = input("food2 : ")
# print("Sweet") if food2 == "cake" or food2 == "jalebi" else print("not Sweet " , food2)


#clever if  OR  Ternary Operator
   
age = int(input("age :"))
vote = ("yes","no") [age <= 18]
print(vote)

sal = float(input("Salary : "))
tax = sal*(0.1,0.2) [sal >= 50000]
print(tax)
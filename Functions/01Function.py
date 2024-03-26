# Block of statement that perform a specific task
#if we want accest same things in whole file again and again then function is used to reduce code 
#helps to reduce reapatibility  (retendant code)


# a = 5
# b = 10

# sum = a + b
# print(sum)

# more lines of code 

# a = int(input("Enter a :"))
# b = int(input("Enter b :"))

#function defination
# a and b are parameters in functions
# def calc_Sum(a,b):
#     # sum = a + b
#     # print(sum)
#     # return sum
#     return a + b

# calc_Sum(a,b) #it's act as functioncall to print the output of the sum, here a nad b are act as arguments 
# calc_Sum(10,20)

#to use return direct we have to store the value of retuen in some variable and then return that or print that
# sum2 = calc_Sum(a,b)
# print(sum2)

# def print_hello():  #it does'nt have any return value or input or any parameters
#     print("hello")

# print_hello()    
# print_hello()    
# print_hello()    

# output = print_hello()
# print(output)    #it's give None bcz it doen't returns anything
    

#average of 3 numbers
c = int(input("Enter the value 1 :"))
d = int(input("Enter the value 2 :"))
e = int(input("Enter the value 3 :"))

def avg(c,d,e):     #we have to pass perameters if we want to call this function for given parameters
    avg = (c + d + e )/3
    print(avg)
    return avg
avg(c,d,e)
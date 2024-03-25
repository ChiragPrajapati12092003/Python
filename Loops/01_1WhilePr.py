#Que = 1
#print numbers from 1 to 100

# i = 1
# while i<=100:
#     print(i)
#     i +=1

#Que = 2
#print numbers from 100 to 1
    
# j =  100
# while j >= 1:  #stoping condition
#     print(j)
#     j -=1   


# Que = 3
#Print the multiplication table of a number n

# n = input("Enter the number :")
# p = 1
# while p <= 10:
#     print(n*p)
#     p += 1                 #this code prints pattern by mistake


# n = int(input("Enter the number :"))
# p = 1
# while p <= 10:
#     print(n*p)
#     p += 1                 #we have provide  type into input



# Que = 4
#print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]
#is methos ko traverse

# num = [1,4,9,16,25,36,49,64,81,100]
# heros = ["ironman","superman","batman","aquaman","thor","odin","loki"]

# indx = 0
# while indx < len(num):
#     print(num[indx])
#     indx +=1 

# index = 0
# while index < len(heros):
#     print(heros[index])
#     index += 1    


# Que = 5
#Search for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter the element or number : "))

r = 0 #initialization
while r < len(tup):
    if(tup[r] == x):
        print("Founde at idx ", r)
    else:
        print("Not Found")    
    r += 1

# QUE = 1 
# write a recursive function to calvulate the sum of first n natural numbers

def sum(n):
    if(n == 0):
        return 0
    return sum(n-1) + n

Total = sum(10)
print(Total)  


# QUE = 2
#write a recursive function to print all elements in a list
#Hint : use list and index as parameter



def print_list(list,indx=0):
    if(indx == len(list)):
        return
    print(list[indx])
    print_list(list,indx+1)

fruits = ["mango","banana","apple","litchi"]   
print_list(fruits) 
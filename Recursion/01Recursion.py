# When a function calls itself repeatedly
#recursive function
# def show(n):
#     if (n == -1): #Base case dena padega varna infinite loop ho jayega
#         return
#     print(n)
#     show(n-1)
#     print("end") #layer by layer(call stack) upar jayega aur firse bapas aayega jisse end 6 baar print o raha hai yaha par

# show(5)    # we want to print 5,4 = n-1,3 = n-2,2 = n-3,1 = n-4


#for factorial
# n! = (n-1)! * n    recursive relation
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))    
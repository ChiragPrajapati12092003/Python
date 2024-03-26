# QUE = 1
# WAP to print the length od a list. (list is the parameters)

cities = ["delhi","ahmedabad","pune","mumbai","deesa","palanpur"]
heros = ["thor","ironman","shaktiman"]

# len(cities) #direct way or default function

# def print_len(list):
#     print(len(list))


# print_len(cities)
# print_len(heros)


# QUE = 2
# Write a function to print elements of a list in a single line.(list is the parameters)

# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(cities)
# print()
# print_list(heros)



# QUE = 3
#WAF to find the factorial of n.(n is the parameters)


# this is the logic behind it
# n = 5
# fac = 1
# for j in range(a,n+1):
#     fac *= j
# print(fac)    

# n = int(input("Enter the number :"))
# def cal_fact(n):
#     fact = 1
#     for j in range(1,n+1):
#         fact *= j
#     print(fact)    

# cal_fact(n)    


# QUE = 4
#WAF to convert USD to INR
n1 = float(input("Enter the value :"))
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =", inr_val , "INR")
 
converter(n1) 
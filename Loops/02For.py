# used for sequential traversal

# nums = [1,2,3,4,5]

# for val in nums:
#     print(val)

# veggies = ["potato","brinjal","ladyfinger","cucumber"]    

# for val2 in veggies:
#     print(val2)

# tup = (5,5,7,6,8,3,8)

# for num in tup:print(num) #gives all vlues inside tuple


# str = "apnacollage"

# for char in str:
#     print(char) #returns all the word one by one
# else :
#     print("END")    #pura loop khatam hone ke baad yeh run hoga

#else ki jarurt kyu padi 
#agr ham kabhi upar break likh de to phir uske baad ka loop to run hoga nai so agar koi kaam hame loop khatam karne ke turant baad karna hai to else mai likh dena aur vo pura loop khatam hone ke baad hi run hoga agar loop khatam nai hua to phir to else run nai hoga


str1 = "Chiragprajapati"

for char1 in str1:
    if(char1 == 'p'):
        print("p founded")
        break
    print(char1)
else:
    print("End")  
print("End2")      
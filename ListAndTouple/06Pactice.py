# WAP to check is a list contains a palindrome of elements.(Hint: use copy() method)
#palindrome words =  jisko samne se ya piche se padhe same hi hoga (maam,racecar)
#copy method returns shallow copy of list

# list = []
# list.append(input("Enter 1st elemet of list : "))
# list.append(input("Enter 2nd elemet of list : "))
# list.append(input("Enter 3rd elemet of list : "))
# list.append(input("Enter 4th elemet of list : "))

# print(list)

# rev = list.reverse()
# print(rev)

# if(list == rev):
#     print("List are palindrome")
# else:
#     print("List is not palindrome") 

#this approach is not working so go with another method


list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("palindrome")
else:
    print("not palindrome")    

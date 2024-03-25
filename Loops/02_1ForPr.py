# Que = 1
# Print the elements of the folloeing list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]

# for el in nums:
#     print(el)

#Que = 2
#Search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]     

nums2 = [1,4,9,16,25,36,49,64,81,100,49]
x = 49

index = 0
for el2 in nums2:
    if(el2 == 49):
        print("number us found at index :", index )
        # break #if we want only found one time
    index += 1    
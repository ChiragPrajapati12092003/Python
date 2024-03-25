# i = 1
# while i<=5:
#     print(i)
#     if (i == 3):
#         break            #yaha par 3 aate hi break ho jayega aur pura loop stop ho jayega par loop ke ageka code run hoga
#     i += 1
# print("Loop Ended")    


# j = 0
# while j<=5:
#     if(j == 3):
#         j += 1  #yaha par 3 skip ho jayega
#         continue  #act as skip means yaha par condition true ho jaye to phir yeh aage ke sabhi steps ko skip kar dega aur loop firse continue hoga 
#     print(j)
#     j += 1

k = 1
while k<=10:
    if(k %2 != 0):
        k += 1
        continue  #act as skip means yaha par condition true ho jaye to phir yeh aage ke sabhi steps ko skip kar dega aur loop firse continue hoga 
    print(k)
    k += 1    
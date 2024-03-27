# as means alias means tony stark => ironman ham use kuch bhi bol sakte hai
#yaha par close statement nai likhni padti kyu ki vo automatically ho jata hai
with open("D:\Python_Codes\Python\Files_Operations\demo3.txt","r") as f:
    data=f.read()
    print(data)

with open("D:\Python_Codes\Python\Files_Operations\demo3.txt","w") as f:
    f.write("new data")    
# Create a new file "practice.txt" using python. add some data

# Que = 1
# with open("D:\Python_Codes\Python\Files_Operations\Practice\ practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using python.\nI like programming in python.")


# Que = 2
#WAF that replaces all occurrence of "python" with "java" in above file 

# with open("D:\Python_Codes\Python\Files_Operations\Practice\ practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("python","Java")
# print(new_data)

# with open("D:\Python_Codes\Python\Files_Operations\Practice\ practice.txt","w") as f:
#     f.write(new_data)


# Que = 3
# Search if the world "learning" is exixts in the file or not


# with open("D:\Python_Codes\Python\Files_Operations\Practice\ practice.txt","r") as f:
#     data = f.read()
#     word = "learning"
#     if(data.find(word) != -1):
#         print("learning is found")
#     else:
#         print("Not found")    


#with use of function

# def check_for_word():
#     word = "learning"
#     with open("D:\Python_Codes\Python\Files_Operations\Practice\ practice.txt","r") as f:
#          data = f.read()
#          if(data.find(word) != -1):
#              print("learning is found")
#          else:
#              print("Not found") 

# check_for_word()             



# Que = 4
#WAF to find in which line of the file does thw word "learning" occurs first.
#print -1 if word not found

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("D:\Python_Codes\Python\Files_Operations\Practice\ practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1   
#     return -1         
# print(check_for_line())


# Que = 5
# From a file containing numbers separated by comma,print the count of even numbers.
#yaha pr hame (1)individual numbe nikalna padega
            # (2)pass / casting to integer

count = 0
with open("D:\Python_Codes\Python\Files_Operations\Practice\practice2.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count += 1
print(count)            
           

# using without split method  => nums = data.split(",") yeh vala logic na aaye to 
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]     
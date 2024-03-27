#open("file_name","mode") #nfile_name = name file one which you want to perform any task , mode => read or write


#Useful modes and we can combine modes also
# r => open for reading(default)
# w => open for writing,truncating the file first 
# x => create new file and open it for writing
# a => open for writing,appending to the end of the file if it exists
# b => binary mode
# t => text mode (default)
# + => open a disk file for updating(reading amd writing)


# ---------------------Rading from file---------------

f = open("D:\Python_Codes\Python\Files_Operations\demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))

# data2 = f.read(5) 
# print(data2) # it only returns no of characters
# f.close()

# line1 = f.readline() #only print 1st line
# print(line1)

# line2 = f.readline() #returns line 2
# print(line2)

#ager koi file ek baar read ho jaye to phir usko dusri baar read nai karva sakte uski jagah vo empty space print karvayega

# -----------------Writing from file-------------------

# f1 = open("D:\Python_Codes\Python\Files_Operations\demo2.txt","w")

# f1.write("My name is chirag not python")

# f1.close()

# f2 = open("D:\Python_Codes\Python\Files_Operations\demo2.txt","a")

# f2.write("\nI am learning python")

# f2.close()

# f3 = open("D:\Python_Codes\Python\Files_Operations\ notexisting.txt","w")  #yeh file thi hi nai lekin agar ham use append ya write kare to phir vo file create ho jati hai
# f3.close()

f4 = open("D:\Python_Codes\Python\Files_Operations\demo.txt","r+") #yaha par r+ => reading + writing but file truncate nai hoti yani ki file mai se data delete nai hota
f4.write("abc") #yaha par data overwrite hota hai means jaha tak ham likhenge utna hi data delet hoga
print(f4.read()) #pointer jaha par aata hai vaha se hi print hota hai means ab pointer abc ke baad aa gaya so ab abc ke baad vala print hoga
f4.close()

#W+ vale mai puri file delete ho jayegi aur phir vaha se likhna suru
#a+ vale mai read + append hota hai aur pointer end mai hota hai jisse read mai kuch bhi print nai hoga aur yaha par no truncate 
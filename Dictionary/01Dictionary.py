#Dict. are used to store data values in key:value pairs

#keys can be integer,float,string  but not dic or list bcz they are mutuable
# they are unordered(kisi bhi oder mai likh sakte hai),mutuable(changable) & don't allow duplicate keys(not allow same keys)

info = {
    "name" : "chirag",
    "subjects" : ["python","C","java"],
    "topics" : ("dict","set"),
    "learnig" : "coding",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4,
    12 : 64854
}

# print(info)
# print(info["name"])
# print(info["age"])
# print(info["topics"])
# print(type(info))

# info["age"] = 20 #overwrite so value will be latest 
# info["surname"] = "prajapati"
# print(info)

# nul_dic = {}
# print(nul_dic)
# nul_dic["name"] = "apnacollage"
# print(nul_dic)


#-------------------------------------nasted dic----------------------------

student = {
    "name" : "chirag prajapati",
    "subject" : {
        "map" : 56,
        "oopc" : 58,
        "toc" : 52,
        "python" : 60,
    }
}
print(student)
print(student["subject"])
print(student["subject"]["map"])
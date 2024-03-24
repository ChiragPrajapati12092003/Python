str = "i am a coder coder"

print(str.endswith("er"))
print(str.endswith("re"))

print(str.capitalize())# it does't change original string
# str = str.capitalize #now it changes main string
print(str)

print(str.replace("a","e"))#replace a=>e
print(str.replace("coder","gamer"))

print(str.find("a"))#it returns index of word a
print(str.find("coder"))#it returns starting index of word coder
print(str.find("g"))#it gives index -1 which invalid in string 

print(str.count("a"))#gives no of a which present in string
print(str.count("coder"))
#most imp thing : sets are mutuable but the elements inside it are immutable
# immutable value hi add kar sakte hai set mai bcz unki hash value same(hashable) milti hai

collection = set()

collection.add(1) #add element 1 inside
collection.add(2)
collection.add(2) #dublicate is ignored
collection.add("apple")
collection.add((1,2,3)) #tuple pass ho sakti hai
# collection.add([1,2,3]) #list pass nai ho sakti

collection.remove(1)
# collection.remove(7) #key erro bcz key =  value and yaha par 7 number ka koi element hai hi nai

collection.clear() #remove all the values from set


print(collection)
print(len(collection))


collection2 = {"hello","apnacollage","world","coding","python"}
print(collection2.pop()) #gives random value from set

set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2)) #it does't affect original sets
print(set1.intersection(set2))
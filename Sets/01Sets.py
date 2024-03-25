#set is the collaction of the unordered items.
#each element in the set must be unique & immutable
#dic. and list are not stored in to sets bcz they are mutuable

collection  = {1,2,3,4,3,4,"hello","world","world"}
print(collection) #kahi bhi kabhi bhi print ho sakta hai kyuki uski index nai hai
print(type(collection))
print(len(collection))#dublicate is not allowed

collection2 = {} #is also same as empty dic.
print(type(collection2))

collection3 = set() #is empty set
print(type(collection3))

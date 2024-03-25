#tuple are immutable like string
tup = (87,64,33,95,76)
tup0 = (87,64,33,95,76,)
print(tup)
print(tup0)
print(type(tup))
print(type(tup0))#are valid for last comma 
print(tup[0])

#assign of value is not possible here

tup2 = () #empty tuple is valid here
tup3 = (1)
tup4 = (1,)#if comma is there then its called tuple
tup5 = (1.05)
tup6 = ("hello")
tup7 = ("hello",)

print(tup2)
print(type(tup2)) #tuple
print(type(tup3)) #int
print(type(tup4)) #tuple
print(type(tup5)) #float
print(type(tup6)) #string
print(type(tup7)) #tuple

#slicing are also valid here 
tuple = (1,2,3,4)
print(tuple[1:3])
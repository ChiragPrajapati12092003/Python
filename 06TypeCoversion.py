# Type Con.
a = 2
b = 4.25

sum = a + b  # float > int
print(sum) # 2.0 + 4.25 => 6.25

c = int("2")
d = 4.25

#e = int(c) #covert it into integer

print(type(c))
# print(type(e))
# print(e + d)
print(c + d) # not evaluated

#we cant convert full name string into integer or float
# x = int("chirag") #it gives an error
# print(type(x))

p = 3.14
q = str(p)
print(type(q))
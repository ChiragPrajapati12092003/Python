list = [2,1,3]

list.append(4) #list mutation yani ki ham list mai change kar sakte hai
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(2,10) #add element 10 at index 2
print(list) #ans = [1,2,10,3,4]

list.remove(10)#remove the value 10
print(list)

list.pop(3)#remove element which are peresent at index 3
print(list)

fruits = ["banana" , "litchi" , "apple"]
fruits.sort() #yaha par sorting abcd se hogi
print(fruits)
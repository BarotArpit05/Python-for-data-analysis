friends=["apple","banana",34,56.43,"hello"]
print(friends)
#method of list are :- sort,reverse,append,insert,pop,remove
friends.append("Hari")
print(friends)

#sort not works with string 
f=[2,3,2,1,5,43,2222,55,34,3]
f.sort()
print(f)
#reverse method
f.reverse()
print(f)

#insert method is used to insert an item at specific location in list
f.insert(1,234)#first arg reprresent index and second arg represent object you want to enter
print(f)

#pop method is used to  delete element from specific index
f.pop(2)
print(f)
#remove method is  to  remove element from list
f.remove(43)
print(f)


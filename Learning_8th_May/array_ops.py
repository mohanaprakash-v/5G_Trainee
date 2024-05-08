from array import *
#insertion operation in array
arr = array('i',[2,3,4,7,6])
print(f"Before inserting an element: {arr}")
arr.insert(1,8)
print(f"After inserting a element is: {arr}")

#deleting operation in array
brr = array('i',[1,2,3,4,5,6])
print(f"Before deleting an element: {brr}")
brr.pop(2)
print(f"After deleting an element: {brr}")

#searching operation in array
crr = array('i',[1,2,3,4,5,6])
num = 5
for i in range(0, len(crr)):
    if crr[i] == num:
        print(f"Element present at the index: {i}")
        break

#accessing an element in a array
drr = array('i',[1,2,3])
a=drr[2]
print(f"Element at 2nd index is: {a}")

#slicing in array
g = [1,2,3,4,5,6,7,8]
err = array('i',g)
print(f"Sliced array: {g[2:5]}")
print(f"Printing all elements using slicing operator: {g[:]}")

#counting elements in array
e = [1,1,1,3,4,5,1]
frr = array('i',e)
count=0
for i in range(len(e)):
    if e[i] == 1:
        count+=1
        print(f"1 occured at indexes: {i}")
print(f"Number of times 1 occurred: {count}")

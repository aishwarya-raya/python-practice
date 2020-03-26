# Write your code here :-)
#a python function that returns common elements from two lists as a list
print('Enter the values into the list1: ')
list1=list(set(map(int,input().split())))
print('Enter the values into the list2: ')
list2=list(set(map(int,input().split())))
print(list1)
print(list2)
flist=[]
for num in list1:
    if num in list2:
        flist.append(num)
print(flist)

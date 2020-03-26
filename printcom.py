# Write your code here :-)
# a python program that returns true if two lists have atleast one common member
print('Enter the values into the list1: ')
list1=list(set(map(int,input().split())))
print('Enter the values into the list2: ')
list2=list(set(map(int,input().split())))
print(list1)
print(list2)
n=False
for num in list1:
    if num in list2:
        n=True
        break
print(n)

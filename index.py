 # Write your code here :-)
# to find index of an item in a specified list
print('Enter the values into the list1: ')
list1=list(set(map(int,input().split())))
print(list1)
num=input('Enter the number whose index is to be found ')
print(list1.index(int(num)))

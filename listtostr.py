# Write your code here :-)
# to convert list of characters into a string
print('Enter the values into the list1: ')
list1=map(str,input().split())
print(list1)
s=''
for ch in list1:
    s+=ch
print(s)

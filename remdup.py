# Write your code here :-)
# a python program to remove duplicates from a list
print('Enter the values into the list: ')
spam=map(int,input().split())
flist=[]
for num in spam:
    if num not in flist:
        flist.append(num)
print(flist)

# Write your code here :-)
# a menu driven program for a simple calculator
print('Simple Calculator')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
ans='y'
while ans=='y':
    print('Enter your choice')
    ch=input()
    print('Enter the two numbers:')
    no1=input()
    no2=input()
    if ch=='1':
        r=int(no1)+int(no2)
        print('The sum='+str(r))
    elif ch=='2':
        r=int(no1)-int(no2)
        print('The difference='+str(r))
    elif ch=='3':
        r=int(no1)*int(no2)
        print('The product='+str(r))
    elif ch=='4':
        r=int(no1)/int(no2)
        print('The quotient='+str(r))
    print('If you want to continue, enter "y"')
    ans=input()

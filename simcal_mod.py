# Write your code here :-)
# Write your code here :-)
# a menu driven program for a simple calculator
print('''Simple Calculator
1.Addition
2.Subtraction
3.Multiplication
4.Division''')
ans='y'
while ans=='y':
    print('Enter your choice')
    ch=input()
    no1,no2=input('Enter the two numbers:').split()
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

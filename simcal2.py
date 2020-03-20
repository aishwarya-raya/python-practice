# Write your code here :-)
# a program to enter expressions into a simple calculator
no1,op,no2=input('Enter your expression: ').split()
if op=='+':
    print(no1+op+no2+'='+str(int(no1)+int(no2)))
elif op=='-':
    print(no1+op+no2+'='+str(int(no1)-int(no2)))
elif op=='*':
    print(no1+op+no2+'='+str(int(no1)*int(no2)))
elif op=='/':
    print(no1+op+no2+'='+str(int(no1)/int(no2)))

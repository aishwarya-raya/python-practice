# Write your code here :-)
# a program to enter expressions into a simple calculator
ch='y'
while ch=='y':
    n=0
    c='y'
    no1,op,no2=input('Enter your expression: ').split()
    while c=='y':
        if n>0:
            print(ans)
            op,no2=input().split()
        if op=='+':
            ans=int(no1)+int(no2)
        elif op=='-':
            ans=int(no1)-int(no2)
        elif op=='*':
            ans=int(no1)*int(no2)
        elif op=='/':
            ans=int(no1)/int(no2)
        print(str(no1)+op+no2,'=',ans)
        no1=ans
        n=n+1
        print('Would you like to continue here?')
        c=input()
    print('Would you like to start another operation?')
    ch=input()

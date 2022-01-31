#coded by harish rane

n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
n3 = int(input("Enter the third number"))

#approach 1
'''
if n1>=n2 and n1>=n3:
    print(f'{n1} is largest')
elif n2>=n3:
    print(f'{n2} is largest')
else:
    print(f'{n3} is largest')

'''

#approach 2

if n1==n2 and n2==n3:
    print("all the numbers are same")
else:
    if n1>n2:
        if n1>n3:
            print("%d is largest number"%n1)
        else:
            print("%d is largest number"%n3)
    elif n2>n3:
        if n2>n1:
            print("%d is largest number"%n2)
        else:
            print("%d is largest number"%n1)
    elif n3>n1:
        if n3>n2:
            print("%d is largest number"%n3)
        else:
            print("%d is largest number"%n2)

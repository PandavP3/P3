'''def sequential(a,n):
    flag=0
    for i in range(0,len(a)):
        if (a[i]==n):
            flag=0
            print("Number is present at location",(i+1))
        else:
            print("Number is not present in array")
            break
a = list(map(int,input("Enter element of array separated by space: ").split()))
n = int(input("Enter number to be scarched: "))
sequential(a,n)'''

'''import datetime
a = int(input("Enter Your birth date"))
b = int(input("Enter Your birth month"))
c = int(input("Enter Your birth Year"))
x = locale.local'''
e=dict()
d=dict()
a=input("Enter your name: ")
b=input("Enter your date of birth: ")
c=2022-int(b[6:])
d={a:c}
e.update(d)
print(e)



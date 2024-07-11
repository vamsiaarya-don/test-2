value=input("Enter the values. ex: 5 + 6")
x,y,z=value.split()
if len([x,y,z])!=3:
    print("please enter three values")

else:
    x=float(x)
    z=float(z)

if y=='+':
    result=x+z
elif y=='-':
    result=x-z
elif y=='*':
    result=x*z
elif y=='/':
    if z==0:
        print("you cannot divide a number by zero")
    else:
        result=x/z
else:
    print("illegal operator")

print(result)
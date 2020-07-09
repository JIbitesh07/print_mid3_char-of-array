z=str(input("enter a string:"))
a=len(z)
b=a%2
mid=" "
print("the length of the string:",a)
if(b==1):
    if(a>7):
        d=a//2
        for i in range(d-1,d+2):
            mid=mid+z[i]
        print(mid)
    else:
        print("the length of string is less than 7")
else:
    print("the length of string is even")

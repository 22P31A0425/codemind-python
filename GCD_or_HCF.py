def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
a,b=map(int,input().split())
#prints 12
#print("The gcd of 60 and 48 is:",end="")
print(hcf(a,b))
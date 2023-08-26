a,b,c=map(int,input().split())
if(a<=b and a<c):
    p=b+c
elif(b<=a and b<=c):
    p=a+c
else:
    p=a+b
print(p)
n=int(input())
I=0;
while(n>0):
    r=n%10
    if I<r:
        I=r
    n=int(n/10)
print(I)
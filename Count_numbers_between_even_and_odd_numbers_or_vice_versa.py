n=int(input())
b=list(map(int,input().split()))
s=0
s1=0
for i in range(0,n-2):
    if(b[i]%2!=0 and (b[i+2])%2==0):
        s+=1
    elif(b[i]%2==0 and (b[i+2])%2!=0):
        s1+=1
print(s+s1)
        
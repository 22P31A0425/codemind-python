a=int(input())
b=list(map(int,input().split()))
s=0
for i in range(1,a-1):
    if b[i]%2==0 and b[i-1]%2!=0 and b[i+1]%2!=0:
        s+=1
print(s)
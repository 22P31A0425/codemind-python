m,n=map(int,input().split())
mat=[]
for i in range(m):
    inner_list=list(map(int,input().split()))
    mat.append(inner_list)
s=0
s1=0
for i in range(m):
    for j in range(n):
        if i%2==0:        
            s+=mat[i][j]
        else:
            s1+=mat[i][j]
print(s,s1)
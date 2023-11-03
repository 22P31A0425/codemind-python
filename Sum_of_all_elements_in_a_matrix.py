m,n=map(int,input().split())
mat=[]
for i in range(m):
    inner_list=list(map(int,input().split()))[:n:]
    mat.append(inner_list)
s=0
#Element based accessing
for inner_list in mat:  
    for every_value in inner_list:        
        s+=every_value
print(s)
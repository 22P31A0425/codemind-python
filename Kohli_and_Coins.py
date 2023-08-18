z=int(input())
if(z%10==0):
    print(z//10)
elif(z%5==0 and z%10!=0):
    print(z//10+1)
else:
    print("-1")
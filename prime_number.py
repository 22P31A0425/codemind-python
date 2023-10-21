num=int(input())
#To take input from the user
#num=int(input("Enter a number:"))
if num==1:
    print("not a prime")
elif num>1:
    #check for factors
    for i in range(2,num):
        if(num%i)==0:
            print("not a prime")
            #print(i,"times",num//i,"is",num)
            break
    else:
        print("prime")
#if input number is less than
#or equal to 1,it is not prime
else:
    print("not a prime")
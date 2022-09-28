def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return True
    else:
        return False
n=int(input())
c=1
for i in range(2,n+1):
    if(n%i==0 and prime(i)):
        c+=1
print(c)

    
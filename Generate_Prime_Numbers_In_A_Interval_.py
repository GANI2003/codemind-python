def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
for i in range(n,m+1):
    if i>1:
        if prime(i):
            print(i)
n=int(input())
a=list(map(int,input().split()))
ev=0
for i in range(n):
    if a[i]%2==0:
        ev=ev+1
print(ev,n-ev)
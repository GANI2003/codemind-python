n=int(input())
arr=list(map(int,input().strip().split()))
s=0
c=0
for i in arr:
    s=s+i
aveg=s//n
for i in arr:
    if i>=aveg:
        c+=1
print(c)
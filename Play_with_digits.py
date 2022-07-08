n=int(input())
arr=list(map(int,input().strip().split()))
c=0
s=0
for i in arr:
    for j in str(i):
        s=s+int(j)
print(s)
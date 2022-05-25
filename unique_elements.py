n=int(input())
arr=list(map(int,input().strip().split()))
p=[]
for i in range(n):
    if arr[i] not in p:
        p.append(arr[i])
print(*p)        
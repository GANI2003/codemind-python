n=int(input())
arr=list(map(int,input().strip().split()))
sum=0
p=[]
for i in range(n):
    if arr[i] not in p:
        p.append(arr[i])
for i in range(len(p)):
    sum=sum+p[i]
print(sum)
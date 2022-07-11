n=int(input())
arr=list(map(int,input().strip().split()))
m=0
t=0
for i in range(n//2):
    m=m+arr[i]
for i in range(n//2,n):
    t=t+arr[i]
print(abs(t-m))
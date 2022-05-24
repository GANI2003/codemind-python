n=int(input())
arr=list(map(int,input().strip().split()))
b=int(input())
count=0
for i in range(n):
    if(arr[i]==b):
        count=count+1
print(count)
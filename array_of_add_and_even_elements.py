n=int(input())
arr=list(map(int,input().split()))[:n]
for i in range(n):
    if (arr[i]%2!=0):
        print(arr[i],end=" ")
for i in range(n):
    if(arr[i]%2==0):
        print(arr[i],end=" ")
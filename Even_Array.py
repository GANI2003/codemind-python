n=int(input())
arr=list(map(int,input().strip().split()))
count=0
for i in range(n):
    if arr[i]%2==0:
        count+=1
if n==count:
    print('True')
else:
    print('False')
    
       
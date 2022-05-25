n=int(input())
arr=list(map(int,input().strip().split()))
tc=0
c=0
for i in range(n):
    if arr[i]%2==0:
        tc=tc+1
    if i%2==0:
        if arr[i]%2==0:
            c=c+1
if c==tc:
    print("True")
else:
    print("False")
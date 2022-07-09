n=int(input())
arr=list(map(int,input().strip().split()))
s=0
for i in arr:
    s=s+i
aveg=s//n
for i in arr:
    if(i==aveg):
        print("True")
        break
else:
    print("False")

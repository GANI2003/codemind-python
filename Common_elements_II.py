m,n=map(int,input().strip().split())
arr1=list(map(int,input().strip().split()))
arr2=list(map(int,input().strip().split()))
l=[]
k=[]
for i in arr1:
    if i in arr1 and i not in l:
        l.append(i)
for i in arr2:
    if i in arr2 and i not in k:
        k.append(i)
for i in l:
    if i not in k:
        print(i,end=' ')
for  i in k:
    if i not in l:
        print(i,end=' ')
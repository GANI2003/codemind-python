n=list(input())
a=list(map(int,input().strip().split()))
k=list(a)
d=set(k)
s=0
for i in d:
    if i%2==0:
         s=s+1
print(s)
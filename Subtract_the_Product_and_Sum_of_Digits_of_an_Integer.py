n=int(input())
s=0
p=1
while(n>1):
    r=n%10
    s=s+r
    p=p*r
    n=n//10
d=p-s
print(d)
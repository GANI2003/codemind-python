n=input()
q=n.lower()
l=list(q)
for i in l:
    if(i==" "):
        l.remove(i)
s=set(l)
c=0
for i in s:
    if(l.count(i)==1):
        c+=1
print(c)
n=input()
a=0
for i in n:
    if i in '0123456789':
        a=a+int(i)
print(a)
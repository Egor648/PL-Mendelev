p=int(input())
c=1
b=1
while p!=0:
    v=int(input())
    p,v=v,p
    if v==p:
        c+=1
    if c>b:
        b=c
        if p!=v:
            c=1
print(b)

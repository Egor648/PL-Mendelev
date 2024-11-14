n=int(input())
if n>0:
    for k in range (1, n+1):
        a,j=[],k
        while j:a.append(j%10);j//=10
        if 0 not in a:
            yes=True
            for b in a:
                if k%b:yes=False;break
            if yes: print(k, sep=',end')
        

n = int(input())
a =[list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        a[j].append(a[i][j])
for k in range(n):
    for i in range(n):
        a[i].pop(0)
for i in range(len(a)):
    print(*a[i])

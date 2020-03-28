def root(a,i):
    while(a[i]!=i):
        i=a[i]
    return i
def union(a,size,u,v):
    rootu=root(a,u)
    rootv=root(a,v)
    if size[rootu]<size[rootv]:
        a[rootu]=a[rootv]
        size[rootv]+=size[rootu]
    else:
        a[rootv]=a[rootu]
        size[rootu]+=size[rootv]
def find(a,u):
    count=0
    for i in range(0,len(a)):
        if root(a,u) == root(a,i):
            count+=1
    return count
N,Q=map(int,input().split())
a=[]
size=[]
for i in range(0,N+1):
        a.append(i)
        size.append(1)

for _ in range(Q):
    l=list(map(str,input().split()))
    if l[0]=='M':
        union(a,size,int(l[1]),int(l[2]))
    elif l[0]=='Q':
        val=root(a,int(l[1]))
        print(size[val])

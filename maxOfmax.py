import sys
def algo(A,N):
    maxVal=-sys.maxsize-1
    tempMax=0
    inds=0
    tempinds=0
    s=0
    for i in range(0,N):
        tempMax=tempMax+A[i]
        
        if maxVal<tempMax:
            maxVal=tempMax
            tempinds=s
            inds=i
        if tempMax<0:
            tempMax=0
            s=i+1
    return [maxVal,tempinds,inds]
N=int(input())
A=list(map(int,input().split()))
val=algo(A,N)
flag=0
for i in range(0,len(A)):
    if A[i]<=0:
        flag=1
if flag==0:
    print(sum(A))
    print(0)
else:
    val=algo(A,N)
    B=A[:val[1]]+A[val[2]+1:]
    if len(B)==0:
        print(val[0])
        print(0)
    else:
        val1=algo(B,len(B))
        print(val[0])
        print(val1[0])

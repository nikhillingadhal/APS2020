def weightedUniformStrings(s, queries):
    d={}
    l=[]
    for i in s:
        d[i]=0
    for i in s:
        d[i]+=ord(i)-96
    for i in range(0,len(queries)):
        if queries[i] in list(d.values()):
            l.append("Yes")
        else:
            l.append("No")
    return l
s=input()
q=list(map(int,input().split()))
print(weightedUniformStrings(s,q))

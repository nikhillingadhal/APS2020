def countDigits(n):
    count=0
    while(n!=0):
        n=n&(n-1)
        count+=1
    return count
def acmTeam(topic):
    l=[]
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            val=int(topic[i],2) | int(topic[j],2)
            l.append(val)
    k=[]
    for i in range(len(l)):
        k.append(countDigits(l[i]))
    val=max(k)
    count=0
    for i in range(len(k)):
        if k[i]==val:
            count+=1
    return [val,count]
n=int(input())
topic=[]
for _ in range(n):
    topic_item = input()
    topic.append(topic_item)
print(acmTeam(topic))

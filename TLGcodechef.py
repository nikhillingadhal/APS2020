T=int(input())
p1s=[]
p2s=[]
dif=[]
for i in range(0,T):
	p1,p2=map(int,input().split())
	if p1s==[] and p2s==[]:
		p1s.append(p1)
		p2s.append(p2)
		if p1>p2:
			dif.append([p1-p2,1])
		else:
			dif.append([p2-p1,2])
	else:
		val1=p1s[len(p1s)-1]+p1
		val2=p2s[len(p2s)-1]+p2
		p1s.append(val1)
		p2s.append(val2)
		if val1>val2:
			dif.append([val1-val2,1])
		else:
			dif.append([val2-val1,2])
ans=max(dif)
print(ans[1],ans[0])

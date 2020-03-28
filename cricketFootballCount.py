from itertools import combinations
T=int(input())
for _ in range(0,T):
	p,q,r=map(int,input().split())
	f=[]
	c=[]
	for i in range(0,p):
		f.append(i)
	for i in range(0,q):
		c.append(i)
	fc=[]
	cc=[]
	for i in range(1,len(f)+1):
		fc.append(list(combinations(f,i)))
	for i in range(2,len(c)+1):
		cc.append(list(combinations(c,i)))
	fcs=[]
	ccs=[]
	print(fc)
	print(cc)
	for i in range(0,len(fc)):
		for j in range(0,len(fc[i])):
			fcs.append(len(fc[i][j]))
	for i in range(0,len(cc)):
		for j in range(0,len(cc[i])):
			ccs.append(len(cc[i][j]))
	count=0
	print(ccs,fcs)
	for i in range(0,len(ccs)):
		for j in range(0,len(fcs)):
			if ccs[i]+fcs[j]==r:
				count+=1
				print(ccs[i],fcs[j],r)
	print(count)

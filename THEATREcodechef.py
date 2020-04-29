from itertools import permutations
T=int(input())
lis=[]
for _ in range(T):
	N=int(input())
	tab=[]
	for i in range(4):
		l=[]
		for j in range(4):
			l.append(0)
		tab.append(l)
	for i in range(N):
		m,t=input().split()
		if t=='12':
			j=0
		elif t=='3':
			j=1
		elif t=='6':
			j=2
		elif t=='9':
			j=3
		tab[ord(m)-65][j]+=1
	l=[0,1,2,3]
	val=[]
	result=[]
	per=list(permutations(l))
	for j in per:
		n=[]
		for i in range(0,4):
			n.append(tab[i][j[i]])
		result.append(n)
	val1=[]
	for i in result:
		newVal=100
		res=0
		while(len(i)!=0):
			v=max(i)
			if v==0:
				res-=100
			else:
				res+=(v*newVal)
				newVal-=25
			i.remove(v)
		val1.append(res)
	lis.append(max(val1))
	print(max(val1))
print(sum(lis))
